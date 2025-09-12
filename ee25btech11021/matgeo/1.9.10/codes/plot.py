import numpy as np
import matplotlib.pyplot as plt

# Same points (from C originally)
A = np.array([0, 6])
B = np.array([0, -2])

# Distance using numpy
dist = np.linalg.norm(A - B)

# ---- Plotting ----
plt.scatter(A[0], A[1], color="red", label=f"A{tuple(A)}")
plt.scatter(B[0], B[1], color="blue", label=f"B{tuple(B)}")

# Draw line segment AB
plt.plot([A[0], B[0]], [A[1], B[1]], color="green", linestyle="--", label=f"Distance = {dist:.2f}")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Distance between A and B")
plt.legend()
plt.grid(True)
plt.axis("equal")

plt.savefig("points_plot.png")
plt.show()
import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./libpoints.so")

# Define function signature for get_points
lib.get_points.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.get_points.restype = None

# Use numpy array for points
points = np.zeros(4, dtype=np.int32)

# Get points from C
lib.get_points(points.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))

# Reshape into 2D points: A and B
A = points[:2]
B = points[2:]

# Distance using numpy
dist = np.linalg.norm(A - B)

# ---- Plotting ----
plt.scatter(A[0], A[1], color="red", label=f"A{tuple(A)}")
plt.scatter(B[0], B[1], color="blue", label=f"B{tuple(B)}")

# Draw line segment AB
plt.plot([A[0], B[0]], [A[1], B[1]], color="green", linestyle="--", label=f"Distance = {dist:.2f}")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Distance between A and B")
plt.legend()
plt.grid(True)
plt.axis("equal")

# Save and show figure
plt.savefig("points_plot.png", dpi=300)
plt.show()

print("✅ Figure saved as points_plot.png")

