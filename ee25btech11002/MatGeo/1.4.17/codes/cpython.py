import sys
import ctypes
import numpy as np
import matplotlib.pyplot as plt


c_lib = ctypes.CDLL('./formula.so')


c_lib.section_formula.argtypes = [
    ctypes.POINTER(ctypes.c_float),  
    ctypes.POINTER(ctypes.c_float),  
    ctypes.POINTER(ctypes.c_float),  
    ctypes.c_int,                    
    ctypes.c_int,                    
    ctypes.c_int                     
]
c_lib.section_formula.restype = None  


k = 2  

A = np.array([2, -2], dtype=np.float32)
B = np.array([-7, 4], dtype=np.float32)


P = np.zeros(k, dtype=np.float32)
Q = np.zeros(k, dtype=np.float32)


m = 1
n = 2
c_lib.section_formula(
    P.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    m,
    n,
    k
)

m = 2
n = 1
c_lib.section_formula(
    Q.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), 
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    m,
    n,
    k
)

plt.plot([A[0], B[0]], [A[1], B[1]], label='Line AB', zorder=1)


all_points = np.vstack([A, B, P, Q])


plt.scatter(all_points[:, 0], all_points[:, 1], color='red', zorder=2)


vert_labels = ['A', 'B', 'P', 'Q']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({all_points[i, 0]:.1f}, {all_points[i, 1]:.1f})',
                 (all_points[i, 0], all_points[i, 1]),
                 textcoords="offset points", xytext=(0,10), ha='center')


ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid(True)
plt.axis('equal')
plt.savefig('plot_from_c_corrected.png')
plt.show()