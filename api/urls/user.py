"""
implemented User api urls
"""

from django.urls import path
from api.views.user import UserListAPIView, UserRetrieveUpdateAPIView
"""

User urls for api

"""
app_name = "user"

urlpatterns = [
    path("", UserListAPIView.as_view(), name="list"),
    path("<int:pk>/", UserRetrieveUpdateAPIView.as_view(), name="detail"),
]
