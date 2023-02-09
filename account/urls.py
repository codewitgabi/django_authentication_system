from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "account"
urlpatterns = [
	path("signup/", signup, name= "signup"),
	path("login/",
		auth_views.LoginView.as_view(
		template_name="account/login.html",
		redirect_authenticated_user= True),
		name= "login"
	),
	path("signup-referral/<str:referral_code>/",
		signup_with_referral,
		name= "signup_with_referral"
	),
	path("logout/",
		auth_views.LogoutView.as_view(
		template_name= "account/logout.html"),
		name= "logout"
	),
	path("settings/", settings_view, name='settings'),
	path("settings/change-password/",
		settings_password_change,
		name="settings_password_change"),
]