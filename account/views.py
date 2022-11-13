from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.contrib import messages
from referral.models import Referral, ReferralNotification

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
			print(form.cleaned_data)
			username = form.cleaned_data.get("username")
			password1 = form.cleaned_data.get("password")
			password2 = form.cleaned_data.get("confirm_password")
			
			if password1 == password2:
				form = form.save(commit= False)
				form.set_password(password1)
				form.save()
				messages.success(request, f"Account for {username} created successfully")
				return redirect("account:login")
			else:
				messages.error(request, "Passwords do not match")
				return redirect("account:signup")
		else:
			print("Invalid Form Input")
	
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
			print(form.cleaned_data)
			print(referral_code)
			if Referral.objects.filter(referral_code= referral_code).exists():
				username = form.cleaned_data.get("username")
				password1 = form.cleaned_data.get("password")
				password2 = form.cleaned_data.get("confirm_password")
				ref_code_owner = Referral.objects.get(referral_code= referral_code).user
				
				if password1 == password2:
					form = form.save(commit= False)
					form.set_password(password1)
					form.save()
					
					# create notification
					ReferralNotification.objects.create(
						user= ref_code_owner,
						message= f"{username} just signed up using your referral code",
					)
					
					messages.success(request, f"Account for {username} created successfully")
					return redirect("account:login")
				else:
					messages.error(request, "Passwords do not match")
					return redirect("account:signup")
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