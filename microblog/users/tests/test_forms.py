from django.test import TestCase
from users.forms import UserRegisterForm


class TestForms(TestCase):

    def test_valid_user_register(self):
        form = UserRegisterForm(data={
            'username': 'charlesdarwin',
            'email': 'charlesdarwin@microblogapp.com',
            'password1': 'madman000',
            'password2': 'madman000'
        })
        self.assertTrue(form.is_valid())

    def test_no_data_user_register(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_no_password1_register(self):
        form = UserRegisterForm(data={
            'username': 'charlesdarwin',
            'email': 'charlesdarwin@microblogapp.com',
            'password1': '',
            'password2': 'madman000'
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_no_password2_register(self):
        form = UserRegisterForm(data={
            'username': 'charlesdarwin',
            'email': 'charlesdarwin@microblogapp.com',
            'password1': 'madman000',
            'password2': ''
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_no_passwords_register(self):
        form = UserRegisterForm(data={
            'username': 'charlesdarwin',
            'email': 'charlesdarwin@microblogapp.com',
            'password1': '',
            'password2': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_no_mail_register(self):
        form = UserRegisterForm(data={
            'username': 'charlesdarwin',
            'email': '',
            'password1': 'madman000',
            'password2': 'madman000'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_no_username_register(self):
        form = UserRegisterForm(data={
            'username': '',
            'email': 'charlesdarwin@microblogapp.com',
            'password1': 'madman000',
            'password2': 'madman000'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_invalid_mail_register(self):
        form = UserRegisterForm(data={
            'username': 'charlesdarwin',
            'email': 'charlesdarwin',
            'password1': 'madman000',
            'password2': 'madman000'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_username_spaces_mail_register(self):
        form = UserRegisterForm(data={
            'username': 'charles darwin',
            'email': 'charlesdarwin@microblogapp.com',
            'password1': 'madman000',
            'password2': 'madman000'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
