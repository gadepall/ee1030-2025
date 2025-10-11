import ctypes
import numpy as np
import matplotlib.pyplot as plt
import math

lib=ctypes.CDLL('./libmat.so')

lib.soln.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,2)),
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,)),
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,))
]
lib.soln.restype=None

Amat = np.array([[np.sqrt(3)/2, 1/np.sqrt(2)],
              [1/2, -1/np.sqrt(2)]], dtype=np.float64)
Bmat = np.array([8, 0], dtype=np.float64)
result = np.zeros(2, dtype=np.float64)

lib.soln(Amat,Bmat,result)
b=result[0]
c=result[0]

#plot
A=np.array([c/math.sqrt(2),c/math.sqrt(2)])
B=np.array([0,0])
C=np.array([7,0])

plt.plot([A[0],B[0]],[A[1],B[1]],label='AB')
plt.plot([A[0],C[0]],[A[1],C[1]],label='AC')
plt.plot([B[0],C[0]],[B[1],C[1]],label='BC')

plt.text(A[0],A[1],"A")
plt.text(B[0],B[1],"B")
plt.text(C[0],C[1],"C")

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title("Triangle ABC")
plt.axis('equal')
plt.savefig('../figs/img.png')
plt.show()
