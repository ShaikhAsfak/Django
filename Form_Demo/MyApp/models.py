from django.db import models

# Create your models here.


class UserModel(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	emailid = models.CharField(max_length=30)
	contactno = models.IntegerField()

	def __str__(self):
		return self.username + " " + self.password