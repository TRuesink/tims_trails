from django.db import models
from model_utils.models import TimeStampedModel
from django.urls import reverse
from django.conf import settings
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager



class Post(TimeStampedModel):
	title = models.CharField(max_length=255)
	post_image = models.ImageField(default='default.jpg', upload_to='blog_post_pics')
	description = models.TextField(default='provid short post description')
	content = RichTextUploadingField(blank=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
	slug = AutoSlugField(unique=True, always_update=False, populate_from="title")
	tags = TaggableManager()

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'slug':self.slug})

	def __str__(self):
		return f'{self.title}'


class Comment(TimeStampedModel):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	content = models.TextField(null=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	active = models.BooleanField(default=True)
	parent = models.ForeignKey('self', null=True, related_name='replies', on_delete=models.CASCADE)

	class Meta:
		ordering = ('created',)

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'slug':self.slug})

	def __str__(self):
		return f'{self.name} - comment'


class Subscriber(TimeStampedModel):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)

	def get_absolute_url(self):
		return reverse('home')

	def __str__(self):
		return f'{self.name} - subscriber'


class Contact(TimeStampedModel):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	content = models.TextField(null=True)

	def get_absolute_url(self):
		return reverse('home')

	def __str__(self):
		return f'{self.name} - contact'








