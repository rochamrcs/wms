from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=25, unique=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
