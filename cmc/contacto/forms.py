from django import forms

class ContactoForm(forms.Form):
	nombre = forms.CharField(
		max_length=30,
		widget=forms.TextInput(
			attrs={
				'style': 'border-color: none',
				'placeholder': 'Escribe tu nombre aqui'
			}
		)
	)
	email = forms.EmailField(max_length=254)
	telefono = forms.CharField(max_length=12)
	mensaje = forms.CharField(max_length=2000, widget=forms.Textarea(), help_text='Deja tu mensaje aqui')

	def clean(self):
		cleaned_data = super(ContactoForm, self).clean()
		name = cleaned_data.get('Nombre')
		email = cleaned_data.get('email')
		phone = cleaned_data.get('phone')
		message = cleaned_data.get('message')

		if not name and not email and not phone and not message:
			raise forms.ValidationError('Todos los campos deben ser llenados')
