import ctypes
import os
import platform
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Step 1: Define a Python class that mirrors the C struct ---
class Vector3D(ctypes.Structure):
    """A ctypes structure to match the Vector3D struct in C."""
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# --- Step 2: Locate and load the compiled C shared library ---

# Determine the correct file extension for the shared library based on the OS
system = platform.system()
if system == "Windows":
    lib_extension = ".dll"
elif system == "Darwin": # macOS
    lib_extension = ".dylib"
else: # Linux and other POSIX
    lib_extension = ".so"

lib_name = "force" + lib_extension
lib_path = os.path.join(os.path.dirname(__file__), lib_name)

# Provide instructions and exit if the library is not found
try:
    c_lib = ctypes.CDLL(lib_path)
except OSError:
    print(f"Error: Could not load the shared library '{lib_name}'.")
    print("Please compile the C code into a shared library first.")
    print("\nOn Linux or macOS, use this command in your terminal:")
    print("gcc -shared -o work_done_calculator.so -fPIC work_done_calculator.c")
    print("\nOn Windows (with MinGW/GCC), use this command:")
    print("gcc -shared -o work_done_calculator.dll work_done_calculator.c")
    exit()

# --- Step 3: Define the C function's signature for ctypes ---

# Get a reference to the function from the loaded library
calculate_work_done_c = c_lib.calculate_work_done

# Specify the argument types (three pointers to Vector3D)
calculate_work_done_c.argtypes = [ctypes.POINTER(Vector3D), 
                                  ctypes.POINTER(Vector3D), 
                                  ctypes.POINTER(Vector3D)]

# Specify the return type (a double)
calculate_work_done_c.restype = ctypes.c_double


# --- Step 4: Prepare data and call the C function ---

# The problem data as tuples
force_P_data    = (2.0, -5.0, 6.0)
position_A_data = (6.0, 1.0, -3.0)
position_B_data = (4.0, -3.0, -2.0)

# Create Python instances of the Vector3D structure
force_P    = Vector3D(*force_P_data)
position_A = Vector3D(*position_A_data)
position_B = Vector3D(*position_B_data)

# Call the C function, passing the structures by reference
work_done = calculate_work_done_c(ctypes.byref(force_P), 
                                  ctypes.byref(position_A), 
                                  ctypes.byref(position_B))


# --- Step 5: Display the result ---

print("--- Calling C function from Python ---")
print(f"Force: {force_P_data}")
print(f"Position A: {position_A_data}")
print(f"Position B: {position_B_data}")
print("-" * 35)
print(f"Work Done (calculated by C library): {work_done} Joules")


# --- Step 6: 3D Visualization using Matplotlib ---

# Convert tuples to NumPy arrays for plotting and vector math
force_np = np.array(force_P_data)
pos_a_np = np.array(position_A_data)
pos_b_np = np.array(position_B_data)
displacement_np = pos_b_np - pos_a_np

# Create the plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting points A and B
ax.scatter(*pos_a_np, color='blue', s=100, label='Point A')
ax.scatter(*pos_b_np, color='red', s=100, label='Point B')

# Origin for position vectors
origin = [0, 0, 0]

# Position vectors from origin
ax.quiver(*origin, *pos_a_np, color='cyan', arrow_length_ratio=0.1, label='Position Vector A')
ax.quiver(*origin, *pos_b_np, color='magenta', arrow_length_ratio=0.1, label='Position Vector B')

# Displacement vector from A to B
ax.quiver(*pos_a_np, *displacement_np, color='green', arrow_length_ratio=0.1, label='Displacement Vector (d)')

# Force vector acting on the particle (shown at point A for context)
ax.quiver(*pos_a_np, *force_np, color='orange', arrow_length_ratio=0.1, label='Force Vector (P)')

# Setting plot labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Visualization of Force and Displacement')

# Setting axis limits
max_val = np.max(np.abs(np.concatenate(([0], pos_a_np, pos_b_np, pos_a_np + displacement_np, pos_a_np + force_np))))
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

ax.legend()
ax.grid(True)

# Show plot
plt.show()


