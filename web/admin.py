# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from web.models import Noticia, Category

'''class PlantillaAdmin(admin.ModelAdmin):
	list_display = ('name', 'anio', 'sort_order', 'id')'''

class NoticiasDestacadasAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description','sort_order', 'category')
	list_filter = ('sort_order',)
	list_search = ('name','sort_order')

class CategoryAdmin(admin.ModelAdmin):
	pass


#admin.site.register(Plantilla,PlantillaAdmin)
admin.site.register(Noticia,NoticiasDestacadasAdmin)
admin.site.register(Category,CategoryAdmin)

# Register your models here.
