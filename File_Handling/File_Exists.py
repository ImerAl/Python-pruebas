import imp
import sys
from os import path
from Basics import impresiones

#pathlib para versiones de la 3.4 para arriba ver si un file o directorio existe.
impresiones()
#Ver existencia del archivo
t = path.exists("example.txt")
print(t)

t2 = path.isfile('example.txt')
print(t2)

d = path.isdir('Basics')
print(d)