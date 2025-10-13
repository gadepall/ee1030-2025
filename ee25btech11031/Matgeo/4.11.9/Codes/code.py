import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import ctypes

c_lib=ctypes.CDLL('./code.so')

c_lib.POI_x.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,ctypes.c_double]

c_lib.POI_y.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,ctypes.c_double]


c_lib.POI_x.restype = ctypes.c_double
c_lib.POI_y.restype = ctypes.c_double


#coefficients of x,y,z in the 3 equations

a1, b1, c1 = 4.0, -1.0, 5.0
a2, b2, c2 = 1.0, 1.0, -5.0
a3, b3, c3 = 1.0, -4.0, 5.0

x1 = c_lib.POI_x(a1, b1, c1, a2, b2, c2)
y1 = c_lib.POI_y(a1, b1, c1, a2, b2, c2)

x2 = c_lib.POI_x(a2, b2, c2, a3, b3, c3)
y2 = c_lib.POI_y(a2, b2, c2, a3, b3, c3)

x3 = c_lib.POI_x(a3, b3, c3, a1, b1, c1)
y3 = c_lib.POI_y(a3, b3, c3, a1, b1, c1)

A = np.array([x1, y1])
B = np.array([x2, y2])
C = np.array([x3, y3])

plt.plot([A[0],B[0]],[A[1],B[1]], label = "$4x-y+5=0$")
plt.plot([C[0],B[0]],[C[1],B[1]], label = "$x+y-5=0$")
plt.plot([A[0],C[0]],[A[1],C[1]], label = "$x-4y+5=0$")

A = A.reshape(-1,1)
B = B.reshape(-1,1)
C = C.reshape(-1,1)

tri_coords = np.block([[A,B,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
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


