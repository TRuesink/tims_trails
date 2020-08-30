from django.urls import path
from . import views as cooking_views

app_name = 'cooking'

urlpatterns = [
	path(route='home/', view=cooking_views.CookingHomeView.as_view(), name='home'),
]