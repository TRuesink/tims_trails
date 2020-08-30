from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

# Create your views here.

class GearHomeView(TemplateView):
	template_name = 'gear/gear_home.html'
	