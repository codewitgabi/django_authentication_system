from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseAdmin


class UserAdmin(BaseAdmin):
	add_fieldsets = (
		(None, {
			"classes": ("wide",),
			"fields": ("username", "email", "password1", "password2")
		}),
	)
	
	
admin.site.register(User, UserAdmin)