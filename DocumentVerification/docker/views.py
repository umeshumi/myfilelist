from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import PageNotAnInteger, Paginator, PageNotAnInteger
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import Documents
from .forms import SignUpForm, DocForm
# Create your views here.
def home(request):
	return render(request, 'index.html')

@user_passes_test(lambda u: u.is_superuser)
def UserListView(request):
	users  = User.objects.all().exclude(is_superuser=True)
	page = request.GET.get('page')
	paginator = Paginator(users, 6)
	try:
		teacherss = paginator.get_page(page)
	except PageNotAnInteger:
		teacherss = paginator.get_page(1)
	except EmptyPage:
		teacherss = paginator.get_page(paginator.numbers)
	context={'teacher':teacherss}
	return render(request, 'userlist.html', context)

@login_required
def DocumentListView(request):
	try:
		docs  = Documents.objects.get(user=request.user)
		context={'teacher':docs}
		return render(request, 'doclist.html', context)
	except Documents.DoesNotExist:
		return HttpResponse('Sorry You Are Yet Uploaded file')

@user_passes_test(lambda u: u.is_superuser)
def DocVerify(request, userid):
	try:
		user  = User.objects.get(id=userid)
		Documents.objects.filter(user=user).update(Verification=True)
		return redirect('docker:home')
	except User.DoesNotExist:
		return Http404

@user_passes_test(lambda u: u.is_superuser)
def PersonDocumentView(request, userid):
	try:
		docs  = User.objects.get(id=userid)
	except User.DoesNotExist:
		raise Http404
	context={'teacher':docs}
	return render(request, 'docviewlist.html', context)

@login_required
def DocCreateView(request):
	if request.method == "POST":
		form = DocForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Documents(Birth_Certificate=request.FILES['Birth_Certificate'],Degree_Certificate=request.FILES['Degree_Certificate'])
			newdoc.user = request.user
			newdoc.save()
			return redirect('docker:doclist')
	else:
		form = DocForm()
	context = {'form':form}
	return render(request, 'docform.html', context)

@login_required
def DeleteDoc(request, docid):
	doc = Documents.objects.get(user_id=docid)
	doc.delete()
	return HttpResponseRedirect(reverse('docker:home'))

def SignUpView(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('docker:home')
	else:
		form = SignUpForm()
	context = {'form':form}
	return render(request, 'signupform.html', context)


def LogotView(request):
	logout(request)
	return redirect('docker:home')