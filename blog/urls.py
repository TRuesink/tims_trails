from django.urls import path
from . import views as blog_views

app_name = 'blog'

urlpatterns = [
	path(route='all/', view=blog_views.PostListView.as_view(), name='list'),
	path(route='create/', view=blog_views.PostCreateView.as_view(), name='create'),
	path(route='<slug:slug>/', view=blog_views.PostDetailView, name='detail'),
	path(route='user/<str:username>/', view=blog_views.UserPostListView.as_view(), name='user-list'),
	path(route='tag/<slug:slug>/', view=blog_views.TagPostListView.as_view(), name='tag-list'),
	path(route='<slug:slug>/update/', view=blog_views.PostUpdateView.as_view(), name='update'),
]
