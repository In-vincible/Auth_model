from __future__ import unicode_literals

from django.db import models

class modules(models.Model):
	module_id = models.AutoField(primary_key = True)
	module_name = models.CharField(max_length = 50)

class features(models.Model):
	feature_id = models.AutoField(primary_key = True)
	feature_name = models.CharField(max_length = 50)
	feature_module = models.ForeignKey(modules,null = True)
