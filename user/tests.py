from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from django.test import TestCase


class UserApp(TestCase):
    username = "username"
    password = "password"
    email = "test@test.test"

    def setUp(self):
        User.objects.create_user(self.id, self.password, self.email)

    def test_profile_created(self):
        queryset = User.objects.get(username=self.username, password=self.password,
                                    email=self.email)
        self.assertEqual(queryset.username, str)
        self.assertEqual(queryset.password, str)
        self.assertEqual(queryset.email, str)

    def user_profile_count(self):
        profile_count = User.objects.count()
        self.assertTrue(1, profile_count)


"""

Implemented  Sign in  test cases for sign in view

"""


class SignInTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12',
                                                         email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
