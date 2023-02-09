"""Auth_Referral_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path("account/", include("account.urls")),
    path("account2/", include("account2.urls")),
    path("referral/", include("referral.urls")),
    # email verification url
    path('verification/', include('verify_email.urls')),
    path("password_reset/",
		auth_views.PasswordResetView.as_view(
			template_name= "account/password-reset.html"
		),
		name= "password_reset"
	),
	path("password_reset_done/",
		auth_views.PasswordResetDoneView.as_view(
			template_name= "account/password-reset-done.html"
		),
		name= "password_reset_done"
	),
	path("password_reset_confirm/<uidb64>/<token>/",
		auth_views.PasswordResetConfirmView.as_view(
			template_name= "account/password-reset-confirm.html"
		),
		name= "password_reset_confirm"
	),
	path("password_reset_complete/",
		auth_views.PasswordResetCompleteView.as_view(
			template_name= "account/password-reset-complete.html"
		),
		name= "password_reset_complete"
	),
	path("oauth/", include("social_django.urls", namespace="social")),
]
