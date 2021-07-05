"""
implemented User api urls
"""

from django.urls import path
from api.views.user import UserListAPIView, UserRetrieveUpdateAPIView

app_name = "user"

urlpatterns = [
    path("", UserListAPIView.as_view(), name="list"),
    path("<int:pk>/", UserRetrieveUpdateAPIView.as_view(), name="detail"),
]
