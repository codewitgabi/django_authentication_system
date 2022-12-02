from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form = form.save(commit= False)
			password1 = form.cleaned_data.get("password1")
			password2 = form.cleaned_date.get("password2")
			
			if password1 == password2:
				form.save()			
				return redirect("account2:register")
			else:
				messages.error(request, "Passwords do not match")
				return redirect("account2:register")
		#print(dir(form))
		#print(form.errors)
		print(form.errors.as_text())
		#print(form.error_messages.get("password_mismatch"))
	
	return render(request, "account2/register.html", {"form": form})