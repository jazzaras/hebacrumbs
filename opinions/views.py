from django.shortcuts import render
from .models import Opin

# Create your views here.

def open(request):
	opin = Opin.objects
	return render(request, 'op/op.html', {'opin':opin})
