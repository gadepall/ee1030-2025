import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

# --- Step 1: Compile the C code (if not already done) ---
# This Python script assumes 'vector_ops.so' or 'vector_ops.dll' exists.
# To create it, run this command in your terminal first:
# gcc -shared -o vector_ops.so -fPIC vector_ops.c

# --- Step 2: Load the compiled C library ---
lib_name = 'vector_ops.so' if os.name != 'nt' else 'vector_ops.dll'
try:
    c_lib = ctypes.CDLL(os.path.abspath(lib_name))
except OSError:
    print(f"Error: '{lib_name}' not found.")
    print("Please compile the C code first by running this command in your terminal:")
    print("gcc -shared -o vector_ops.so -fPIC vector_ops.c")
    exit()

# Define the argument and return types for the C function
c_lib.check_perpendicularity.argtypes = [ctypes.c_float] * 6
c_lib.check_perpendicularity.restype = ctypes.c_float

# --- Step 3: Define vectors and call C function ---
a = np.array([5, -1, -3], dtype=np.float32)
b = np.array([1, 3, -5], dtype=np.float32)
p = a + b
q = a - b

# Call the C function to get the dot product
dot_product = c_lib.check_perpendicularity(*a, *b)
print(f"Dot product calculated by C code: {dot_product}")
if abs(dot_product) < 1e-6:
    print("✅ The vectors are perpendicular.")
else:
    print("❌ The vectors are NOT perpendicular.")

# --- Step 4: Generate the 3D plot ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# A dictionary of vectors to plot with their properties
vectors = {
    '$\\vec{a}$': (a, 'green'),
    '$\\vec{b}$': (b, 'orange'),
    '$\\vec{a}+\\vec{b}$': (p, 'blue'),
    '$\\vec{a}-\\vec{b}$': (q, 'red')
}

origin = [0, 0, 0]

for name, (vec, color) in vectors.items():
    # Draw the vector arrow
    ax.quiver(*origin, *vec, color=color, arrow_length_ratio=0.1, label=name)
    # Mark the endpoint
    ax.scatter(*vec, color=color, s=50)
    # Label the endpoint coordinate
    ax.text(vec[0], vec[1], vec[2], f'({vec[0]}, {vec[1]}, {vec[2]})', color='black')

# Plotting settings
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Plot of Vectors and Endpoints')
ax.legend()
ax.grid(True)
# Set a fixed view for consistency
ax.view_init(elev=20, azim=25)
plt.show()