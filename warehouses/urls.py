from django.urls import path
from warehouses.views import address_create, address_list


app_name = "warehouses"

urlpatterns = [
    path("", view=address_list, name="address_list"),
    path("new_address/", view=address_create, name="new_address")
]