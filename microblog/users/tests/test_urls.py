from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import (
    register,
    profile
)
from django.contrib.auth.views import LoginView, LogoutView


class TestUrls(SimpleTestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.profile_url = reverse('profile')

    def test_register_view_url_resolves(self):
        self.assertEqual(resolve(self.register_url).func, register)

    def test_login_view_url_resolves(self):
        self.assertEqual(resolve(self.login_url).func.view_class, LoginView)

    def test_logout_view_url_resolves(self):
        self.assertEqual(resolve(self.logout_url).func.view_class, LogoutView)

    def test_profile_view_url_resolves(self):
        self.assertEqual(resolve(self.profile_url).func, profile)
