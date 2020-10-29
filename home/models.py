from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200, default='')
	image = models.ImageField(upload_to='images/')
	summery = models.CharField(max_length=300)

	def __str__(self):
	    return self.title