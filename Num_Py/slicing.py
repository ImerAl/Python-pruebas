import numpy as np 

a = np.array([5,4,10,3,6,8,0])

print(a[1:4]) #Muestra los valores de la posicion 1 a la 3 (4-1)

print(a[:4]) #Desde el inicio hasta la posicion 3 (4-1)

#[INICIO,FINAL-1,STEP]

print(a[:6:3])