#Pagina Web Asesorías Tributarias Cynthia Morales

##Proyecto hecho con Django - Por Diego Araneda

Boceto Inicial

1.- Index
 1.1 Servicios
 	1.1.1 Remuneraciones y leyes sociales
 	1.1.2 Declaraciones de impuestos
 	1.1.3 Auditorias tributarias
 	1.1.4 Auditorias financieras
 	1.1.5 Creacion de empresas
 1.2 Productos
 1.3 Quien soy

2.- links de interes
 2.1 SII
 2.2 Articulos anexos
 	2.2.1 Remuneraciones y leyes sociales
 	2.2.2 Declaraciones de impuestos
 	2.2.3 Auditorias tributarias
 	2.2.4 Auditorias financieras
 	2.2.5 Creacion de empresas

3.- contacto
 3.1 formulario
 3.2 envio de correo a cinthia.e.morales@gmail.com
 3.3 link a facebook y otras redes sociales
 3.4 telefono: +56 9 45274351

4.- Calendario tributario
 4.1 Tipo Clientes 1
 4.2 Tipo Clientes 2

IMPORTANTE: Trabajar logos y diseño de colores de la pagina
IMPORTANTE: Revisar opcion de subscripcion para envio de boletines informativos
IMPORTANTE: Revisar opcion de calendario tributario


Estructura Django
base: cmc
apps:
	index
	links
	contacto
	boletin

Pagina Admin
superuser: daraneda;da172003672



Base de datos para boletin:
Tabla: subscriptor
	subs_id
	subs_nombre
	subs_apellido
	subs_mail
	subs_telefono
	subs_fecha
	subs_medioPago

Tabla: boletin
	bltn_id
	bltn_mes
	bltn_fechaPub
	bltn_archivo

Tabla: envio
	env_id
	env_subs_id
	env_bltn_id
	env_fechaEnvio
	env_estadoEnvio