from django.urls import path
from . import views as gear_views

app_name = 'gear'

urlpatterns = [
	path(route='home/', view=gear_views.GearHomeView.as_view(), name='home'),
]