from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()


class ContactForm(forms.Form):
	fullName = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"form_full"}))
	Email 	 =	forms.EmailField()
	content  = forms.CharField()



class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
	username = forms.CharField()
	Email 	 = forms.EmailField(widget=forms.EmailInput)
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)


	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)

		if qs.exists():
			raise forms.ValidationError("username exists")

		return username


	def clean_Email(self):
		username = self.cleaned_data.get("Email")
		qs = User.objects.filter(email=username)

		if qs.exists():
			raise forms.ValidationError("email exists")

		return username


	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")

		if password != password2:
			raise forms.ValidationError("Password must match")

		return data