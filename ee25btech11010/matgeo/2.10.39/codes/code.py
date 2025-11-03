import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # needed for 3D plotting

# --- Mirror the C struct ---
class Vec3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# --- Load the shared library ---
lib = ctypes.CDLL("./code.so")
lib.find_unit_vector_c.restype = Vec3  # C returns a Vec3 struct

# --- Call the C function ---
result = lib.find_unit_vector_c()
unit_vector = np.array([result.x, result.y, result.z])
print("Unit vector from C:", unit_vector)

# --- Plot the unit vector ---
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

# Draw axes
ax.quiver(0, 0, 0, unit_vector[0], unit_vector[1], unit_vector[2],
          color='blue', arrow_length_ratio=0.1, linewidth=2)

# Mark the tip of the vector
ax.scatter(unit_vector[0], unit_vector[1], unit_vector[2],
           color='red', s=50, label='Unit Vector')

# Label axes
ax.set_xlim([0,1]); ax.set_ylim([0,1]); ax.set_zlim([0,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Unit Vector from C Library')
ax.legend()

plt.tight_layout()
plt.show()
