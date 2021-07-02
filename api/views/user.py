"""
Implemented User views API
"""""
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from user.serializers import UserSerializer


class UserListAPIVie(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
