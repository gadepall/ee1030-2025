import ctypes
import platform
import os
import matplotlib.pyplot as plt
import numpy as np

# --- Part 1: C function integration using ctypes ---

# Define the line equation: 3x + 0y + 2 = 0
line_coeffs = {'a': 3.0, 'b': 0.0}

# Load the shared library based on the operating system
lib_name = 'vector_lib.so' if platform.system() != 'Windows' else 'vector_lib.dll'
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), lib_name)

try:
    vector_lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error loading shared library: {e}")
    print("Please ensure you have compiled the C code in Step 2.")
    exit()


# Define the function signature (argument types and return type)
# Corresponds to: void get_line_vectors(float a, float b, float* normal_vec, float* direction_vec)
get_line_vectors_c = vector_lib.get_line_vectors
get_line_vectors_c.restype = None
get_line_vectors_c.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float)
]

# Create C-compatible arrays to store the results
FloatArray2 = ctypes.c_float * 2
normal_c = FloatArray2()
direction_c = FloatArray2()

# Call the C function
get_line_vectors_c(
    ctypes.c_float(line_coeffs['a']),
    ctypes.c_float(line_coeffs['b']),
    normal_c,
    direction_c
)

# Convert the results from C arrays to NumPy arrays
normal_vector = np.array([normal_c[0], normal_c[1]])
direction_vector = np.array([direction_c[0], direction_c[1]])

print(f"Normal vector from C function: {normal_vector}")
print(f"Direction vector from C function: {direction_vector}")


# --- Part 2: Plotting code using the results from C ---

# Normalize the vectors for consistent plotting appearance
# This makes them unit vectors, so their length is 1.
norm_n = np.linalg.norm(normal_vector)
if norm_n > 0:
    normal_vector /= norm_n

norm_m = np.linalg.norm(direction_vector)
if norm_m > 0:
    direction_vector /= norm_m

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))

# Set axis limits and aspect ratio
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2, 2.5)
ax.set_aspect('equal', adjustable='box')

# Draw the grid and main axes
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.axhline(y=0, color='k', linewidth=0.8)
ax.axvline(x=0, color='k', linewidth=0.8)

# 1. The line x = -2/3
x_line = -2/3
ax.axvline(x=x_line, color='blue', linewidth=2, label='$3x+2=0$')

# 2. The point P on the line where vectors originate
p_coords = np.array([x_line, 0.5])
ax.plot(p_coords[0], p_coords[1], 'o', color='black', markersize=6)

# 3. The normal vector (using result from C function)
ax.quiver(p_coords[0], p_coords[1], normal_vector[0], normal_vector[1],
          angles='xy', scale_units='xy', scale=1, color='red', width=0.01)

# 4. The direction vector (using result from C function)
ax.quiver(p_coords[0], p_coords[1], direction_vector[0], direction_vector[1],
          angles='xy', scale_units='xy', scale=1, color='green', width=0.01)

# --- Add labels ---

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.text(-0.2, -0.2, '$O$', fontsize=12)

# Dynamically place vector labels based on their direction
label_offset = 1.2
ax.text(p_coords[0] + label_offset * normal_vector[0],
        p_coords[1] + label_offset * normal_vector[1],
        '$\\mathbf{n}$', fontsize=14, color='red', va='center', ha='center')

ax.text(p_coords[0] + label_offset * direction_vector[0],
        p_coords[1] + label_offset * direction_vector[1],
        '$\\mathbf{m}$', fontsize=14, color='green', va='center', ha='center')

# Add legend and title
ax.legend()
ax.set_title('Line $3x+2=0$ with Vectors Calculated from C Function')

# Save and show the figure
plt.savefig('line_and_vectors_from_c.png', bbox_inches='tight')
plt.show()
