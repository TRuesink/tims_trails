from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class TTUserRegisterView(CreateView):
	form_class = CustomUserCreationForm
	template_name = 'tt_user/register.html'


class HomeView(TemplateView):
	template_name = 'home.html'


class TTUserLoginView(LoginView):
	template_name = 'tt_user/login.html'


class TTUserLogoutView(LogoutView):
	template_name = 'tt_user/logout.html'


class TTUserUpdateView(UpdateView):
	form_class = CustomUserChangeForm
	model = CustomUser
	template_name = 'tt_user/update.html'

	slug_field = "username"
	slug_url_kwarg = "username"


class TTUserDetailView(DetailView):
	model = CustomUser
	template_name = 'tt_user/detail.html'

	slug_field = "username"
	slug_url_kwarg = "username"


