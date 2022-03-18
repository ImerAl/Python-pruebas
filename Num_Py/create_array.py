import numpy as np

ar = np.array([1,5,6,9])

print(ar)

### 0-D array ###

a = np.array(15)

### 1-D array ###

b = np.array([3,5,-5,67])

### 2-D array ###

c = np.array([[3,5,-6],[4,6,-9]]) # [[ARRAY],[ARRAY]]

### 3-D array ###

d = np.array([[[3,5,6],[-1,0,8]],[[5,8,-4],[3,-7,8]]]) # [[[ARRAY],[ARRAY]],[[ARRAY],[ARRAY]]]

print(d.ndim)