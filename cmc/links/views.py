from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def links(request):
	context = {}
	return render(request, 'links/links.html', context)