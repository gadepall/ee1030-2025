import sys
import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C library
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

k = 3  # 3D points

A = np.array([1, -2, 3], dtype=np.float32)
B = np.array([3, 4, -5], dtype=np.float32)

P = np.zeros(k, dtype=np.float32)
Q = np.zeros(k, dtype=np.float32)

# Internal (2:3)
m, n = 2, 3
c_lib.section_formula(
    P.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    m, n, k
)

# External (2:3)
m, n = 2, -3   # equivalent to formula
c_lib.section_formula(
    Q.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), 
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    m, n, k
)

# Plot in XY-plane projection
plt.plot([A[0], B[0]], [A[1], B[1]], label='Line AB')

all_points = np.vstack([A, B, P, Q])
labels = ['A', 'B', 'P', 'Q']

plt.scatter(all_points[:, 0], all_points[:, 1], color='red')
for i, txt in enumerate(labels):
    plt.annotate(f'{txt}\n({all_points[i,0]:.1f}, {all_points[i,1]:.1f})',
                 (all_points[i,0], all_points[i,1]),
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

plt.savefig('figs/Plot_P.png')
plt.show()