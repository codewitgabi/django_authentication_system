from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
	path("", index, name= "index"),
	path("referral-notifications/",
		view_notification,
		name= "view_notification"
	),
]