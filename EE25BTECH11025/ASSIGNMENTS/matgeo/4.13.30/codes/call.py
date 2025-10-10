import ctypes
import numpy as np


lib = ctypes.CDLL("./problem.so")

pointP = [0.00,0.00]
pointQ = [0.00,0.00]
pointR = [0.00,0.00]

for i in range(0,2):
    pointP[i] = lib.get_pointP(i)
for i in range(0,2):
    pointQ[i] = lib.get_pointQ(i)
for i in range(0,2):
    pointR[i] = lib.get_pointR(i)

normal = [0,0]
print(pointP)
print(pointQ)
print(pointR)

for i in range(0,2):
    normal[i] = pointQ[i] + pointR[i] - (2*pointP[i])
z = np.array(['x','y'])
z_t = z.T
k = 0.00
for i in range(0,2):
    k += ((pointQ[i]**2)+(pointR[i]**2)-(2*(pointP[i]**2)))/2
print(normal,z_t,'=',k,"\nHence the locus of S is a line.")


