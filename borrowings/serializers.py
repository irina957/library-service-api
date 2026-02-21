from django.db import transaction
from rest_framework import serializers
from books.serializers import BookSerializer
from borrowings.models import Borrowing


class BorrowingReadSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = serializers.SlugRelatedField(read_only=True, slug_field="email")

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "user",
        )


class BorrowingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "book",
            "expected_return_date",
        )

    def validate(self, attrs):
        book = attrs["book"]
        if book.inventory <= 0:
            raise serializers.ValidationError("This book is out of stock.")
        return attrs

    def create(self, validated_data):
        book = validated_data["book"]
        with transaction.atomic():
            book.inventory -= 1
            book.save()
            return super().create(validated_data)
