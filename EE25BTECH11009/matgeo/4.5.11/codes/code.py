import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the shared library
lib = ctypes.CDLL("./func.so")

# Create arrays for results
A = (ctypes.c_int * 3)()
m = (ctypes.c_int * 3)()

# Call C functions
lib.get_point(A)
lib.get_direction(m)

# Convert to numpy
point_A = np.array([A[i] for i in range(3)])
direction_vector = np.array([m[i] for i in range(3)])

print("Point A:", point_A)
print("Direction vector:", direction_vector)

# --- Generate line points using parametric form ---
lam = np.linspace(-5, 5, 100)
x = point_A[0] + lam * direction_vector[0]
y = point_A[1] + lam * direction_vector[1]
z = point_A[2] + lam * direction_vector[2]

# --- Plotting ---
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, label="Required Line", color="blue")
ax.scatter(point_A[0], point_A[1], point_A[2],
           color="red", s=50, label="Point A (-2,4,-5)")
ax.quiver(point_A[0], point_A[1], point_A[2],
          direction_vector[0], direction_vector[1], direction_vector[2],
          color="green", label="Direction Vector", arrow_length_ratio=0.1)

ax.set_title("Line through A parallel to given line")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
ax.set_box_aspect([1,1,1])
plt.savefig("../figs/Figure_2.png")
plt.show()
