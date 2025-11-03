import numpy as np
import matplotlib.pyplot as plt

# Define the x-axis range for plotting
x = np.linspace(-4, 2, 500)

# --- Equations of the Triangle Sides ---
# L1: x + y = 1  => y = 1 - x
y_l1 = 1 - x
# L2: 2x + 3y = 6 => y = (6 - 2x) / 3
y_l2 = (6 - 2*x) / 3
# L3: 4x - y = -4 => y = 4x + 4
y_l3 = 4*x + 4

# --- Calculated Vertices of the Triangle ---
A = np.array([-3, 4])        # Intersection of L1 and L2
B = np.array([-3/7, 16/7])   # Intersection of L2 and L3
C = np.array([-3/5, 8/5])    # Intersection of L3 and L1

# --- Equations of the Altitudes ---
# Altitude from A, perpendicular to L3. Its equation is x + 4y = 13.
y_alt_A = (13 - x) / 4
# Altitude from C, perpendicular to L2. Its equation is 3x - 2y = -5.
y_alt_C = (3*x + 5) / 2

# --- Calculated Orthocentre (Intersection of Altitudes) ---
H = np.array([3/7, 22/7])

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the sides of the triangle
ax.plot(x, y_l1, 'b-', label='L1: $x + y = 1$')
ax.plot(x, y_l2, 'g-', label='L2: $2x + 3y = 6$')
ax.plot(x, y_l3, 'm-', label='L3: $4x - y = -4$')

# Plot the altitudes (dashed lines)
ax.plot(x, y_alt_A, 'r--', alpha=0.7, label='Altitude from A')
ax.plot(x, y_alt_C, 'c--', alpha=0.7, label='Altitude from C')

# Plot the vertices
ax.plot(A[0], A[1], 'ko', markersize=8)
ax.plot(B[0], B[1], 'ko', markersize=8)
ax.plot(C[0], C[1], 'ko', markersize=8)

# --- Add coordinate labels to vertices ---
vertices = {'A': A, 'B': B, 'C': C}
for name, pos in vertices.items():
    label = f'{name} ({pos[0]:.2f}, {pos[1]:.2f})'
    ax.text(pos[0] + 0.1, pos[1] + 0.1, label, fontsize=12, va='bottom', ha='left')

# Plot the orthocentre as a red point
ax.plot(H[0], H[1], 'ro', markersize=12, label=f'Orthocentre H ({H[0]:.2f}, {H[1]:.2f})')

# --- Add coordinate label to the orthocentre ---
orthocentre_label = f'H ({H[0]:.2f}, {H[1]:.2f})'
ax.text(H[0] + 0.1, H[1] - 0.1, orthocentre_label, fontsize=12, va='top', color='red')

# --- Formatting the Plot ---
ax.set_title('Orthocentre of a Triangle', fontsize=18)
ax.set_xlabel('x-axis', fontsize=12)
ax.set_ylabel('y-axis', fontsize=12)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Set the aspect ratio to 'equal'
ax.set_aspect('equal', adjustable='box')

# Set plot limits to focus on the relevant area
ax.set_xlim(-4, 2)
ax.set_ylim(-1, 5)

ax.legend(loc='upper right')
plt.show()
