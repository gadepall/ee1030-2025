import ctypes #python library for interacting with c codes such as .so files
import numpy as np
import matplotlib.pyplot as plt

so = ctypes.CDLL("./findpoint.so")#loads my C shared library so that python can call the function

so.findpoint.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
#Tells Python the types of arguments the C function expects.
so.findpoint.restypes = None
#tells py that it doesn't return a value

px = ctypes.c_double()#creates empty double variables
py = ctypes.c_double()

so.findpoint(-6.0, 10.0, 3.0, -8.0, 2, 7, ctypes.byref(px), ctypes.byref(py))#byref to direct python to the address

A = np.array([-6.0, 10.0])
B = np.array([3.0, -8.0])
P = np.array([px.value, py.value])

plt.plot([A[0], B[0]], [A[1], B[1]], 'g--', label="Line AB")
plt.scatter(*A, color="red")
plt.scatter(*B, color="blue")
plt.scatter(*P, color="black")

plt.text(*A, "A(-6,10)")
plt.text(*B, "B(3,-8)")
plt.text(P[0], P[1]+0.5, f"P({px.value:.1f},{py.value:.1f})")

plt.legend()
plt.axis("equal")
plt.grid(True)
plt.savefig("fig.png")
plt.show()
