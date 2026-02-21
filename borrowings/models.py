from django.db import models
from django.core.exceptions import ValidationError

from django.conf import settings
from django.utils import timezone


class Borrowing(models.Model):
    borrow_date = models.DateField(auto_now_add=True)
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="borrowings",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="borrowings",
    )

    class Meta:
        ordering = ["-borrow_date"]

    def clean(self):
        current_borrow_date = self.borrow_date or timezone.now().date()

        if self.expected_return_date <= current_borrow_date:
            raise ValidationError(
                "Expected return date must be later than borrow date."
            )

        if self.actual_return_date:
            if self.actual_return_date < current_borrow_date:
                raise ValidationError(
                    "Actual return date cannot be earlier than borrow date."
                )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.title} borrowed by {self.user.email}"
