from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
	id = models.UUIDField(
		primary_key=True,
		editable=False,
		default=uuid.uuid4)
	username = models.CharField(max_length= 100)
	email = models.EmailField(unique= True)
	
	REQUIRED_FIELDS = ["username"]
	USERNAME_FIELD = "email"
	
	def __str__(self):
		return self.username
		
		