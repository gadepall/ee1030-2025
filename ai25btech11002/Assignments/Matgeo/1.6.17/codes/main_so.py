import math
import ctypes   
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpim
from mpl_toolkits.mplot3d import Axes3D
from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen
#if using termux
#import subprocess
#import shlex
#end if
# Load the shared library
lib = ctypes.CDLL("./librank.so")

# Tell ctypes about the function signature
lib.rank.argtypes = [ctypes.c_int, ctypes.c_int,
                     np.ctypeslib.ndpointer(dtype=np.float32,
                                            ndim=2,
                                            flags="C_CONTIGUOUS")]
lib.rank.restype = ctypes.c_int

def c_matrix_rank(mat: np.ndarray) -> int:
    mat = np.array(mat, dtype=np.float32, order='C')  # ensure C-contiguous float32
    m, n = mat.shape
    return lib.rank(m, n, mat)
A = np.array([-2,-10,3]).reshape(-1,1)
B = np.array([1,-1,3]).reshape(-1,1)
C = np.array([3,5,3]).reshape(-1,1)

#rank of matrix
R=c_matrix_rank(np.hstack((A,B,C)))

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Flatten vectors before plotting
A, B, C = A.flatten(), B.flatten(), C.flatten()

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)

#Plotting all lines
ax.plot(x_AB[0,:],x_AB[1,:], x_AB[2,:],color='pink',label='$AB$')
ax.plot(x_BC[0,:],x_BC[1,:], x_BC[2,:],color='y',label='$BC$')

# Scatter plot
ax.scatter(*A, color='r', s=100, label='A(-2, -10, 3)')
ax.scatter(*B, color='g', s=100, label='B(1, -1, 3)')
ax.scatter(*C, color='b', s=100, label='C(3, 5, 3)')

#Annotating points
ax.text(*A, ' A', color='r', fontsize=10)
ax.text(*B, ' B', color='g', fontsize=10)
ax.text(*C, ' C', color='b', fontsize=10)\

#Setting axes' labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Points A, B, C and the line passing through')
ax.legend()
ax.grid(True)

# Save to figs folder
plt.savefig("../Figs/plot.png")
plt.show()
