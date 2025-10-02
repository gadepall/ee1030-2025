import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# --- Setup and C Library Call ---

# To compile the C code into the required shared library, run the following command in your terminal:
# gcc -fPIC -shared -o circle_solver.so circle_solver.c -lm

# Define the folder to save figures
figs_folder = "figs"
if not os.path.exists(figs_folder):
    os.makedirs(figs_folder)

# Load the compiled C shared object
lib = ctypes.CDLL("./10.7.90.so")

# Define the C function signature
lib.find_circle_properties.argtypes = [ctypes.POINTER(ctypes.c_double * 2), ctypes.POINTER(ctypes.c_double)]
lib.find_circle_properties.restype = None

# Create variables to store the results from the C function
center_res = (ctypes.c_double * 2)()
radius_res = ctypes.c_double()

# Call the C function to populate the variables
lib.find_circle_properties(center_res, ctypes.byref(radius_res))

# Extract the results into Python variables
C = np.array([center_res[0], center_res[1]])
r = radius_res.value
print(f"Circle Center C: ({C[0]}, {C[1]})")
print(f"Circle Radius r: {r:.4f}")

# --- Geometric Points and Lines ---

# Origin
O = np.array([0, 0])
# Point of Tangency P (on y=x, at distance 4*sqrt(2) from O, and corresponding to the correct center)
P = np.array([-4, -4]) 
# Interior Point
Q = np.array([-10, 2])
# Midpoint of the chord on x+y=0
M = np.array([-5, 5])
# Chord endpoints on x+y=0
chord_p1 = np.array([-2, 2])
chord_p2 = np.array([-8, 8])

# --- Plotting ---

fig, ax = plt.subplots(figsize=(10, 10))

# Plot the circle
circle_patch = Circle(C, r, color='cyan', alpha=0.3, label=f"$(x+9)^2+(y-1)^2=50$")
ax.add_patch(circle_patch)
ax.plot(C[0], C[1], 'o', color='black') # Mark center
ax.text(C[0] + 0.3, C[1] + 0.3, f'C({C[0]:.0f}, {C[1]:.0f})', color='black')

# Plot the tangent line y=x
x_line = np.linspace(-15, 5, 100)
ax.plot(x_line, x_line, 'r--', label='Tangent Line: $y=x$')

# Plot the chord line x+y=0
ax.plot(x_line, -x_line, 'b--', label='Chord Line: $x+y=0$')

# Plot the actual chord segment
ax.plot([chord_p1[0], chord_p2[0]], [chord_p1[1], chord_p2[1]], 'b', linewidth=3, label='Chord (length $6\\sqrt{2}$)')

# Plot all relevant points
ax.plot(P[0], P[1], 'o', color='red')
ax.text(P[0] + 0.3, P[1] - 0.8, f'P({P[0]:.0f}, {P[1]:.0f})', color='red')
ax.plot(Q[0], Q[1], 'o', color='purple')
ax.text(Q[0] + 0.3, Q[1] + 0.3, f'Q({Q[0]:.0f}, {Q[1]:.0f})', color='purple')
ax.plot(O[0], O[1], 'o', color='green')
ax.text(O[0] + 0.3, O[1] - 0.8, 'Origin O', color='green')
ax.plot(M[0], M[1], 'x', color='blue')
ax.text(M[0] + 0.3, M[1] + 0.3, 'Chord Midpoint M', color='blue')


# --- Formatting ---

ax.set_aspect('equal')
ax.grid(True, linestyle=':')
ax.set_xlim(-18, 6)
ax.set_ylim(-12, 12)
ax.set_title("Geometric Construction of the Circle")
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.legend()

# Save the figure
fig_path = os.path.join(figs_folder, "Figure_1.png")
plt.savefig(fig_path)
print(f"Plot saved to {fig_path}")

plt.show()


