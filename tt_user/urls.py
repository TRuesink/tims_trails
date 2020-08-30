from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tt_user'

urlpatterns = [
	#path(route='login/',view=views.TTUserLoginView.as_view(), name='login'),
	#path(route='logout/',view=views.TTUserLogoutView.as_view(), name='logout'),
	#path(route='register/',view=views.TTUserRegisterView.as_view(), name='register'),
	#path(route='<slug:username>', view=views.TTUserDetailView.as_view(), name='detail'),
	#path(route='<slug:username>/update/', view=views.TTUserUpdateView.as_view(), name='update'),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)