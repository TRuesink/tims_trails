from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from blog.models import Subscriber
from blog.forms import SubscriberForm, ContactForm
from django.core.mail import send_mail
from django.contrib import messages

'''
class TTUserRegisterView(CreateView):
	form_class = CustomUserCreationForm
	template_name = 'tt_user/register.html'
'''


class HomeView(TemplateView):

	def get(self, request, *args, **kwargs):
		view = HomeDisplayView.as_view()
		return view(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		view = SubscribeView.as_view()
		s_form = SubscriberForm(request.POST)
		if s_form.is_valid():
			messages.success(request, 'Thank you for Subscribing!')
			s_form.save()
			s_form.send_email()
		return view(request, *args, **kwargs)

class HomeDisplayView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super(HomeDisplayView, self).get_context_data(**kwargs)
		context['s_form'] = SubscriberForm()
		return context
	

class SubscribeView(FormView):
	template_name = 'home.html'
	form_class = SubscriberForm
	context_object_name = 's_form'

	def get_success_url(self):
		return reverse('home')

class IndependentSubscribeView(FormView):
	template_name = 'subscribe.html'
	form_class = SubscriberForm
	context_object_name = 's_form'
	success_url = '/'

	def form_valid(self, form):
		messages.success(self.request, 'Thank you for Subscribing!')
		form.send_email()
		form.save()
		return super().form_valid(form)



class TermsConditionsView(TemplateView):
	template_name = 'terms_and_conditions.html'

class PrivacyPolicyView(TemplateView):
	template_name = 'privacy_policy.html'

class CopyrightView(TemplateView):
	template_name = 'copyright.html'

class DisclaimerView(TemplateView):
	template_name = 'disclaimer.html'

class AboutMeView(TemplateView):
	template_name = 'about_me.html'

	def get_context_data(self, *args, **kwargs):
		context = super(AboutMeView, self).get_context_data(**kwargs)
		context['s_form'] = SubscriberForm()
		return context

	def post(self, request, *args, **kwargs):
		view = IndependentSubscribeView.as_view()
		s_form = SubscriberForm(request.POST)
		s_form.save()
		return view(request, *args, **kwargs)

class ContactMeView(FormView):
	template_name = 'contact_me.html'
	form_class = ContactForm
	context_object_name = 'form'
	success_url = '/'

	def form_valid(self, form):
		messages.success(self.request, 'Thank you for contacting me! I will be in touch soon')
		form.send_email()
		form.save()
		return super().form_valid(form)


'''
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
'''

