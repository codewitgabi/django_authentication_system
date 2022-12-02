from django.urls import path
from .views import *

app_name = "account2"
urlpatterns = [
	path("register/", register, name= "register"),
]