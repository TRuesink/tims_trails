from django.urls import path
from . import views as trails_views

app_name = 'trails'

urlpatterns = [
	path(route='home/', view=trails_views.TrailsHomeView.as_view(), name='home'),
]