#Dictionary una coleccion sin orden y que pueda cambiar, en pares. Para (llave,valor)

#{key,value}
from ast import Str


dic = {'Tim':18,'Charlie':12}
print(dic['Charlie']) #Imprimir valor con un llave

#copy() copiar un diccionario a otro
boys = {'Charlie':18,'Michael':21}
girls ={'Tatiana':22}

studentB = boys.copy()
studentG = girls.copy()
print(studentB)
print(studentG)

#update() Agregar un diccionario a otro
dic.update({'Misato':25})
print(dic)

#items() retorna una lista de tuplas
print("Students %s" % dic.items())


#Comparar 2 diccionarios, si alguna llave ya existe en el diccionario
for key in boys.keys():
    if key in dic.keys():
        print(True)

    else:
        print(False)
            
        
#sort() 
students = list(dic.keys()) #Combierte en lista para hacer el sort solo de las llaves
students.sort() #Ordena
for S in students:
    print(":".join((S,str(dic[S])))) #Imprimie la llave en S y el valor en str(dic[S]) S es la llave.
print(students)

#del elimina un elemento
del dic['Charlie']
print(dic)

#Otras funciones cmp() ya lo soporta python 3
len(dic) #logitud
Str(dic) #Convertir un diccionario a un string printeable
