# Code by GVV Sharma
# September 12, 2023
# released under GNU GPL
# This script checks if the points (-a,-b), (0,0), (a,b), and (a^2, ab) are collinear.
# It now includes a check using a custom C function via ctypes.

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import subprocess
import shlex
import ctypes
import os

# local imports (assuming funcs.py is in the same directory)
from libs.funcs import *

# --- COMPILE AND LOAD C FUNCTION ---
# This block compiles line.c into a shared library and loads it.

c_file = "line.c"
lib_file = "line.so" if os.name != 'nt' else "line.dll"

# Compile C code into a shared library
# The -fPIC flag is needed for creating a shared library
compile_command = f"gcc -shared -o {lib_file} -fPIC {c_file}"
try:
    subprocess.run(shlex.split(compile_command), check=True)
    print(f"Successfully compiled {c_file} to {lib_file}\n")
except (subprocess.CalledProcessError, FileNotFoundError):
    print("Error: C compilation failed. Make sure gcc is installed and in your PATH.")
    exit()

# Load the shared library
try:
    c_lib = ctypes.CDLL(os.path.abspath(lib_file))
except OSError as e:
    print(f"Error loading shared library: {e}")
    exit()

# Define the C function's signature (argument types and return type)
check_collinearity_c = c_lib.check_collinearity
check_collinearity_c.argtypes = [ctypes.c_double] * 6  # six double arguments
check_collinearity_c.restype = ctypes.c_double         # returns a double

# --- PROBLEM SETUP ---

# For a tangible example, let's choose non-zero values for a and b
a = 2.0
b = 3.0

# Define the four points using numpy arrays
P1 = np.array([-a, -b]).reshape(-1, 1)
P2 = np.array([0.0, 0.0]).reshape(-1, 1)
P3 = np.array([a, b]).reshape(-1, 1)
P4 = np.array([a**2, a*b]).reshape(-1, 1)


# --- METHOD 1: MATRIX RANK COLLINEARITY CHECK (Original Method) ---
print("--- Method 1: NumPy Matrix Rank ---")
# Form a matrix with the vectors as columns.
vec_matrix = np.hstack([P1, P3, P4])
rank = LA.matrix_rank(vec_matrix)

print(f"Checking points with a={a}, b={b}")
print(f"Matrix of vectors (from origin to other points):\n{vec_matrix}")
print(f"Rank of the matrix: {rank}")

if rank == 1:
    print("Conclusion: A rank of 1 means the points are COLLINEAR. ✅")
else:
    print("Conclusion: The points are NOT collinear. ❌")

print("-" * 40)


# --- METHOD 2: C FUNCTION COLLINEARITY CHECK (New Method) ---
print("--- Method 2: Calling C function via ctypes ---")
# To check if 4 points are collinear, we can check 2 sets of 3 points.
# For example, are P1, P2, P3 collinear? And are P1, P2, P4 collinear?

# Check collinearity for points P1, P2, and P3
det1 = check_collinearity_c(
    P1[0,0], P1[1,0],  # P1(x, y)
    P2[0,0], P2[1,0],  # P2(x, y)
    P3[0,0], P3[1,0]   # P3(x, y)
)

# Check collinearity for points P1, P2, and P4
det2 = check_collinearity_c(
    P1[0,0], P1[1,0],  # P1(x, y)
    P2[0,0], P2[1,0],  # P2(x, y)
    P4[0,0], P4[1,0]   # P4(x, y)
)

print(f"Determinant for P1, P2, P3: {det1}")
print(f"Determinant for P1, P2, P4: {det2}")

# For floating point numbers, check if the determinant is very close to zero
if abs(det1) < 1e-9 and abs(det2) < 1e-9:
    print("\nConclusion: Both determinants are zero, so the points are COLLINEAR. ✅")
else:
    print("\nConclusion: At least one determinant is non-zero, so the points are NOT collinear. ❌")


# --- PLOTTING SECTION (No changes needed here) ---
print("\nGenerating plot...")
x_line = line_gen(P1, P4)
plt.plot(x_line[0,:], x_line[1,:], label='Line of Collinearity')
all_coords = np.hstack([P1, P2, P3, P4])
plt.scatter(all_coords[0,:], all_coords[1,:])
vert_labels = ['P1(-a, -b)', 'P2(0, 0)', 'P3(a, b)', 'P4(a², ab)']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({all_coords[0,i]:.1f}, {all_coords[1,i]:.1f})',
                 (all_coords[0,i], all_coords[1,i]),
                 textcoords="offset points", xytext=(0,10), ha='center')

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()

# Clean up the compiled library file
if os.path.exists(lib_file):
    os.remove(lib_file)
