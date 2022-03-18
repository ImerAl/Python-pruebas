import imp
import sys
from os import path


#pathlib para versiones de la 3.4 para arriba ver si un file o directorio existe.
try:
    
    #Ver existencia del archivo
    t = path.exists("example.txt")
    print(t)

    t2 = path.isfile('example.txt')
    print(t2)

    d = path.isdir('Basics')
    print(d)       
except print("Error NYAAAAAAAAAH"):
    pass

