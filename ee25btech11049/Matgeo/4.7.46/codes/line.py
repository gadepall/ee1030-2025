import ctypes
import numpy as np
import matplotlib.pyplot as plt
from libs.funcs import line_dir_pt
from libs.params import omat
import os

# --- 1. Load the C Shared Library ---
try:
    # Construct the full path to the library file
    lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'line.so')
    line_lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error loading shared library: {e}")
    print("Please compile the C code first using 'make'.")
    exit()

# --- 2. Define the C Function Signature ---
# Specify the argument types and return type for the C function
calculate_line_normals = line_lib.calculate_line_normals
calculate_line_normals.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]
calculate_line_normals.restype = ctypes.c_int

# --- 3. Prepare Inputs and Outputs for the C Function ---
# Given point and distance
P_coords = (1.0, 0.0)
d = np.sqrt(3) / 2

# Create C-compatible double types for the outputs
a1, b1 = ctypes.c_double(), ctypes.c_double()
a2, b2 = ctypes.c_double(), ctypes.c_double()

# --- 4. Call the C Function ---
result = calculate_line_normals(
    P_coords[0], P_coords[1], d,
    ctypes.byref(a1), ctypes.byref(b1),
    ctypes.byref(a2), ctypes.byref(b2)
)

if result != 0:
    print("C function failed to find a solution.")
    exit()

# --- 5. Process the Results ---
# Convert the results from C types to NumPy arrays
n1 = np.array([a1.value, b1.value]).reshape(-1, 1)
n2 = np.array([a2.value, b2.value]).reshape(-1, 1)

# The point through which the lines pass
P = np.array([P_coords[0], P_coords[1]]).reshape(-1, 1)

# Calculate direction vectors by rotating the normal vectors
m1 = omat @ n1
m2 = omat @ n2

# Generate points for plotting the lines
line1 = line_dir_pt(m1, P, k1=-2, k2=2)
line2 = line_dir_pt(m2, P, k1=-2, k2=2)

# --- 6. Plotting ---
plt.figure(figsize=(8, 8))
plt.plot(line1[0, :], line1[1, :], label=r'$\sqrt{3}x + y - \sqrt{3} = 0$')
plt.plot(line2[0, :], line2[1, :], label=r'$\sqrt{3}x - y - \sqrt{3} = 0$')
plt.plot(P[0], P[1], 'o', color='red', markersize=8, label=f'Point P{P_coords}')

circle = plt.Circle((0, 0), d, color='gray', linestyle='--', fill=False, label=f'Distance d ≈ {d:.2f}')
plt.gca().add_artist(circle)

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title(r"Lines through (1, 0) at a distance of $\frac{\sqrt{3}}{2}$ from the Origin (C Backend)")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.xlim(-1.5, 2.5)
plt.ylim(-2, 2)
plt.show()

