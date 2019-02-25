from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import (
    register,
    profile
)
from django.contrib.auth.views import LoginView, LogoutView


class TestUrls(SimpleTestCase):

    def test_register_view_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)

    def test_login_view_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginView)

    def test_logout_view_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)

    def test_profile_view_url_resolves(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile)
