import numpy as np

a = np.array([[2,1], [5,2]])
x,y = np.linalg.eig(a)
if(x[0]>0):
    print("The positive eigen value: ", x[0])
else:
    print("The positive eigen value: ", x[1])








