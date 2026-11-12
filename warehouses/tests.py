from django.test import TestCase
from django.urls import reverse
from warehouses.models import StorageLocation, Storage, LocationType
from django.contrib.auth.models import User

class AddressTestCase(TestCase):


    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.storage = Storage.objects.create(name="Depósito A")
        self.location_type = LocationType.objects.create(name="Armazanagem")

        self.data = {
            "address": "A-01",
            "storage": self.storage.pk,
            "capacity": "10",
            "capacity_unit": "PL",
            "location_type": self.location_type.pk
        }

    def test_authenticated_user_can_list_address_and_return_200(self):

        self.client.force_login(self.user)

        url = reverse('warehouses:address_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_authenticated_user_can_create_address(self):

        self.client.force_login(self.user)

        address_url = reverse('warehouses:new_address')
        address_list = reverse('warehouses:address_list')
        response = self.client.post(address_url, data=self.data)
        self.assertRedirects(response, address_list)

        address = StorageLocation.objects.get(address=self.data["address"])
        self.assertEqual(address.address, self.data["address"])


