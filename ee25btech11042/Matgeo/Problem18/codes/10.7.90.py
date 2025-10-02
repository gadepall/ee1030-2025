import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def find_circle_properties():
    """
    Solves for the circle's center and radius based on the problem's geometric constraints.
    This function replicates the logic from the C code directly in Python.
    """
    # Possible points of tangency (P) where OP = 4*sqrt(2) on y=x
    P1 = np.array([4, 4])
    P2 = np.array([-4, -4])
    
    # Interior point Q
    Q = np.array([-10, 2])
    
    # Four potential centers are calculated based on two cases for P
    # Case 1: P = (4, 4), locus of centers is h+k=8
    # r^2 = 50, (h-4)^2 + (k-4)^2 = 50  => centers (9,-1) and (-1,9)
    # Case 2: P = (-4, -4), locus of centers is h+k=-8
    # r^2 = 50, (h+4)^2 + (k+4)^2 = 50 => centers (1,-9) and (-9,1)
    
    possible_centers = [
        np.array([9, -1]),
        np.array([-1, 9]),
        np.array([1, -9]),
        np.array([-9, 1])
    ]
    
    r_squared = 50.0
    correct_center = None
    
    # Check which center satisfies the interior point condition
    for center in possible_centers:
        # Calculate squared distance from Q to the potential center
        dist_sq = np.sum((Q - center)**2)
        if dist_sq < r_squared:
            correct_center = center
            break
            
    if correct_center is not None:
        return correct_center, np.sqrt(r_squared)
    else:
        # This case should not be reached if logic is correct
        return np.array([0, 0]), 0

# --- Setup and Python Calculation ---

# Define the folder to save figures
figs_folder = "figs"
if not os.path.exists(figs_folder):
    os.makedirs(figs_folder)

# Get circle properties from our Python function
C, r = find_circle_properties()
print(f"Circle Center C: ({C[0]}, {C[1]})")
print(f"Circle Radius r: {r:.4f}")

# --- Geometric Points and Lines ---

# Origin
O = np.array([0, 0])
# Point of Tangency P (on y=x, corresponding to the correct center)
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
fig_path = os.path.join(figs_folder, "Figure_2.png")
plt.savefig(fig_path)
print(f"Plot saved to {fig_path}")

plt.show()


