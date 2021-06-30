from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import UserSignInView, UserSignUpView,  UserProfileView
app_name = "user"
urlpatterns = [
    path("sign-up/", UserSignUpView.as_view(), name="sign-up"),
    path("sign-in/", UserSignInView.as_view(), name="sign-in"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", UserProfileView.as_view(), name="profile")
]