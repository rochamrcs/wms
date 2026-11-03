from django.test import TestCase
from django.urls import reverse
from .forms import ProductForm
from products.models import Product
from django.contrib.auth.models import User


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


    def test_redirects_unauthenticated_user(self):

        product_url = reverse('products:new_product')
        login_url = reverse('accounts:login')
        response = self.client.get(product_url)
        self.assertRedirects(response, f'{login_url}?next={product_url}')


    def test_authenticated_user_can_access_product_creation_form(self):

        user = User.objects.create_user(username="testuser", password="testpassword")

        self.client.force_login(user)

        product_url = reverse('products:new_product')

        response = self.client.get(product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_form.html")


    def test_authenticated_user_can_create_product(self):

        user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.force_login(user)

        new_product = {
            "name": "Test Product",
            "code": "CX-12345"
        }

        product_url = reverse('products:new_product')
        product_list = reverse('products:product_list')

        response = self.client.post(product_url, data=new_product)
        self.assertRedirects(response, product_list)

        product = Product.objects.get(code=new_product["code"])
        self.assertEqual(product.name, new_product["name"])


    def test_invalid_product_is_not_created(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )
        self.client.force_login(user)

        new_product = {"name": "Test Product"}

        product_url = reverse("products:new_product")
        response = self.client.post(product_url, data=new_product)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_form.html")

        form = response.context["new_product"]
        self.assertIn("code", form.errors)
        self.assertEqual(form["name"].value(), new_product["name"])
        self.assertFalse(Product.objects.exists())


    def test_unauthenticated_user_cant_create_product(self):

        new_product = {
            "name": "Test Product",
            "code": "CX-12345"
        }

        product_url = reverse("products:new_product")
        login_url = reverse('accounts:login')
        response = self.client.post(product_url, data=new_product)
        self.assertRedirects(response, f'{login_url}?next={product_url}')
        self.assertFalse(Product.objects.exists())


    def test_authenticated_user_can_access_products_list(self):

        user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )
        self.client.force_login(user)

        Product.objects.create(name='Folha A4', code='CDE-900', status=True)

        product_url = reverse("products:product_list")
        response = self.client.get(product_url)
        self.assertContains(response, "Folha A4")
        self.assertContains(response, "CDE-900")

    def test_unauthenticated_user_cant_access_products_list(self):

        product_url = reverse('products:product_list')
        login_url = reverse('accounts:login')
        response = self.client.get(product_url)
        self.assertRedirects(response, f'{login_url}?next={product_url}')