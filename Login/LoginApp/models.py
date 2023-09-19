from django.db import models

# Create your models here.

class loginModel(models.Model):
	fname = models.CharField(max_length = 30)
	lname = models.CharField(max_length = 30)
	email = models.CharField(max_length = 30)
	uname = models.CharField(max_length = 30)
	password = models.CharField(max_length = 30)
	cpassword = models.CharField(max_length = 30)

	def __str__(self):
		return self.fname + " " + self.lname + " " + self.email + " " + self.uname + " " + self.password + " " + self.cpassword
