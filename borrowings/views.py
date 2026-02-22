from django.utils import timezone
from rest_framework.decorators import action
from django.db import transaction
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from borrowings.models import Borrowing
from borrowings.serializers import BorrowingReadSerializer, BorrowingCreateSerializer


class BorrowingViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Borrowing.objects.select_related("book", "user")
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "create":
            return BorrowingCreateSerializer
        return BorrowingReadSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset

        user_id = self.request.query_params.get("user_id")
        is_active = self.request.query_params.get("is_active")

        if not user.is_staff:
            queryset = queryset.filter(user=user)
        else:
            if user_id:
                queryset = queryset.filter(user_id=user_id)

        if is_active is not None:
            is_active_bool = is_active.lower() == "true"
            queryset = queryset.filter(actual_return_date__isnull=is_active_bool)

        return queryset

    @action(methods=["post"], detail=True, url_path="return")
    def return_borrowing(self, request, pk=None):
        borrowing = self.get_object()
        book = borrowing.book
        if borrowing.actual_return_date is None:
            with transaction.atomic():
                book.inventory += 1
                borrowing.actual_return_date = timezone.now().date()
                book.save()
                borrowing.save()
                return Response(BorrowingReadSerializer(borrowing).data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "This borrowing has already been returned."},
            status=status.HTTP_400_BAD_REQUEST
        )
