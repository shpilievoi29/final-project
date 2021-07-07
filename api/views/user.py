"""
Implemented User views API
"""""
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from api.permissions import UserListAPIPermission, UserAPIPermission
from user.serializers import UserSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [UserListAPIPermission]


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [UserAPIPermission]
