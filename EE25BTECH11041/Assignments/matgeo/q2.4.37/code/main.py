import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C shared object
lib = ctypes.CDLL("./main.so")

# Define argument and return types
lib.perpendicular_vectors.argtypes = [
    ctypes.POINTER(ctypes.c_double), # a
    ctypes.POINTER(ctypes.c_double), # b
    ctypes.c_double,                 # magnitude
    ctypes.POINTER(ctypes.c_double), # v1
    ctypes.POINTER(ctypes.c_double)  # v2
]
lib.perpendicular_vectors.restype = None

# Given vectors
a = np.array([2.0, -1.0, 2.0], dtype=np.double)
b = np.array([4.0, -1.0, 3.0], dtype=np.double)
magnitude = 6.0

# Prepare outputs
v1 = np.zeros(3, dtype=np.double)
v2 = np.zeros(3, dtype=np.double)

# Call C function
lib.perpendicular_vectors(
    a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    b.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    magnitude,
    v1.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    v2.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)

print(f"Vector a: {a}")
print(f"Vector b: {b}")
print(f"First perpendicular vector v1 (|v1|={np.linalg.norm(v1):.2f}): {v1}")
print(f"Second perpendicular vector v2 (|v2|={np.linalg.norm(v2):.2f}): {v2}")

# --- Plotting ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
origin = [0, 0, 0]

ax.plot([0,a[0]], [0,a[1]], [0,a[2]], color='r', label='A')
ax.plot([0,b[0]], [0,b[1]], [0,b[2]], color='b', label='B')
ax.plot([0,v1[0]], [0,v1[1]], [0,v1[2]], color='g', label='C1')
ax.plot([0,v2[0]], [0,v2[1]], [0,v2[2]], color='m', label='C2')

ax.text(a[0], a[1], a[2], 'A', color='r')
ax.text(b[0], b[1], b[2], 'B', color='b')
ax.text(v1[0], v1[1], v1[2], 'C1', color='g')
ax.text(v2[0], v2[1], v2[2], 'C2', color='m')

max_val = np.max(np.abs(np.vstack((a, b, v1, v2)))) * 1.2
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vectors and Perpendiculars')
ax.legend()
ax.grid(True)
ax.set_box_aspect([1,1,1])

plt.savefig('vector_plot.png')

plt.show()
