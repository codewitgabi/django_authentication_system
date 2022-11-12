from django import forms
from .models import User


class UserForm(forms.ModelForm):
	username = forms.CharField(
		widget= forms.TextInput(
			attrs= {
				"placeholder": "Username",
			}
		)
	)
	email = forms.CharField(
		widget= forms.TextInput(
			attrs= {
				"placeholder": "Email",
			}
		)
	)
	password = forms.CharField(
		widget= forms.PasswordInput(
			attrs= {
				"placeholder": "Password",
			}
		)
	)
	confirm_password = forms.CharField(
		widget= forms.PasswordInput(
			attrs= {
				"placeholder": "Confirm Password",
			}
		)
	)
	class Meta:
		model = User
		fields = [
			"username",
			"email",
			"password",
			"confirm_password"
		]
		
	def clean_username(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		if User.objects.filter(username= username).exists():
			raise forms.ValidationError("Username already in use.")
		else:
			return username
			
	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		if User.objects.filter(email= email).exists():
			raise forms.ValidationError("Email already in use.")
		else:
			return email
		
	def clean_password(self, *args, **kwargs):
		password = self.cleaned_data.get("password")
		if len(password) < 8:
			raise forms.ValidationError("Your password must contain at least 8 characters.")
		elif password.isdigit():
			raise forms.ValidationError("Your password can’t be entirely numeric.")
		elif password.isalpha():
			raise forms.ValidationError("Your password can’t be a commonly used password.")
		else:
			return password