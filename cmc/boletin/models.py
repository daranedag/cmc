from django.db import models

# Create your models here.
class subscriptor(models.Model):
	subs_id = models.AutoField(primary_key=True)
	subs_nombre = models.CharField(max_length=50)
	subs_apellido = models.CharField(max_length=50)
	subs_mail = models.CharField(max_length=150)
	subs_telefono = models.CharField(max_length=12)
	subs_fecha = models.DateTimeField('Fecha de alta')
	subs_medioPago = models.CharField(max_length=1)

	def __str__(self):
		return self.subs_id

class boletin(models.Model):
	bltn_id = models.AutoField(primary_key=True)
	bltn_mes = models.CharField(max_length=2)
	bltn_fechaPub = models.DateTimeField('Fecha publicacion Boletin')
	bltn_archivo = models.FileField(upload_to='uploads/%Y/%m/%d')

	def __str__(self):
		return self.bltn_id

class envio(models.Model):
	env_id = models.AutoField(primary_key=True)
	env_subs_id = models.IntegerField()
	env_bltn_id = models.IntegerField()
	env_fechaEnvio = models.DateTimeField('Fecha envio Boletin')
	env_estadoEnvio = models.BooleanField(default='false')

	def __str__(self):
		return self.env_id