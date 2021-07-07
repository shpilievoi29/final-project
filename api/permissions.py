from rest_framework.permissions import BasePermission


class UserListAPIPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class UserAPIPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
