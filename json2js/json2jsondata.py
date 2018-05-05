#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import codecs,locale,sys
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
import re, collections
import argparse
parser = argparse.ArgumentParser(description=u'Convierte un JSON a JS')
parser.add_argument("-f", "--file", required=True, help=u"Define el archivo de entrada JSON")
"""
#	USO:
python json2jsondata.py -f json_sample.json

"""
# Archivo JSON a convertir
args = parser.parse_args()
if args.file:
    archivo = args.file

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