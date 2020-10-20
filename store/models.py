from django.db import models

# Create your models here.

class Store(models.Model):
	title = models.CharField(max_length=200, default='')
