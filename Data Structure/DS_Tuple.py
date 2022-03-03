#Las tuplas son inalterables y siempre van entre parentesis
#NO PUEDEN SER ELIMINADAS xD
#Tupla vacia
import numbers


tup1 =()

#Asignar valores
tup2 =('Robert','California','1965','Dunder Mifflin','CEO','Pensilvania')
print(tup2[0]) #Posicion 0 de izquierda a derecha
print(tup2[1:4]) #De la posicion 1 a la 3, [1:4[

#Packing de tuplas
tuplaMamona = ('Raiden Shogun','Electro',5)
#Unpacking, extraer valores de la tuple mediante variables
(nombre,elemento,estrellas) = tuplaMamona
print(nombre)
print(elemento)
print(estrellas)

#Comparar tuplas (La comparacion siempre inicia con las primeras posiciones)
a = (5,4)
b = (5,6)
if (a>b):print("a is bigger")
else:print("b is bigger")

#Tuplas y diccionarios 
a = {'x':100, 'y':200} #Diccionario
b = list(a.items()) #Con Items transformo el diccionario a tupla y con list lo meto en un lista
#Lista de tuplas
print(b)


print(all(tuplaMamona)) #all() retorna TRUE si la Tupla esta vacia "Iterable object" OJETE ITERABLE JAJAJA
print(any(tuplaMamona)) #any() retorna FALSE si la tupla esta vacia
#max() Ver valor maximo en tuplas de numeros
#min() Ver valor minimo en tuplas de numeros
#sorted() Ordenar solo funcion con variables de un mismo tipo
print(len(tuplaMamona)) #Logitud de la tupla
