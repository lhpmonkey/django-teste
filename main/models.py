from django.db import models
import datetime

# Create your models here.

class Contato(models.Model):

	SEXO_CHOICES = (
		(u'masculino', u'Masculino'),
		(u'feminino', u'Feminino'),
		)

	ESTADO_CIVIL_CHOICES = (
		(u'solteiro', u'Solteiro'),
		(u'casado', u'Casado'),
		)

	contato_id = models.AutoField(primary_key=True)
	contato_nome = models.CharField(max_length=50)
	contato_nascimento = models.DateField()
	contato_sexo = models.CharField(max_length=50, choices = SEXO_CHOICES)
	contato_estado_civil = models.CharField(max_length=50, choices= ESTADO_CIVIL_CHOICES, verbose_name='Estado Civil')
	contato_email = models.CharField(max_length=50)
	contato_favorito = models.BooleanField(verbose_name='Favorito')

class Post(models.Model):
	post_id = models.AutoField(primary_key=True)
	post_title = models.CharField(max_length=50)
	post_content = models.TextField()
	post_published_date = models.DateTimeField(default=datetime.datetime.now, blank=True)