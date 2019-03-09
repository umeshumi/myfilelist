from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, LoginForm, RegisterForm

def homePage(request):
	context = {
	"home":"welcome to home"
	}
	return render(request,'home_page.html', context)

def about_page(request):
	context = {
	"home":"About page"
	}
	return render(request,'home_page.html', context)

def contact_page(request):
	form = ContactForm()
	context = {
	"home":"contact page",
	"form":form
	}

	if request.method == "POST":
		print(request.POST.get('name'))
	return render(request,'ontact.html', context)


def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
	"form":form
	}
	# print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user 	=	authenticate(request, username=username, password=password)
		# print(request.user.is_authenticated())

		if user is not None:
			# print(request.user.is_authenticated())
			login(request, user)
			return redirect("/login")
		else:
			print("Error")
		
	return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
	"form":form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("Email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create_user(username, email, password)
		print(new_user)
	return render(request, "auth/register.html", context)