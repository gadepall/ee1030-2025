import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./libdistance.so")

# Define argument and return types
lib.plane_distance.argtypes = [ctypes.c_double, ctypes.c_double,
                               ctypes.c_double, ctypes.c_double,
                               ctypes.c_double, ctypes.c_double,
                               ctypes.c_double]
lib.plane_distance.restype = ctypes.c_double

# Plane coefficients
A, B, C, D = 2, -3, 4, -6
x0, y0, z0 = 0.0, 0.0, 0.0   # origin

# Call C function
dist = lib.plane_distance(A, B, C, D, x0, y0, z0)
print(f"Distance from origin = {dist:.4f}")

# ---------- PLOT ----------
# Generate grid for plane
xx, yy = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))
zz = (-A*xx - B*yy - D) / C

# Normal vector
normal = np.array([A, B, C])
normal = normal / np.linalg.norm(normal)

# Closest point on plane to origin = -D * (n / |n|)
closest_point = -D * normal / (A*normal[0] + B*normal[1] + C*normal[2])

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plane surface
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Origin
ax.scatter([0], [0], [0], color='red', s=50, label="Origin")

# Closest point
ax.scatter([closest_point[0]], [closest_point[1]], [closest_point[2]],
           color='blue', s=50, label="Closest Point")

# Distance line
ax.plot([0, closest_point[0]],
        [0, closest_point[1]],
        [0, closest_point[2]], color='black', linewidth=2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f"Distance = {dist:.4f}")

ax.legend()
plt.show()