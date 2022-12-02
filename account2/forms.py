from account.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.fields["username"].widget.attrs.update({
			"type": "text",
			"name": "username",
			"class": "form-control",
			"id": "yourUsername",
			"required": ""
		})
		self.fields["email"].widget.attrs.update({
			"type": "email",
			"name": "email",
			"class": "form-control",
			"id": "yourEmail",
			"required": ""
		})
		self.fields["password1"].widget.attrs.update({
			"type": "password",
			"name": "password",
			"class": "form-control",
			"id": "yourPassword",
			"required": "",
			"minlength": "10"
		})
		self.fields["password2"].widget.attrs.update({
			"type": "password",
			"name": "password2",
			"class": "form-control",
			"id": "yourPassword",
			"required": "",
			"minlength": "10"
		})
		
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]
		
	