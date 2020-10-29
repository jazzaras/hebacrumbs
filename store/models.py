from django.db import models

# Create your models here.

class Store(models.Model):
	title = models.CharField(max_length=200, default='')
	image = models.ImageField(upload_to='images/', null=True)
	summery = models.CharField(max_length=200, default='')

	def __str__(self):
	    return self.title
