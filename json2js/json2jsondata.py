#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import codecs,locale,sys
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
import re, collections

"""
#	USO:
python json2jsondata.py

"""
# Archivo JSON a convertir
archivo = "json_sample.json"

# Abrir como json
with open(archivo) as jsonfile:
    datos = json.load(jsonfile)

with open(archivo, 'w') as jsonfile:
    json.dump(datos, jsonfile, separators=(',',':'))

# Abrir archivo como cadena
with open(archivo, 'r') as jsonfile:
    datos=jsonfile.read()

# Crear el jsondata.js correcto
with open("../jsondata.js","w") as jsonfile:
    jsonfile.write("var jsondata = '"+datos.replace("\\r","").replace("\\n","\\\\n").replace("\\t","\\\\t").replace('"','\\"').replace("'","\\'")+"';")