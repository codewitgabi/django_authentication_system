from django.db import models
from account.models import User


class Referral(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE, blank= True, null= True)
	referral_code = models.CharField(max_length= 40)
	
	def __str__(self):
		return self.referral_code
		
		
class ReferralNotification(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE, blank= True, null= True)
	message = models.CharField(max_length= 200)
	date_created = models.DateTimeField(auto_now= True)
	seen = models.BooleanField(default= False)
	
	def __str__(self):
		return self.message

