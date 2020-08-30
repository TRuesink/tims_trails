from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

class CookingHomeView(TemplateView):
	template_name = 'cooking/cooking_home.html'
