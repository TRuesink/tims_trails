from django import forms
from .models import Post, Comment, Subscriber, Contact
from django.core.mail import send_mail
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = [
			'name',
			'email',
			'content',
		]

		widgets = {
			'name':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your name','rows':'1','cols':'10'}),
			'email':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your email','rows':'1','cols':'10'}),
			'content':forms.Textarea(attrs={'class': 'form-control','placeholder':'Type your reply','rows':'4','cols':'10'}),
		}

		labels = {
			'name':'',
			'email':'',
			'content':'',
		}


class SubscriberForm(forms.ModelForm):
	captcha_field = CaptchaField()
	class Meta:
		model = Subscriber
		fields = [
			'name',
			'email',
		]
		widgets = {
			'name':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your name','rows':'1','cols':'40'}),
			'email':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your email','rows':'1','cols':'10'}),
		}
		labels = {
			'name':'',
			'email':'',
		}

	def send_email(self):
		send_mail(
		    'Welcome to Tims Trails!',
		    'Welcome to Tims Trails! I am glad you decided to subscribe. I hope Tims Trails is a useful resource for you as you plan your next adventure. In addition, I would love to help in any way that I can - If you have any questions or would just like to chat, you can respond directly to this email and I will get back to you within 24 hrs. Happy Backpacking!',
		    'timstrails@gmail.com',
		    [self.cleaned_data['email']],
		    fail_silently=False,
		)

class ContactForm(forms.ModelForm):
	captcha_field = CaptchaField()
	class Meta:
		model = Contact
		fields = [
			'name',
			'email',
			'content',
		]

		widgets = {
			'name':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your name','rows':'1','cols':'10'}),
			'email':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your email','rows':'1','cols':'10'}),
			'content':forms.Textarea(attrs={'class': 'form-control','placeholder':'Type your question here','rows':'4','cols':'10'}),
		}

		labels = {
			'name':'',
			'email':'',
			'content':'',
		}

	def send_email(self):
		send_mail(
		    'Thanks for contacting Tims Trails!',
		    'I got your note! I will be in touch within 24 hours. Happy Backpacking!\n\n- Tim',
		    'timstrails@gmail.com',
		    [self.cleaned_data['email']],
		    fail_silently=False,
		)

		contact_question = f'{self.cleaned_data["name"]} SAID \n\n{self.cleaned_data["content"]}.\n\n Send reply to {self.cleaned_data["email"]}'

		send_mail(
		    'Someone contacted you!',
		    contact_question,
		    'timstrails@gmail.com',
		    ['timstrails@gmail.com'],
		    fail_silently=False,
		)







