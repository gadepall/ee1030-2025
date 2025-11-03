import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./code.so")
lib.point_line_plane_distance.restype = ctypes.c_double
lib.point_line_plane_distance.argtypes = [ctypes.c_double]*13

def distance(P, a, b, n, c):
    return lib.point_line_plane_distance(
        P[0], P[1], P[2],
        a[0], a[1], a[2],
        b[0], b[1], b[2],
        n[0], n[1], n[2],
        c
    )

# Input
P = [-1, -5, -10]
a = [2, -1, -2]
b = [3, 4, 2]
n = [1, -1, 1]
c = 5

# Compute distance
d = distance(P, a, b, n, c)
print("Distance =", d)

# Compute intersection point in Python (needed for plotting)
dot_na = np.dot(n, a)
dot_nb = np.dot(n, b)
lam = (c - dot_na) / dot_nb
X = np.array(a) + lam * np.array(b)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Line (parametric points)
t = np.linspace(-5, 5, 50)
line_pts = np.array([a + np.array(b)*ti for ti in t])
ax.plot(line_pts[:,0], line_pts[:,1], line_pts[:,2], 'b-', label='Line')

# Plane (mesh grid)
xx, yy = np.meshgrid(range(-10, 11), range(-10, 11))
zz = (c - n[0]*xx - n[1]*yy)/n[2]
ax.plot_surface(xx, yy, zz, alpha=0.3, color='cyan')

# Plot P and intersection X
ax.scatter(*P, color='red', s=50, label='Point P')
ax.scatter(*X, color='green', s=50, label='Intersection X')

# Distance line (P-X)
ax.plot([P[0], X[0]], [P[1], X[1]], [P[2], X[2]], 'r--', label='Distance')

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
 plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/4.10.10/figs/q8.png")
plt.show()
