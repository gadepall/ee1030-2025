import numpy as np


a = np.array([1, 0, 0])
b = np.array([0,1,0])
c = np.array([0.6, 0.8, 0])

x = np.dot(2*a-b, np.cross(2*b-c,2*c-a))
print("Value of x: ", x)
