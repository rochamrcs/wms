from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AuthTestCase(TestCase):


    def test_get_200_in_login_page(self):

        login_url = reverse('accounts:login')
        response = self.client.get(login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")


    def test_redirects_unauthenticated_user(self):

        login_url = reverse('accounts:login')
        response = self.client.get('/')
        self.assertRedirects(response, f'{login_url}?next=/')


    def test_invalid_login_credentials(self):

        credentials = {
            "username": "teste",
            "password": "123456"
        }

        login_url = reverse('accounts:login')
        response = self.client.post(login_url, data=credentials)
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertTrue(form.non_field_errors())


    def test_valid_login_credentials(self):

        user = User.objects.create_user(username="testuser", password="testpassword")

        credentials = {
            "username": "testuser",
            "password": "testpassword"
        }

        login_url = reverse('accounts:login')
        response = self.client.post(login_url, data=credentials)
        self.assertRedirects(response, "/")
        home_response = self.client.get("/")
        self.assertContains(home_response, user.username)


    def test_valid_login_redirects_to_next(self):

        user = User.objects.create_user(username="testuser", password="testpassword")

        credentials = {
            "username": "testuser",
            "password": "testpassword"
        }

        login_url = reverse('accounts:login')

        with self.settings(LOGIN_REDIRECT_URL="/test/"):
            response = self.client.post(f'{login_url}?next=/', data=credentials)
            self.assertRedirects(response, '/')


    def test_redirects_to_login_page_after_logout(self):

        user = User.objects.create_user(username="testuser", password="testpassword")

        credentials = {
            "username": "testuser",
            "password": "testpassword"
        }

        login_url = reverse('accounts:login')
        logout_url = reverse('accounts:logout')
        response = self.client.post(login_url, data=credentials)
        self.assertRedirects(response, "/")
        logout_response = self.client.post(logout_url)
        self.assertRedirects(logout_response, login_url)
        home_response = self.client.get("/")
        self.assertRedirects(home_response, f'{login_url}?next=/')


    def test_get_405_to_try_access_logout_route(self):

        user = User.objects.create_user(username="testuser", password="testpassword")

        credentials = {
            "username": "testuser",
            "password": "testpassword"
        }
        login_url = reverse('accounts:login')
        logout_url = reverse('accounts:logout')
        self.client.post(login_url, data=credentials)
        response = self.client.get(logout_url)
        self.assertEqual(response.status_code, 405)
        home_response = self.client.get("/")
        self.assertEqual(home_response.status_code, 200)