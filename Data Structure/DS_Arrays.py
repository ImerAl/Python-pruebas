from array import array


import array
arrayName = array.array('d',[4.5,5.6,-1.2])
print(arrayName[1])
print(arrayName)
#Insertar elemento array.insert(index,valor)
#Modificar array[index]=valor
#Pop arrar.pop(index)
arrayName.insert(3,7.4)
arrayName[1]=2.5
arrayName.pop(2)
print(arrayName)
