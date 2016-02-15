from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SignUp(models.Model):
	First_Name = models.CharField(max_length=25)
	Last_Name = models.CharField(max_length=25)
	Email = models.EmailField()
	Timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		
		return self.First_Name   