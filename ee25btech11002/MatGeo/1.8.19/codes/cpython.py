# File: main_script.py

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import ctypes
import os

# --- Part 1: Mathematical Solution ---

# Define the known points
Q_coords = (0, 1)
P_coords = (5, -3)

# Since Q is equidistant from P and R(x, 6), we have distance(Q, P) = distance(Q, R).
# We can use the squared distance to avoid square roots:
# (5-0)^2 + (-3-1)^2 = (x-0)^2 + (6-1)^2
# 25 + 16 = x^2 + 25
# 41 = x^2 + 25
# x^2 = 16
# x = 4 or x = -4

# The two possible points for R are:
R1_coords = (4, 6)
R2_coords = (-4, 6)

# Calculate the required distances using numpy
P = np.array(P_coords)
Q = np.array(Q_coords)
R1 = np.array(R1_coords)
R2 = np.array(R2_coords)

dist_QR1 = LA.norm(R1 - Q)
dist_PR1 = LA.norm(R1 - P)
dist_PR2 = LA.norm(R2 - P)

print("--- Mathematical Solution ---")
print("The values of x for point R are 4 and -4.")
print(f"Distance QR (Radius): {dist_QR1:.2f}")
print(f"Distance PR1 (for x=4): {dist_PR1:.2f}")
print(f"Distance PR2 (for x=-4): {dist_PR2:.2f}\n")


# --- Part 2: C Code Integration using ctypes ---

print("--- C Function Verification ---")
try:
    # Load the shared library
    # The path must be correct relative to where you run the script.
    lib_path = ctypes.CDLL('./formula.so')
    geom_lib = ctypes.CDLL(lib_path)

    # Define the function signature (argument types) from the C code
    # The function takes three pointers to double arrays.
    c_double_p = ctypes.POINTER(ctypes.c_double)
    geom_lib.formula.argtypes = [c_double_p, c_double_p, c_double_p]
    geom_lib.formula.restype = None  # The C function returns void

    # Prepare the data for the C function
    # The C function expects arrays of doubles.
    P_c = (ctypes.c_double * 2)(*P)
    Q_c = (ctypes.c_double * 2)(*Q)
    R1_c = (ctypes.c_double * 2)(*R1)
    R2_c = (ctypes.c_double * 2)(*R2)

    # Call the C function for both solutions of R
    print("Calling C function with R1(4, 6):")
    geom_lib.formula(P_c, Q_c, R1_c)

    print("\nCalling C function with R2(-4, 6):")
    geom_lib.formula(P_c, Q_c, R2_c)

except (OSError, AttributeError) as e:
    print(f"Error loading or using the C library: {e}")
    print("Please ensure 'libgeometry.so' is in the same directory as this script.")


# --- Part 3: Plotting (using your provided code) ---

# Reshape points for plotting code compatibility
Q = Q.reshape(-1, 1)
P = P.reshape(-1, 1)
R1 = R1.reshape(-1, 1)
R2 = R2.reshape(-1, 1)

# The radius 'r' is the distance between Q and P.
r = LA.norm(P - Q)

# Helper function to generate circle points
def circ_gen(O, r):
    len = 100
    theta = np.linspace(0, 2*np.pi, len)
    x_circ = np.zeros((2, len))
    x_circ[0, :] = r * np.cos(theta)
    x_circ[1, :] = r * np.sin(theta)
    x_circ = (x_circ.T + O.T).T
    return x_circ

# Generate shapes for plotting
x_circ = circ_gen(Q, r)
x_line = np.linspace(-10, 10, 100)
y_line = np.full_like(x_line, 6)

# Plot the circle and the line
plt.figure(figsize=(10, 8))
plt.plot(x_circ[0, :], x_circ[1, :], label='Circle centered at Q')
plt.plot(x_line, y_line, label='Line y = 6')

# Plot lines connecting points
plt.plot([P[0,0], R1[0,0]], [P[1,0], R1[1,0]], 'g--', label='Line $PR_1$')
plt.plot([P[0,0], R2[0,0]], [P[1,0], R2[1,0]], 'g--', label='Line $PR_2$')
plt.plot([P[0,0], Q[0,0]], [P[1,0], Q[1,0]], 'k--', label='Line PQ')


# Plot and label the points
points = np.hstack((P, Q, R1, R2))
plt.scatter(points[0, :], points[1, :], s=50, color='red', zorder=5) # zorder to plot on top
point_labels = [f'P({P_coords[0]}, {P_coords[1]})',
                f'Q({Q_coords[0]}, {Q_coords[1]})',
                f'$R_1$({R1_coords[0]}, {R1_coords[1]})',
                f'$R_2$({R2_coords[0]}, {R2_coords[1]})']

for label, (x, y) in zip(point_labels, points.T):
    plt.annotate(
        label,
        (x, y),
        textcoords="offset points",
        xytext=(0, 10),
        ha='center'
    )

# Add a text box with the calculated distances
text_str = (f'Radius of circle (QR): {dist_QR1:.2f}\n'
            f'Distance $PR_1$: {dist_PR1:.2f}\n'
            f'Distance $PR_2$: {dist_PR2:.2f}')

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.text(-15, -5, text_str, fontsize=10, bbox=props)


# Plot formatting
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Visual Representation of Question 1.8.19")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.xlim(-11, 11)
plt.ylim(-6, 8)
plt.show()