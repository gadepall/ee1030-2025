import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

# Load library
lib = ct.CDLL("./libcircle.so")

lib.circle_center_matrix.argtypes = [ct.c_double, ct.c_double,
                                     ct.POINTER(ct.c_double),
                                     ct.POINTER(ct.c_double),
                                     ct.POINTER(ct.c_double)]
lib.circle_center_matrix.restype = None

# Inputs
a, b = 6.0, 4.0
cx, cy, r = ct.c_double(), ct.c_double(), ct.c_double()

lib.circle_center_matrix(a, b, ct.byref(cx), ct.byref(cy), ct.byref(r))

print(f"Centre = ({cx.value}, {cy.value}), Radius = {r.value}")

# Plot
theta = np.linspace(0, 2*np.pi, 400)
X = cx.value + r.value*np.cos(theta)
Y = cy.value + r.value*np.sin(theta)

plt.plot(X, Y, label="Circle")
plt.scatter([0,a,0], [0,0,b], color="red", label="Given points")
plt.scatter([cx.value], [cy.value], color="green", marker="x", s=100, label="Centre")
plt.gca().set_aspect("equal", adjustable="box")
plt.title(f"Direct Matrix Expansion: Centre=({cx.value:.2f},{cy.value:.2f}), r={r.value:.2f}")
plt.legend(); plt.grid(True)
plt.savefig("circle.png")
plt.show()

