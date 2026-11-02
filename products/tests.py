from django.test import TestCase
from .forms import ProductForm
from products.models import Product


class ProductTestCase(TestCase):


    def test_normalization_product_form(self):

        form = ProductForm(data={
            "name": "Produto de teste",
            "code": " Abc-123 "
        })

        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(
            form.cleaned_data["code"],
            "ABC-123",
        )


    def test_reject_creation_of_duplicated_product(self):

        Product.objects.create(name='Folha A4', code='CDE-900', status=True)

        form = ProductForm(data={
            "name": "Caderno",
            "code": " cde-900 "
        })

        self.assertFalse(form.is_valid())
        self.assertIn("code", form.errors)