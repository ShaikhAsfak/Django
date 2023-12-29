from django import forms
from .models import UserModel

class SignUpForm(forms.ModelForm):
	class Meta:
		model=UserModel
		fields='__all__'

class LoginForm(forms.ModelForm):
	class Meta:
		model=UserModel
		fields=['username','password']
