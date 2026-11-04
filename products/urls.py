from .views import product_create, product_list, product_change_status
from django.urls import path

app_name = "products"

urlpatterns = [
    path("", view=product_list, name="product_list"),
    path("new_product/", view=product_create, name="new_product"),
    path("<int:pk>/change_status/", view=product_change_status, name="product_change_status")
]