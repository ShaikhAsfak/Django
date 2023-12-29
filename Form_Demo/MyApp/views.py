from django.shortcuts import render,redirect
from .models import UserModel
from .forms import SignUpForm
from .forms import LoginForm
from django.http import HttpRequest , HttpResponse
# from django.contrib.auth import authenticate
# Create your views here.


def index(request):
	if request.method == "POST":
		signup_form = SignUpForm(request.POST)
		if signup_form.is_valid():
			signup_form.save()
		return redirect(index)
	signup_form = SignUpForm()
	signup = UserModel.objects.all()
	context = {'signup_form':signup_form, 'signup':signup}
	return render(request,'homepage.html',context)

def login(request):
	if request.method == "POST":
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			"""if (username == login_form('username') and password == login_form('password')):"""
			username = login_form.cleaned_data.get('username')
			password = login_form.cleaned_data.get('password')
			res = UserModel.objects.filter(username=username,password=password)
			print(res)
			if len(res) > 0:
				return HttpResponse('Login Successfull')
		
	login_form = LoginForm()
	context = {'login_form':login_form}
	return render(request,'login.html',context)









# Ruff
# def login(request):
# 	if request.method == "POST":
# 		Login = LoginForm(request.POST)
# 		if Login.is_valid():
# 			username = request.POST.get['username']
# 			password = request.POST.get['password']
# 			user = authenticate(username=username , password=password)
# 			if user is not None:
# 				Login(request,user)
# 				return redirect(login)
# 		else:
# 			Login = LoginForm()
# 	return render(request,'login.html',context={'login_form':LoginForm})
