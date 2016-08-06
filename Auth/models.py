from __future__ import unicode_literals

from django.db import models
from default_app.models import features
# Create your models here.

class levels(models.Model):
	level_id = models.AutoField(primary_key = True)
	level_name = models.CharField(max_length = 10)
	features = models.ManyToManyField(features)
	valid = models.BooleanField(default = True)

class Auth(models.Model):
	username = models.CharField(max_length = 50)
	password = models.CharField(max_length = 150)
	level = models.ForeignKey(levels,null = True,blank = True)
	valid = models.BooleanField(default = False)
