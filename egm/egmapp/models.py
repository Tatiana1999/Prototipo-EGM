# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from egm import settings
from django.db import models



class Encuestado(models.Model):
    id_encuestado = models.TextField()
    contenido = models.TextField(blank=False,null=False)
    def __unicode__ (self):
 	    return self.contenido

class Codigo(models.Model):
    preguntas = models.TextField()
    etiquetas = models.TextField()
    codigo =  models.TextField()


class Mapa(models.Model):
    orden = models.IntegerField()
    campo = models.TextField()
    tipo = models.TextField()
    pregunta = models.TextField()
    longitud = models.IntegerField()
    pinicial = models.IntegerField()
    pfinal = models.IntegerField()
    show = models.BooleanField(default=False)
