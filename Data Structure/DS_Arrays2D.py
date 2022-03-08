matriz = [[1,4,6,7],[5,8,10,5]]
print(matriz)
i=0

for rows in matriz:
   print(matriz[i])
   i+=1

#Agregar una fila en la matriz
matriz.insert(3,[4,5,6,0])   

i=0
for rows in matriz:
    print(matriz[i])
    i+=1

#Modificar  array[row] = [values] ^ array[row][column] = [value]
#Logitud len() Devuelve las filas de la matriz