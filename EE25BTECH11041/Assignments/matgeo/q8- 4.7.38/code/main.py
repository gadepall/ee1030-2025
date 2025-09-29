import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared C library
lib = ctypes.CDLL('./libplane.so')

# Define argument/return types
lib.find_plane.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C")]

# Prepare coeff array
coeff = np.zeros(4, dtype=np.float64)
lib.find_plane(coeff)

A, B, C, D = coeff
print("Required plane equation: {:.2f}x + {:.2f}y + {:.2f}z + {:.2f} = 0".format(A, B, C, D))

# Define planes
def plane1(x, y):
    return (4 - x + 2*y) / 3

def plane2(x, y):
    return (-5 + 2*x - y)

def plane3(x, y):
    return (-D - A*x - B*y) / C

# Grid
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

Z1 = plane1(X, Y)
Z2 = plane2(X, Y)
Z3 = plane3(X, Y)

# Plot
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z1, alpha=0.5, color='red', label="Plane 1")
ax.plot_surface(X, Y, Z2, alpha=0.5, color='blue', label="Plane 2")
ax.plot_surface(X, Y, Z3, alpha=0.7, color='green', label="Required Plane")

# Legend hack
plane_proxy = [plt.Rectangle((0,0),1,1,fc=c) for c in ["red","blue","green"]]
ax.legend(plane_proxy, ["Plane 1","Plane 2","Required Plane"])

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Intersection of Three Planes")
plt.savefig("figure.png", dpi=200)
plt.show()

