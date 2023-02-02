from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields["password1"].help_text = None
		self.fields["password2"].help_text = None
		
		
	class Meta:
		model = User
		fields = [
			"username",
			"email",
			"password1",
			"password2"
		]
		
		