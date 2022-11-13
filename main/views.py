from django.shortcuts import render
from account.models import User
from referral.models import Referral, ReferralNotification


def index(request):
	if request.user.is_authenticated:
		referral_code = Referral.objects.get(user= request.user).referral_code
	else:
		referral_code = ""
	context = {
		"referral_code": referral_code
	}
	return render(request, "main/index.html", context)
	
	
def view_notification(request):
	if request.user.is_authenticated:
		notifications = ReferralNotification.objects.filter(user= request.user).order_by("-date_created")
	else:
		notifications = ""
	context = {
		"notifications": notifications
	}
	return render(request, "main/notification.html", context)