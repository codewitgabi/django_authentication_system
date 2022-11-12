from django.db.models.signals import post_save
from django.contrib.auth.models import User
from account.models import User
from .models import Referral, ReferralNotification
import random


def customer_referral_link(sender, instance, created, **kwargs):
	if created:
		# create referral link for user
		string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
		random_code = instance.username.upper() + "".join(random.choices(string, k= 4))
		referral_code = Referral.objects.create(
			user= instance,
			referral_code= random_code
		)
		referral_code.save()
		print("Created   code == {}".format(random_code))
		
		
post_save.connect(customer_referral_link, sender= User)