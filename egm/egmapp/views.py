# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Mapa,Encuestado,Codigo

def codigo(request):#tabla de codigos
    preguntas = []
    etiquetas = []
    codigodata = []
    codigo = Codigo.objects.all()
    for c in codigo:
        preguntas.append(c.preguntas)
        etiqueta = c.etiquetas
        codig = c.codigo
        codig = int(float(codig))#pasar a entero
        codigodata.append(codig)
        etiqueta = etiqueta.replace(str(codig)+"-"," ")#limpiar etiqueta
        etiquetas.append(etiqueta)

    context={
        'preguntas':preguntas,
        'etiquetas':etiquetas,
        'codigodata':codigodata


    }
    return render(request,"codigo.html",context)

def data(request): #Tabla de encuestados con encabezado de mapa
    mapa =  Mapa.objects.filter(show=True)
    persona = Encuestado.objects.all()#Consulta a la base de datos con un limite
    personadata = []
    encabezado = []
    for c in mapa:
        encabezado.append(c.campo)
    for p in persona:
        p = str(p)
        personadataexp = []
        for m in mapa:
            personadataexp.append(p[m.pinicial-1:m.pfinal])

        personadata.append(personadataexp)
    context={
        'encabezado':encabezado,
        'personadata':personadata

        }
    return render(request,"base.html",context)


def campo(request):#campo se tabla Mapa seleccionado por un check
    mapa =  Mapa.objects.filter(show=True)
    campo = []
    for m in mapa:
        campo.append(m.campo)

    context={
        'campo':campo
    }
    return render(request,"campo.html",context)#campos clarity

def medio_clarity(request):
    print "campitos"

    context={

    }
    return render(request,"medio_clarity.html",context)
