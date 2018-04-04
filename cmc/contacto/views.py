from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import ContactoForm

# Create your views here.

def contacto(request):
	if request.method == 'POST':
		form = ContactoForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = ContactoForm()
	context = {'form': form}
	return render(request, 'contacto/contacto.html', context)