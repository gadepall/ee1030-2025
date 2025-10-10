import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import ctypes

c_lib=ctypes.CDLL('./code.so')

c_lib.Solve_for_y.argtypes = [
        ctypes.c_double*2,
        ctypes.c_double*2
        ]

c_lib.Solve_for_y.restype = ctypes.c_double

A = (ctypes.c_double*2)(5.0, -6.0) 
B = (ctypes.c_double*2)(-1.0, -4.0)

y = c_lib.Solve_for_y(A,B)

y = np.round(y,2)

A = np.array([5,-6]).reshape(-1,1) 
B = np.array([-1,-4]).reshape(-1,1)

P = np.array([0.0,y]).reshape(-1,1)

plt.plot([A[0,0], B[0,0]], [A[1,0], B[1,0]], label="Line Segment $AB$")

x = np.array([A[0,0], B[0,0], P[0,0]])
y = np.array([A[1,0], B[1,0], P[1,0]])

plt.scatter(x,y, c='red')

vert_labels = ['A', 'B', 'P']

for i,txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({x[i]},{y[i]})',
                  (x[i],y[i]),
                  textcoords = "offset points",
                  xytext = (20,5),
                  ha = 'center')

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')


plt.savefig("../Figs/plot(py+C).png")

plt.show()

