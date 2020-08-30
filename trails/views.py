from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

class TrailsHomeView(TemplateView):
	template_name = 'trails/trails_home.html'
