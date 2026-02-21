from rest_framework import viewsets, mixins
from borrowings.models import Borrowing
from borrowings.serializers import BorrowingReadSerializer


class BorrowingViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingReadSerializer
