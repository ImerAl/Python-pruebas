import numpy as np      

array_int = np.array([1,2,3,4])

array_string = np.array(['Weon','Wachin','Qliao'])

print(array_string)

array_numeros_string = np.array([1,2,3,4], dtype='S')

############## COPY VS VIEW ###############

a = np.array([1,2,3,4,5])

x = a.copy()

a[0] = 0

print(a)
print(x)

b = np.array([1,2,3,4,5,6])

y = b.view()

b[0] = 0

print(b)
print(y)