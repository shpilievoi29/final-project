from rest_framework.permissions import BasePermission

"""
Implemented permissions for admin and registered Users
"""


class UserListAPIPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class UserAPIPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff
