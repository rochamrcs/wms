from django import forms
from warehouses.models import StorageLocation, Storage, LocationType


class StorageLocationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["storage"].queryset = Storage.objects.filter(status=True)
        self.fields["location_type"].queryset = LocationType.objects.filter(status=True)


    def clean_address(self):
        data_address = self.cleaned_data.get('address')
        return data_address.strip().upper()


    class Meta:
        model = StorageLocation
        fields = ["address", "storage", "capacity", "capacity_unit", "location_type"]
