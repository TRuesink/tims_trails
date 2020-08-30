"""tims_trails URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tt_user import views as TTUser_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('gear/', include('gear.urls', namespace='gear')),
    path('cooking/', include('cooking.urls', namespace='cooking')),
    path('trails/', include('trails.urls', namespace='trails')),
    path(route='terms-and-conditions/', view=TTUser_views.TermsConditionsView.as_view(), name='terms'),
    path(route='copyright-notice/', view=TTUser_views.CopyrightView.as_view(), name='copyright'),
    path(route='privacy-policy/', view=TTUser_views.PrivacyPolicyView.as_view(), name='privacy'),
    path(route='disclaimer/', view=TTUser_views.DisclaimerView.as_view(), name='disclaimer'),
    path(route='about-me/', view=TTUser_views.AboutMeView.as_view(), name='about'),
	path(route='', view=TTUser_views.HomeView.as_view(), name='home'),
    path(route='subscribe', view=TTUser_views.IndependentSubscribeView.as_view(), name='subscribe'),
    path(route='contact-me', view=TTUser_views.ContactMeView.as_view(), name='contact'),
    path('', include('tt_user.urls', namespace='tt_user')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
