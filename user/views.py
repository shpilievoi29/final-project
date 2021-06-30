from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, RedirectView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from user.forms import UserSignUpForm, UserSignInForm


class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = "user/register.html"

    def get_success_url(self):
        return self.request.GET.get("next") or reverse_lazy("user:sign-in")


class UserSignInView(LoginView):
    model = User
    template_name = "user/user_form.html"

    def get_success_url(self):
        return self.request.GET.get("next") or reverse_lazy("film:list")


class LogoutView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy("film:list")

    def logout(self, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(self, *args, **kwargs)


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "user/profile.html"
