from django.db import models
from django.shortcuts import render

# Create your models here.

class Store(models.Model):
	title = models.CharField(max_length=200, default='')
	image = models.ImageField(upload_to='images/', null=True)
	summery = models.CharField(max_length=200, default='')
	size0 = models.CharField(max_length=20, default='')
	price0 = models.CharField(max_length=20, default='')

	def __str__(self):
	    return self.title

	def sar(self):
		return self.price0 + ' SAR'

	def size(self):
		return self.size0 + ' cm' 	

	# def cart(self, request):
	# 	(request, 'store/store.html')
	# 	if request.GET.get('cartadd') == ('cartadd'):
	# 		return render(request, 'home/home.html')