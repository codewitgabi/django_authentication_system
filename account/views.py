from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.contrib import messages
from referral.models import Referral, ReferralNotification
from verify_email.email_handler import send_verification_email

def is_authenticated(func):
	def wrapper(request):
		if request.user.is_authenticated:
			return redirect("main:index")
		return func(request)
	return wrapper
	

@is_authenticated
def signup(request):
	form = UserForm()
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			inactive_user = send_verification_email(request, form)
			return redirect("account:login")
	context = {"form": form}
	return render(request, "account/register.html", context)


def signup_with_referral(request, referral_code):
	page = "from_referral"
	referral_code = get_object_or_404(Referral, referral_code= referral_code)
	redirect_ref_code = referral_code
	form = UserForm()
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			referral_code = request.POST.get("ref_code", None)
			inactive_user = send_verification_email(request, form)
			if Referral.objects.filter(
				referral_code= referral_code).exists():
				ref_code_owner = Referral.objects.get(referral_code= referral_code).user
				
				username = inactive_user.username
				# create notification
				ReferralNotification.objects.create(
					user= ref_code_owner,
					message= f"{username} just signed up using your referral code",
				)
					
				messages.success(request, f"Account for {username} created successfully")
				return redirect("account:login")
			else:
				messages.error(request, "Invalid Referral Code")
				return redirect("account:signup_with_referral", referral_code= redirect_ref_code)
		else:
			print("Invalid Form Input")
			
	context = {
		"form": form,
		"referral_code": referral_code,
		"page": page,
	}
	return render(request, "account/register.html", context) 