from django.shortcuts import render,redirect
from django.http import HttpRequest , HttpResponse
from . models import loginModel

# Create your views here.

def index(request):
	return render(request,'index.html')

def signup(request):
	return render(request,'signup.html')

def savedata(request):
	fname = request.GET.get('fname') #fname = request.GET['fname']
	lname = request.GET.get('lname') #lname = request.GET['lname']
	email = request.GET.get('email')
	uname = request.GET.get('uname')
	password = request.GET.get('password')
	cpassword = request.GET.get('cpassword')
	if (password != cpassword):
		return HttpResponse('<b>Password Does not Match<b><br>\
					  			<b><a href="/signup/">Sign Up Again</a></b>')
	else:
		data=loginModel(fname=fname,lname=lname,email=email,uname=uname,password=password,cpassword=cpassword)
		data.save()
		return render(request,'login.html')

def login(request):
	return render(request,'login.html')

def loginchk(request):
	uname = request.GET.get('uname')
	password = request.GET.get('password')
	# Method 1
	# data = loginModel.objects.all()
	# for d in data:
	# 	if (d.uname == uname and d.password == password):
	# 		return HttpResponse('<h2>You are login Successfully</h2>')
	# 	else:
	# 		return HttpResponse('<h2>Wrong Uname and Password</h2>')

	# Method 2
	data = loginModel.objects.all()
	dic={'User_Name':uname,'Data':data}
	for d in data:
		if (d.uname == uname and d.password == password):
			return render(request,'home.html',dic)
		
	return HttpResponse('<h2>Wrong Uname and Password</h2><br>\
					  			<b><a href="/login/">Login Again</a></b>')

def home(request):
	return render(request,'home.html')

def delete(request):
	id=request.GET['id']
	b=loginModel.objects.get(id=id)
	b.delete()
	return redirect(index)

def update(request):
	id=request.GET['id']
	data=loginModel.objects.get(id=id)
	return render(request,'edit.html',{'b':data})

def editAction(request):
	id=request.GET['id']
	udata=loginModel.objects.get(id=id)
	password=request.GET['password']
	cpassword=request.GET['cpassword']
	if (password != cpassword):
		return HttpResponse('<b>Password Does not Match<b><br>\
					  			<b><a href="/">Home Page</a></b>')
	else:
		udata.fname=request.GET['fname']
		udata.lname=request.GET['lname']
		udata.email=request.GET['email']
		udata.uname=request.GET['uname']
		udata.password=request.GET['password']
		udata.cpassword=request.GET['cpassword']
		udata.save()
		return redirect(login)
