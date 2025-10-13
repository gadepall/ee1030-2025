import math
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA


A = np.array([5,-6])
B = np.array([-1,-4])

k = -(A[0])/(B[0])

y = (A[1] + k*B[1])/(k+1)

y = np.round(y,2)

P = np.array([0.0,y]).reshape(-1,1)

A = A.reshape(-1,1)
B = B.reshape(-1,1)

plt.plot([A[0,0], B[0,0]], [A[1,0],B[1,0]], label = "Line Segment $AB$")

x = np.array([A[0,0], B[0,0], P[0,0]])
y = np.array([A[1,0], B[1,0], P[1,0]])

plt.scatter(x,y, c='red')

vert_labels = ['A', 'B', 'P']

for i,txt in enumerate(vert_labels):
    plt.annotate(f'{txt}({x[i]},{y[i]})',
                  (x[i],y[i]),
                  textcoords = "offset points",
                  xytext = (20,5),
                  ha = 'center')


ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.savefig("../Figs/plot(py).png")
plt.show()

