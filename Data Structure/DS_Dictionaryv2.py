#Las llaves de un diccionario son unicas y pueden ser string, int, tuplas, etc. 
#Todas las llaves son del mismo tipo
dick = {"Name":[],"Element":[],"Stars":[]}
dick["Name"].append("Raiden Shogun")
dick["Element"].append("Electro")
dick["Stars"].append(5)
print(dick)

#Imprimir una posicion
print(dick["Name"])

#dictionary.clear() Para borrar todo el diccionario.
#dictionary.pop(key, value) Sacar un elemento del diccionario
dick.pop("Name")
print(dick)

#Agregar y modificar un campo
dick['Name']="Raiden"
print(dick)
dick['Name']="Yae Miku"
print(dick)
