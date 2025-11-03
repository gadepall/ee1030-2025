import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./librhombus.so")

lib.rhombus_vertex.argtypes = [
    ctypes.POINTER(ctypes.c_double), ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

def rhombus_vertex(n1, c1, n2, c2, O):
    n1_arr = (ctypes.c_double*2)(*n1)
    n2_arr = (ctypes.c_double*2)(*n2)
    O_arr  = (ctypes.c_double*2)(*O)
    res = (ctypes.c_double*2)()
    lib.rhombus_vertex(n1_arr, c1, n2_arr, c2, O_arr, res)
    return np.array([res[0], res[1]])

n1 = [1, -1]; c1 = -1
n2 = [7, -1]; c2 = 5
O  = [-1, -2]

V = rhombus_vertex(n1, c1, n2, c2, O)
print("Remaining vertex:", V)

A = np.array([1,2])          # solved earlier
C = 2*np.array(O) - A
B = 2*np.array(O) - V

points = np.array([A, V, C, B, A])
plt.plot(points[:,0], points[:,1], 'b-', linewidth=2)

for P,name in zip([A,V,C,B,O], ["A","V","C","B","O"]):
    plt.scatter(P[0],P[1],color="red")
    plt.text(P[0]+0.2, P[1]+0.2, name)

plt.axis("equal")
plt.grid(True)
plt.title("Rhombus from Given Lines and Centre")
plt.savefig("../figs/img1.png")

