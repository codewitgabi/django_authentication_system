from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm


class UserForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields["password1"].help_text = None
		self.fields["password2"].help_text = None
		
	password2 = forms.CharField(
		label="",
		required=False,
		widget=forms.PasswordInput(attrs={
			"style": "display: none;"
		})
	)
		
	class Meta:
		model = User
		fields = [
			"username",
			"email",
			"password1",
			"password2"
		]
		
	def clean_password1(self, *args, **kwargs):
		symbols = "@#_~[]{}()$&?%/"
		password = self.cleaned_data.get("password1")
		
		# MinimumLengthValidator
		if len(password) < 10:
			raise forms.ValidationError("Password is too short.")
		
		# CommonPasswordValidator
		if password.isdigit() or password.isalpha():
			raise forms.ValidationError("Password is too common.")
		
		# NoSymbolValidator
		if not any([sym in symbols for sym in password]):
			raise forms.ValidationError(f"Password should contain any of {symbols}")
			
		return password;
		
		
class CustomAdminPasswordChangeForm(
	AdminPasswordChangeForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		print(dir(self.fields["password2"]))
		self.fields["password1"].help_text = None
		self.fields["password2"].help_text = None
		self.fields["password2"].errors = None
		
	class Meta:
		model = User
		fields = "__all__"
		
	def clean_password1(self):
		symbols = "@#_~[]{}()$&?%/"
		password = self.cleaned_data.get("password1")
		
		# MinimumLengthValidator
		if len(password) < 10:
			raise forms.ValidationError("Password is too short.")
		
		# CommonPasswordValidator
		if password.isdigit() or password.isalpha():
			raise forms.ValidationError("Password is too common.")
		
		# NoSymbolValidator
		if not any([sym in symbols for sym in password]):
			raise forms.ValidationError(f"Password should contain any of {symbols}")
			
		return password;
		

class CustomPasswordChangeForm(PasswordChangeForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		print(self.fields)
		self.fields["old_password"].help_text = None
		self.fields["new_password1"].help_text = None
		self.fields["new_password2"].help_text = None
		
	new_password1 = forms.CharField(
		label="",
		required=False,
		widget=forms.PasswordInput(attrs={
			"style": "display: none;"
		})
	)
		
	class Meta:
		model = User
		fields = ["old_password", "new_password1"]
		
	def clean_new_password1(self):
		symbols = "@#_~[]{}()$&?%/"
		password = self.cleaned_data.get("new_password1")
		
		""" check if old password equals new password """
		if self.cleaned_data.get("old_password") == password:
			raise forms.ValidationError("New password cannot have same value as old password!")
		
		""" MinimumLengthValidator """
		if len(password) < 10:
			raise forms.ValidationError("Password is too short.")
		
		""" CommonPasswordValidator """
		if password.isdigit() or password.isalpha():
			raise forms.ValidationError("Password is too common.")
		
		""" NoSymbolValidator """
		if not any([sym in symbols for sym in password]):
			raise forms.ValidationError(f"Password should contain any of {symbols}")
			
		return password;
		