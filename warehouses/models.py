from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class UnitOfMeasure(models.TextChoices):
    PALLET = "PL", "Pallet"
    KILOGRAM = "KG", "Kilogram"
    LITER = "L", "Liter"
    METER = "M", "Meter"


class Storage(models.Model):
    name = models.CharField(max_length=20, unique=True, blank=False, null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class LocationType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class StorageLocation(models.Model):
    address = models.CharField(max_length=20, blank=False, null=False)
    storage = models.ForeignKey(Storage, on_delete=models.PROTECT, related_name= "locations")
    is_available = models.BooleanField(default=True)
    capacity = models.DecimalField(max_digits=8, decimal_places=3, validators=[MinValueValidator(0)])
    capacity_unit = models.CharField(max_length=2,choices=UnitOfMeasure.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    location_type = models.ForeignKey(LocationType, on_delete=models.PROTECT, related_name="locations")

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=["address", "storage"],
                name="unique_address_per_storage",
            ),
        ]

    def clean(self):
        super().clean()

        if self.capacity is None:
            return

        if self.capacity_unit == UnitOfMeasure.PALLET and self.capacity != int(self.capacity):
            raise ValidationError({
                "capacity": "A capacidade em paletes deve ser um número inteiro.",
            })
    

    def __str__(self):
        return f"{self.storage} - {self.address}"
