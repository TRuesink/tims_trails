from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from tt_user.models import CustomUser
from .models import Post, Comment, Subscriber
from .forms import CommentForm
from taggit.models import Tag


class PostListView(ListView):
	model = Post
	template_name = 'blog/post_list.html'
	context_object_name = 'posts'
	paginate_by = 6

	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		common_tags = Post.tags.most_common()[:10]
		for tag in common_tags:
			
		context['tags'] = common_tags

		return context

'''
class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'post'

'''


def PostDetailView(request, slug):
	#get the current post object
	post_obj = get_object_or_404(Post, slug=slug)

	comments = post_obj.comments.filter(active=True, parent__isnull=True)

	if request.method == 'POST':
		c_form = CommentForm(request.POST)
		if c_form.is_valid():
			parent_obj = None
			#get parent ID from hidden input
			try:
				parent_id = int(request.POST.get('parent_id'))
			except:
				parent_id = None
			# if parent_id has been submitted get parent_obj id
			if parent_id:
				parent_obj = Comment.objects.get(id=parent_id)
				#if parent object exists
				if parent_obj:
					reply_comment = c_form.save(commit=False)
					#assign parent object to reply comment
					reply_comment.parent = parent_obj

			# normal comment
			comment_obj = c_form.save(commit=False)
			comment_obj.post = post_obj
			comment_obj.save()
			return redirect('blog:detail', slug=slug)
	else:
		c_form = CommentForm()
	context = {
		'post':post_obj,
		'c_form':c_form,
		'comments':comments,
	}
	return render(request, 'blog/post_detail.html', context)


class PostCreateView(CreateView):
	model = Post
	template_name = 'blog/post_create.html'
	fields = [
		'title',
		'content',
	]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(UpdateView):
	model = Post
	template_name = 'blog/post_update.html'
	fields = [
		'title',
		'content',
	]


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_post_list.html'
	context_object_name = 'posts'

	slug_field = "username"
	slug_url_kwarg = "username"

	def get_queryset(self):
		user = get_object_or_404(CustomUser, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user)

	def get_context_data(self, **kwargs):
		context = super(UserPostListView, self).get_context_data(**kwargs)
		context['tags'] = Post.tags.most_common()[:10]
		context['current_tag'] = self.kwargs.get('slug')
		return context


class TagPostListView(ListView):
	model = Post
	template_name = 'blog/tag_post_list.html'
	context_object_name = 'posts'

	def get_queryset(self):
		tag = get_object_or_404(Tag, slug=self.kwargs.get('slug'))
		return Post.objects.filter(tags=tag)

	def get_context_data(self, **kwargs):
		context = super(TagPostListView, self).get_context_data(**kwargs)
		context['tags'] = Post.tags.most_common()[:10]
		context['current_tag'] = self.kwargs.get('slug')
		return context













