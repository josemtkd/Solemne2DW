# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

'''class Plantilla(models.Model):
	name = models.CharField(verbose_name='Título', max_length=144)
	description = models.TextField(verbose_name='Descripción')
	anio = models.PositiveIntegerField(verbose_name='Año')
	sort_order = models.IntegerField(verbose_name='Clasificación')'''

class Category(models.Model):
	name = models.CharField(max_length=144)
	created = models.DateTimeField(auto_now_add=True)
	modifed = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s (%s)" % (self.name, self.created)

class Noticia(models.Model):
	name = models.CharField(verbose_name='Título', max_length=144)
	description = models.TextField(verbose_name='Descripción')
	sort_order = models.BooleanField(verbose_name='Destacada')
	category = models.ForeignKey(Category,verbose_name='Categoría')
	created = models.DateTimeField(auto_now_add=True)
	modifed = models.DateTimeField(auto_now_add=True)
	photo = models.ImageField(upload_to='notice_image',blank=True)


	def __str__(self):
		return self.name