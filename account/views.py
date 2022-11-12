from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages


def signup(request):
	form = UserForm()
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			username = form.cleaned_data.get("username")
			password1 = form.cleaned_data.get("password")
			password2 = form.cleaned_data.get("password2")
			
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


