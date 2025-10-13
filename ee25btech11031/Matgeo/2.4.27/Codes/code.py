import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA
import ctypes

c_lib=ctypes.CDLL('./code.so')

c_lib.Solve_for_y.argtypes = [
        ctypes.c_double*2,
        ctypes.c_double*2
        ]

c_lib.Solve_for_y.restype = ctypes.c_double

A = (ctypes.c_double*2)(1.0,5.0)
B = (ctypes.c_double*2)(4.0,6.0)

y = c_lib.Solve_for_y(A,B)

A = np.array([1,5]).reshape(-1,1)
B = np.array([4,6]).reshape(-1,1)
P = np.array([0,y]).reshape(-1,1)
M = np.array([2.5,5.5]).reshape(-1,1)

plt.plot([A[0,0],B[0,0]],[A[1,0],B[1,0]], label = "Line Segment $AB$")
plt.plot([P[0,0],M[0,0]],[P[1,0],M[1,0]], 'o--', label = "Perpendicular Bisector")


tri_coords = np.block([[A,B,P]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','P']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), 
                 textcoords="offset points", 
                 xytext=(20,5), 
                 ha='center') 

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

plt.savefig("../Figs/plot(py+C).png")
plt.show()
