from django import forms
from .models import Documents
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
	last_name  = forms.CharField(max_length=30, required=False, help_text='Optional')
	email 	   = forms.EmailField(max_length=100, help_text='Required, Enter Valid Email Address')

	class Meta:
		model = User
		fields =['username', 'first_name', 'last_name','email', 'password1', 'password2']


class DocForm(forms.ModelForm):

	class Meta:
		model = Documents
		fields = ['Birth_Certificate', 'Degree_Certificate']