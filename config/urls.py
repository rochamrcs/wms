from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", view=views.home, name="home"),
    path("accounts/", include("accounts.urls")),
    path("products/", include("products.urls"))
]
