import numpy as np

### 1-D array ###

b = np.array([3,5,-5,67])
print(b[1])

### 2-D array ###

c = np.array([[3,5,-6],[4,6,-9]]) # [[ARRAY],[ARRAY]]  
print(c[1,2]) # array[row,column]

### 3-D array ###

d = np.array([[[3,5,6],[-1,0,8]],[[5,8,-4],[3,-7,8]]]) # [[[ARRAY],[ARRAY]],[[ARRAY],[ARRAY]]]
print(d[1,0,2]) # array[matrix row, submatrix row, submatriz column]