from django.contrib.auth.models import User
from django.test import TestCase


class UserApp(TestCase):
    username = "username"
    password = "password"

    def setUp(self):
        User.objects.create_user(self.id, self.password)

    def test_profile_created(self):
        queryset = User.objects.get(username__username=self.username)
        self.assertTrue(queryset)

    def user_profile_count(self):
        profile_count = User.objects.count()
        self.assertEqual(1, profile_count)
