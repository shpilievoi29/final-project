"""
Implemented User views API
"""""
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.permissions import UserListAPIPermission, UserAPIPermission
from user.serializers import UserSerializer

"""

User views for api

"""


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserListAPIPermission]


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserAPIPermission]
