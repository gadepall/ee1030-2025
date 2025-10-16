# Code by GVV Sharma
# September 12, 2023
# Revised September 28, 2025
# released under GNU GPL
# This script checks if the points (-a,-b), (0,0), (a,b), and (a^2, ab) are collinear.


import sys                                        
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# local imports
from libs.funcs import *

# if using termux
import subprocess
import shlex
# end if

# ------------------- MODIFICATION START -------------------

# For a tangible example, let's choose non-zero values for a and b
a = 2
b = 3

# Define the four points based on the problem statement
P1 = np.array([-a, -b]).reshape(-1, 1)
P2 = np.array([0, 0]).reshape(-1, 1)
P3 = np.array([a, b]).reshape(-1, 1)
P4 = np.array([a**2, a*b]).reshape(-1, 1)

# To check if all points are collinear, we can check the rank of a matrix
# formed by the vectors from the origin (P2) to the other points.
# The vectors are P1-P2 (i.e., P1), P3-P2 (i.e., P3), and P4-P2 (i.e., P4).
# If all these vectors lie on the same line, the rank of the matrix will be 1.

# Form a matrix with the vectors as columns
# Note: P2 is the origin, so it's not needed to form the vectors.
vec_matrix = np.block([P1, P3, P4])

# Calculate and print the rank
rank = LA.matrix_rank(vec_matrix)
print(f"The points are defined with a={a} and b={b}")
print(f"Matrix of vectors:\n{vec_matrix}")
print(f"Rank of the matrix: {rank}")

if rank == 1:
    print("Conclusion: A rank of 1 means the vectors are linearly dependent, so the points are COLLINEAR. ✅")
else:
    print("Conclusion: The points are NOT collinear. ❌")


# --- Plotting Section ---

# Generate a line passing through the points to visualize.
# We can use the two outer points, P1 and P4, to draw the line.
x_line = line_gen(P1, P4)

# Plot the generated line
plt.plot(x_line[0,:], x_line[1,:], label='Line of Collinearity')

# Combine all points into one array for plotting
all_coords = np.block([[P1, P2, P3, P4]])
plt.scatter(all_coords[0,:], all_coords[1,:])

# Label the coordinates
vert_labels = ['P1(-a, -b)', 'P2(0, 0)', 'P3(a, b)', 'P4(a², ab)']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({all_coords[0,i]:.0f}, {all_coords[1,i]:.0f})',
                 (all_coords[0,i], all_coords[1,i]), # Point to label
                 textcoords="offset points",   # How to position the text
                 xytext=(0,10),                # Distance from text to points (x,y)
                 ha='center')                  # Horizontal alignment


# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()
