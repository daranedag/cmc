from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def contacto(request):
	context = {}
	return render(request, 'contacto/contacto.html', context)