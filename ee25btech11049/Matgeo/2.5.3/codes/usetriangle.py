# Code by GVV Sharma
# September 7, 2023
# Revised by Gemini
# This version integrates a C library to verify the right-angle property
# and uses fixed points as per the problem statement.

import sys
import os
import ctypes
import numpy as np
import numpy.linalg as LA
import scipy.linalg as SA
import matplotlib.pyplot as plt

# --- Helper functions (to make the script self-contained) ---

def line_gen(A, B, n=10):
    """Generates n points on a line segment between points A and B."""
    return np.array([np.linspace(A[0], B[0], n), np.linspace(A[1], B[1], n)])

def label_pts(points, labels):
    """Adds text labels to a plot for each point."""
    for i, label in enumerate(labels):
        plt.text(points[0, i] + 0.2, points[1, i] + 0.2, label, fontsize=12)

# --- C Library Integration ---

def check_triangle_with_c_lib(p1, p2, p3):
    """
    Loads the C shared library and calls the isRightAngled function.
    """
    try:
        # Determine library name based on OS
        lib_name = 'libtriangle.so' if sys.platform.startswith(('linux', 'darwin')) else 'triangle.dll'
        lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), lib_name)
        
        triangle_lib = ctypes.CDLL(lib_path)

        # Define the C function signature for type safety
        isRightAngled = triangle_lib.isRightAngled
        isRightAngled.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        isRightAngled.restype = ctypes.c_int

        # Call the C function
        result = isRightAngled(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])

        # Print the result
        print("-" * 50)
        print("--- C Library Verification ---")
        if result == 1:
            print(f"C function returned: 1")
            print(f"Conclusion: The points form a right-angled triangle.")
        else:
            print(f"C function returned: 0")
            print(f"Conclusion: The points DO NOT form a right-angled triangle.")
        print("-" * 50)

    except OSError as e:
        print(f"Error: Could not load the shared library '{lib_name}'.")
        print("Please compile 'triangle_checker.c' first.")
        print("  Linux/macOS: gcc -shared -o libtriangle.so -fPIC triangle_checker.c")
        print("  Windows:     gcc -shared -o triangle.dll triangle_checker.c")
        print(f"Details: {e}")
        # Exit if the library isn't found, as the check is crucial
        sys.exit(1)


# ----------------- Main Script -------------------------------

# --- Define Triangle Vertices (as per the problem statement) ---
A = np.array([-2, 3])
B = np.array([8, 3])
C = np.array([6, 7])

# Perform the check using the C library before proceeding
check_triangle_with_c_lib(A, B, C)

# Create the vertex matrix G_v (vertices as columns)
G_v = np.array([A, B, C]).T


# --- Matrix Algebra Calculations (from original script) ---

# Rotation matrix for normals
R_o = np.array([[0, -1], [1, 0]])

# Direction vector circulant matrix
C_m = SA.circulant([1, 0, -1]).T

# Direction vector Matrix (vectors representing sides B-A, C-B, A-C)
G_dir = G_v @ C_m

# Normal vector matrix
G_n = R_o @ G_dir

# Find the line constants for the side equations n.T @ x = c
cmat = np.diag(G_n.T @ G_v).reshape(-1, 1)
# print("Line Matrix [nx, ny, c]:\n", np.block([G_n.T, cmat]))

# Get lengths of the sides
side_lengths = np.linalg.norm(G_dir, axis=0)
a, b, c = side_lengths[1], side_lengths[2], side_lengths[0] # BC, AC, AB
# print(f"Side lengths squared: AB^2={c**2:.1f}, BC^2={a**2:.1f}, AC^2={b**2:.1f}")


# ----------------- Plotting -------------------------------

# Generate points for each side
line_AB = line_gen(A, B)
line_BC = line_gen(B, C)
line_CA = line_gen(C, A)

# Setup the plot
plt.figure(figsize=(10, 8))
plt.style.use('seaborn-v0_8-whitegrid')

# Plot the sides
plt.plot(line_AB[0, :], line_AB[1, :], label='Side AB')
plt.plot(line_BC[0, :], line_BC[1, :], label='Side BC')
plt.plot(line_CA[0, :], line_CA[1, :], label='Side AC')

# Plot and label the vertices
plt.plot(G_v[0, :], G_v[1, :], 'o', color='red', markersize=8)
vert_labels = [f'A({A[0]},{A[1]})', f'B({B[0]},{B[1]})', f'C({C[0]},{C[1]})']
label_pts(G_v, vert_labels)

# Set plot properties
plt.title('Triangle Analysis', fontsize=16)
plt.xlabel('$x$-axis', fontsize=12)
plt.ylabel('$y$-axis', fontsize=12)
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

