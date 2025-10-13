import ctypes
import numpy as np
import matplotlib.pyplot as plt


c_lib = ctypes.CDLL("./code.so")


c_lib.plane_from_vectors.argtypes = [ctypes.c_double*3,
                                   ctypes.c_double*3,
                                   ctypes.c_double*4]


a = (ctypes.c_double*3)(1.0, 1.0, 1.0) 
b = (ctypes.c_double*3)(1.0, -1.0, 1.0)
plane = (ctypes.c_double*4)(0.0, 0.0, 0.0, 0.0)

c_lib.plane_from_vectors(a,b,plane)

#a = np.array([1.0, 1.0, 1.0])
#b = np.array([1.0, -1.0, 1.0])


c = np.array([1.0,-1.0,-1.0])
v = np.array([3.0, -1.0, 3.0])

A, B, C, D = plane
#xx, yy = np.meshgrid(range(-5,6), range(-5,6))
xx, yy = np.meshgrid(np.linspace(-3, 3, 20), np.linspace(-3, 3, 20))


# Avoid divide by zero if C=0
#if C != 0:
zz = (-A*xx - B*yy - D)/C
#else:
#    zz = np.zeros_like(xx)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx, yy, zz, alpha=0.5, color='grey')

# Plot vectors for reference
ax.quiver(0,0,0, a[0],a[1],a[2], color="red", label=r"$\vec{a}$")
ax.quiver(0,0,0, b[0],b[1],b[2], color="blue", label=r"$\vec{b}$")
ax.quiver(0,0,0, c[0],c[1],c[2], color="orange", label=r"$\vec{c}$")
ax.quiver(0,0,0, v[0],v[1],v[2], color="black", label=r"$\vec{v}$")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.savefig("../Figs/plot(py+C).png")
plt.show()

