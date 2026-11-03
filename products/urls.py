from .views import product_create, product_list
from django.urls import path

app_name = "products"

urlpatterns = [
    path("new_product/", view=product_create, name="new_product"),
    path("", view=product_list, name="product_list")
]