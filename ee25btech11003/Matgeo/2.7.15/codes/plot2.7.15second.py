import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ==============================================================================
# PART 1: CALCULATE VOLUME USING CTYPES AND EXTERNAL C FUNCTION
# ==============================================================================

# --- Setup for ctypes ---
# CORRECT VECTORS - Please ensure these values are exact in your file.
vec_a = np.array([-3, 7, 5], dtype=np.double)
vec_b = np.array([-5, 7, -3], dtype=np.double)
vec_c = np.array([7, -5, -3], dtype=np.double)

# Determine the library file name based on the operating system
lib_name = 'libvolume.so' if os.name != 'nt' else 'volume.dll'
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), lib_name)

volume_from_c = -1.0 # Default value if library fails

try:
    # 1. Load the shared library
    c_lib = ctypes.CDLL(lib_path)

    # 2. Define the argument and return types for the C function
    volume_func = c_lib.volumeOfParallelepiped
    c_double_p = ctypes.POINTER(ctypes.c_double)
    volume_func.argtypes = [c_double_p, c_double_p, c_double_p]
    volume_func.restype = ctypes.c_double

    # 3. Get pointers to the NumPy array data buffers
    a_ptr = vec_a.ctypes.data_as(c_double_p)
    b_ptr = vec_b.ctypes.data_as(c_double_p)
    c_ptr = vec_c.ctypes.data_as(c_double_p)

    # 4. Call the C function and store the result
    volume_from_c = volume_func(a_ptr, b_ptr, c_ptr)

    # 5. Print the result from the C function
    print("-" * 50)
    print("Part 1: Volume Calculation via C function (ctypes)")
    print("-" * 50)
    print(f"The volume calculated via C is: {volume_from_c:.0f} cubic units")
    print("\nNow generating the 3D plot...")


except (OSError, AttributeError) as e:
    print(f"Error: Could not execute the C function from '{lib_name}'.")
    print("Please make sure you have compiled 'volume_calculator.c' first.")
    print("The plot will still be generated, but the C calculation was skipped.")
    print(f"Details: {e}")


# ==============================================================================
# PART 2: GENERATE THE CORRECT 3D PLOT
# ============================================================================== import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ==============================================================================
# PART 1: CALCULATE VOLUME USING CTYPES AND EXTERNAL C FUNCTION
# ==============================================================================

# --- Setup for ctypes ---
# CORRECT VECTORS - Please ensure these values are exact in your file.
vec_a = np.array([-3, 7, 5], dtype=np.double)
vec_b = np.array([-5, 7, -3], dtype=np.double)
vec_c = np.array([7, -5, -3], dtype=np.double)

# Determine the library file name based on the operating system
lib_name = 'libvolume.so' if os.name != 'nt' else 'volume.dll'
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), lib_name)

volume_from_c = -1.0 # Default value if library fails

try:
    # 1. Load the shared library
    c_lib = ctypes.CDLL(lib_path)

    # 2. Define the argument and return types for the C function
    volume_func = c_lib.volumeOfParallelepiped
    c_double_p = ctypes.POINTER(ctypes.c_double)
    volume_func.argtypes = [c_double_p, c_double_p, c_double_p]
    volume_func.restype = ctypes.c_double

    # 3. Get pointers to the NumPy array data buffers
    a_ptr = vec_a.ctypes.data_as(c_double_p)
    b_ptr = vec_b.ctypes.data_as(c_double_p)
    c_ptr = vec_c.ctypes.data_as(c_double_p)

    # 4. Call the C function and store the result
    volume_from_c = volume_func(a_ptr, b_ptr, c_ptr)

    # 5. Print the result from the C function
    print("-" * 50)
    print("Part 1: Volume Calculation via C function (ctypes)")
    print("-" * 50)
    print(f"The volume calculated via C is: {volume_from_c:.0f} cubic units")
    print("\nNow generating the 3D plot...")


except (OSError, AttributeError) as e:
    print(f"Error: Could not execute the C function from '{lib_name}'.")
    print("Please make sure you have compiled 'volume_calculator.c' first.")
    print("The plot will still be generated, but the C calculation was skipped.")
    print(f"Details: {e}")


# ==============================================================================
# PART 2: GENERATE THE CORRECT 3D PLOT
# ==============================================================================
# 1. Define the edge vectors starting from the origin
a = np.array([-3, 7, 5])
b = np.array([-5, 7, -3])
c = np.array([7, -5, -3])

# 2. Calculate the 8 vertices of the parallelepiped
v0 = np.array([0, 0, 0]) # Origin
v1 = a
v2 = b
v3 = c
v4 = a + b
v5 = a + c
v6 = b + c
v7 = a + b + c

# Combine all vertices into a single array for easy plotting
vertices = np.array([v0, v1, v2, v3, v4, v5, v6, v7])

# 3. Define the 6 faces of the parallelepiped by specifying the vertices for each face
faces = [
    [v0, v1, v4, v2],  # Bottom face
    [v0, v2, v6, v3],  # Back face
    [v0, v3, v5, v1],  # Left face
    [v7, v6, v2, v4],  # Front face (from b's side)
    [v7, v5, v1, v4],  # Right face (from a's side)
    [v7, v6, v3, v5]   # Top face
]

# 4. Set up the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 5. Add the faces to the plot
# Use a semi-transparent color to see through the shape
face_collection = Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='k', alpha=0.25)
ax.add_collection3d(face_collection)

# Plot the vertices as points
ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], s=50, c='r')

# Plot the initial vectors a, b, c from the origin
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='blue', arrow_length_ratio=0.1, label='a')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='green', arrow_length_ratio=0.1, label='b')
ax.quiver(0, 0, 0, c[0], c[1], c[2], color='purple', arrow_length_ratio=0.1, label='c')

# 6. Set plot labels and limits for better visualization
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Parallelepiped Defined by Vectors a, b, and c')

# Auto-scale axes to fit the data
all_points = np.vstack(faces).flatten()
ax.auto_scale_xyz(all_points, all_points, all_points)

ax.legend()
plt.grid(True)
plt.savefig("fig1.png")
plt.show()
