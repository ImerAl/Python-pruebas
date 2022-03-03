#Declaracion
a=4230
print(a)

#Re-declare, Podemos redeclarar las variables a pesar de hacer sido declaradas antes.
a='Puro sabor'
print(a)

#Concatenancion de Strings
# Error en concatenacion de String con Int ---> print("Sobrasousky" + 44)
#Concatenar String con INT
b=44
print(a + str(b)) #str() para convertir a string

#Variables locales: Utilizadas escificamente en una funcion o en un metodo.
#Variables globales: Utilizadas a lo largo del programa y declara de manera global.

d = 'XD'#Variable global
def unMetodo():
    c = 400 #Variable local
    print(c)

unMetodo()
print(d)

#Borrar variable mamahuevo
del(a) #Funcion del()
print(a)
