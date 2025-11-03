import ctypes



import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg
import math

X = np.linspace(-10,10,100)
Y = np.linspace(-10,10,100)

Y1 = X*X+1
X1 = Y*Y+1

fig = plt.figure(figsize = (6,6))
ax = fig.add_subplot(111)

ax.plot(X,Y1)
ax.plot(X1,Y)
ax.scatter(1,2, label= 'P(1,2)')
ax.scatter(2,1, label = '$P_i(2,1)$')
ax.scatter(5,2, label = 'Q(5,2)')
ax.scatter(2,5, label = '$Q_i(2,5)$')

# Data for the line segments
x1, y1 = [1, 2], [2, 1]
x2, y2 = [2, 5], [5, 2]
x3, y3 = [1, 5], [2, 2]

# Plotting the line segments
plt.plot(x1, y1, marker='o')
plt.plot(x2, y2, marker='o')
plt.plot(x3, y3, marker='o', color = 'black')


ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')





ax.legend()
ax.grid(True)
plt.show()




c_lib=ctypes.CDLL('./18c.so')

c_lib.norm.argtypes = [ctypes.c_float, ctypes.c_float]
c_lib.norm.restype = ctypes.c_float


answer1 = c_lib.norm(
    ctypes.c_float(float(1)),
    ctypes.c_float(float(2)), 
)

answer2 = c_lib.norm(
    ctypes.c_float(float(5-1)),
    ctypes.c_float(float(2-2)), 
)
if(answer1 > answer2):
    print("PQ is less than $PP_i$")

else:
    print("PQ is greater than $PP_i$")