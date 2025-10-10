import matplotlib.pyplot as plt
import numpy as np
import ctypes

# Load C library
lib = ctypes.CDLL("./plane_points.so")
lib.generate_plane_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
lib.generate_plane_points.restype = None

# --- Choose numeric a, b, c satisfying 1/a^2 + 1/b^2 + 1/c^2 = 1 ---
a = b = c = np.sqrt(3)  # This ensures plane distance = 1

# Generate points
points_array = (ctypes.c_double * 9)()
lib.generate_plane_points(a, b, c, points_array)
A = np.array(points_array[0:3])
B = np.array(points_array[3:6])
C = np.array(points_array[6:9])
D = (A + B + C)/3  # centroid

# Plane distance from origin
distance = 1 / np.sqrt(1/a**2 + 1/b**2 + 1/c**2)

# Plot triangle, centroid, and plane
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for P, color, label in zip([A, B, C, D], ['red','green','blue','black'], ['A','B','C','Centroid D']):
    ax.scatter(*P, color=color, label=label)

# Triangle edges
for P1, P2 in [(A, B), (B, C), (C, A)]:
    ax.plot([P1[0], P2[0]], [P1[1], P2[1]], [P1[2], P2[2]], 'gray')

# Plane surface
xx, yy = np.meshgrid(np.linspace(0, a, 10), np.linspace(0, b, 10))
zz = c*(1 - xx/a - yy/b)
ax.plot_surface(xx, yy, zz, alpha=0.3, color='cyan')

ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_title(f'Triangle ABC, Centroid D, Plane\nDistance from origin = {distance:.2f}')
ax.legend()
plt.savefig('triangle_centroid_plane_distance.png')
plt.show()
