from django.db import models
# Create your models here.

class Opin(models.Model):
	image = models.ImageField(upload_to='images/', null=True)
