from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path("account/", include("account.urls")),
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
