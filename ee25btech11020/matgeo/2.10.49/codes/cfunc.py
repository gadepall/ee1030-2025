import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./cfunc.so")
lib.solve_q2_10_49.restype = ctypes.POINTER(ctypes.c_double)
lib.solve_q2_10_49.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

def solve_q2_10_49(A, B, C):
    A_arr = (ctypes.c_double * 3)(*A)
    B_arr = (ctypes.c_double * 3)(*B)
    C_arr = (ctypes.c_double * 3)(*C)

    res_ptr = lib.solve_q2_10_49(A_arr, B_arr, C_arr)
    result = np.array([res_ptr[i] for i in range(3)])
    return result

A = [2, 1, 1]
B = [1, -1, 1]
C = [3, 2, 6]

P_hat = solve_q2_10_49(A, B, C)
print("Unit vector P:", P_hat)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.view_init(elev=15,azim=165)
origin = [0,0,0]
ax.quiver(*origin, *A, color='r', label="A")
ax.quiver(*origin, *B, color='r', label="B")
ax.quiver(*origin, *C, color='r', label="C")
ax.quiver(*origin, *P_hat, color='g', label="P (unit)")
ax.text(A[0]*1.1, A[1]*1.1, A[2]*1.1, "A", color='r')
ax.text(B[0]*1.1, B[1]*1.1, B[2]*1.1, "B", color='r')
ax.text(C[0]*1.1, C[1]*1.1, C[2]*1.1, "C", color='r')
ax.text(P_hat[0]*1.1, P_hat[1]*1.1, P_hat[2]*1.1, "P", color='g')


ax.set_xlim([-4,4])
ax.set_ylim([-4,4])
ax.set_zlim([-4,4])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#plt.show()
plt.savefig("../figs/img.png", dpi=300)

