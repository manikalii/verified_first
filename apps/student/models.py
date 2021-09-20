from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Language(models.Model):
	language_name = models.CharField(max_length=30,unique=True)
	def __str__(self):
		return self.language_name

class Student(models.Model):
	# user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="student")
	name = models.CharField(max_length=200,null=True,blank=True)
	email = models.EmailField(max_length = 254,unique=True)
	phone = models.CharField(max_length=14,null=True,blank=True)
	languages = models.ManyToManyField(Language,blank=True)
	
	def __str__(self):
		return self.name