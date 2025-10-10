# Code by GVV Sharma
# September 7, 2023
# Revised by Gemini to use separate files for parameters and functions.
# This script contains the main logic and plotting.

import numpy as np
import numpy.linalg as LA
import scipy.linalg as SA
import matplotlib.pyplot as plt

# Local imports from separate files
from libs.params import *
from libs.funcs import *

# ----------------- Main Script -------------------------------

# --- Define Triangle Vertices (as per the problem statement) ---
A = np.array([-2, 3])
B = np.array([8, 3])
C = np.array([6, 7])

# Perform the right-angle check using the imported function from funcs.py
is_right_angled_python(A, B, C)

# Create the vertex matrix G_v (vertices as columns for matrix operations)
G_v = np.array([A, B, C]).T

# --- Matrix Algebra Calculations ---

# Direction vector circulant matrix
C_m = SA.circulant([1, 0, -1]).T

# Direction vector Matrix (vectors representing sides B-A, C-B, A-C)
G_dir = G_v @ C_m

# Normal vector matrix (uses R_o imported from params.py)
G_n = R_o @ G_dir

# Find the line constants for the side equations n.T @ x = c
cmat = np.diag(G_n.T @ G_v).reshape(-1, 1)

t
# ----------------- Plotting -------------------------------

# Generate points for each side (uses line_gen from funcs.py)
line_AB = line_gen(A, B)
line_BC = line_gen(B, C)
line_CA = line_gen(C, A)

# Setup the plot
plt.figure(figsize=(10, 8))
plt.style.use('seaborn-v0_8-whitegrid')

# Plot the sides of the triangle
plt.plot(line_AB[0, :], line_AB[1, :], label='Side AB')
plt.plot(line_BC[0, :], line_BC[1, :], label='Side BC')
plt.plot(line_CA[0, :], line_CA[1, :], label='Side AC')

# Plot and label the vertices (uses label_pts from funcs.py)
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


