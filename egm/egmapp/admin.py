# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Mapa,Encuestado,Codigo
from import_export import resources
# Register your models here.

class MapaResource(resources.ModelResource):
    class Meta:
        model = Mapa
        exclude = ('imported')
        fields = ('id','orden','campo','tipo','pregunta','longitud','pinicial','pfinal','show')

class MapaAdmin(ImportExportModelAdmin):
    resource_class = MapaResource
    list_display = ['orden','campo','tipo','pregunta','longitud','pinicial','pfinal','show']
    list_editable = ['show']

class EncuestadoResource(resources.ModelResource):
    class Meta:
        model = Encuestado
        exclude = ('import')
        fields = ('id','id_encuestado','contenido')
class EncuestadoAdmin(ImportExportModelAdmin):
    resource_class = EncuestadoResource
    list_display = ['id','id_encuestado','contenido']

class  CodigoResource(resources.ModelResource):
    class Meta:
        model = Codigo
        exclude = ('import')
        fields = ('id','preguntas','etiquetas','codigo')

class CodigoAdmin(ImportExportModelAdmin):
    resource_class = CodigoResource
    list_display = ['id','preguntas','etiquetas','codigo']

admin.site.register(Mapa,MapaAdmin)
admin.site.register(Encuestado,EncuestadoAdmin)
admin.site.register(Codigo,CodigoAdmin)
