import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- load shared library ---
lib = ctypes.CDLL("./libplane3d.so")

# define argtypes/restypes
lib.find_k.restype = ctypes.c_double
lib.find_k.argtypes = [ctypes.POINTER(ctypes.c_double),
                       ctypes.POINTER(ctypes.c_double),
                       ctypes.POINTER(ctypes.c_double),
                       ctypes.c_int]

lib.compute_n.argtypes = [ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double),
                          ctypes.c_double,
                          ctypes.POINTER(ctypes.c_double),
                          ctypes.c_int]

lib.compute_C.restype = ctypes.c_double
lib.compute_C.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]

lib.plane_distance.restype = ctypes.c_double
lib.plane_distance.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.c_int]

lib.foot_point.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double,
                           ctypes.POINTER(ctypes.c_double), ctypes.c_int]

# helper to convert numpy to C array
def c_arr(arr):
    return (ctypes.c_double * len(arr))(*arr.tolist())

# --- input data ---
n1 = np.array([1.0,1.0,1.0])
n2 = np.array([2.0,3.0,-1.0])
c1, c2 = 1.0, -4.0
ex = np.array([1.0,0.0,0.0])

n1_c, n2_c, ex_c = c_arr(n1), c_arr(n2), c_arr(ex)

# Step 1: find k
k = lib.find_k(ex_c, n1_c, n2_c, 3)

# Step 2: compute plane normal n = n1 + k n2
n_c = (ctypes.c_double * 3)()
lib.compute_n(n1_c, n2_c, ctypes.c_double(k), n_c, 3)
n = np.array([n_c[i] for i in range(3)])

# Step 3: compute constant C
C = lib.compute_C(c1, c2, k)

# Step 4: distance
dist = lib.plane_distance(n_c, C, 3)

# Step 5: foot of perpendicular from origin to plane
foot_c = (ctypes.c_double * 3)()
lib.foot_point(n_c, C, foot_c, 3)
foot = np.array([foot_c[i] for i in range(3)])

print("k =", k)
print("plane normal n =", n)
print("C =", C)
print("distance =", dist)
print("foot of perpendicular =", foot)

# --- Plotting ---
fig = plt.figure(figsize=(8,7))
ax = fig.add_subplot(111, projection='3d')

# x-axis
x_line = np.linspace(-6,6,50)
ax.plot(x_line, np.zeros_like(x_line), np.zeros_like(x_line), color='r', lw=3, label="x-axis")

# plane surface
xx, zz = np.meshgrid(np.linspace(-6,6,30), np.linspace(-6,6,30))
yy = (C - n[0]*xx - n[2]*zz)/n[1]
ax.plot_surface(xx,yy,zz,alpha=0.6,color='cyan')

# perpendicular
ax.plot([0, foot[0]], [0, foot[1]], [0, foot[2]], 'k--', lw=2, label="perpendicular")
ax.scatter(*foot, color='k', s=50)

# labels & view
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Plane (cyan) & x-axis (red)\nPerpendicular distance = {dist:.3f}")
ax.legend()
ax.view_init(elev=18, azim=60)
ax.set_box_aspect([1,1,1])

plt.tight_layout()
plt.savefig("plane.png")
plt.show()

