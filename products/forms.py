from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):

    def clean_code(self):
        data_code = self.cleaned_data.get('code')

        return data_code.strip().upper()

    class Meta:
        model = Product
        fields = ["name", "code"]