from django.shortcuts import render
from .models import Store

# Create your views here.

def home(request):
	return render(request, 'home/home.html')

def store(request):
	store = Store.objects
	return render(request, 'store/store.html', {'store':store})

def test(request):
	return render(request, 'home/test2.html')