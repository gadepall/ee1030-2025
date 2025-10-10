import matplotlib.pyplot as plt
import numpy as np

# --- 1. Define Base Vectors ---
# We assign arbitrary coordinates to vectors 'a' and 'b' for visualization.
# To see a different layout, you can change these values.
a = np.array([1, 1])
b = np.array([-1, 2])

# --- 2. Define Position Vectors for P and Q ---
# As given in the problem statement.
P = 2*a + b
Q = a - 3*b

# --- 3. Calculate Position Vector for R ---
# Using the external division formula result we found: R = 3a + 5b
R = 3*a + 5*b

# --- 4. Verify P is the midpoint of RQ ---
# This calculation should result in the same coordinates as P.
midpoint_RQ = (R + Q) / 2
print(f"Coordinates of P: {P}")
print(f"Calculated midpoint of RQ: {midpoint_RQ}")
print(f"Is P the midpoint of RQ? {np.allclose(P, midpoint_RQ)}")


# --- 5. Create the Plot ---
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the line segment RQ
ax.plot([R[0], Q[0]], [R[1], Q[1]], 'k--', alpha=0.6, label='Line Segment RQ')

# Plot the points O, P, Q, R
ax.scatter(0, 0, c='black', s=100, zorder=5, label='Origin (O)')
ax.scatter(P[0], P[1], c='red', s=100, zorder=5, label=f'P = {P}')
ax.scatter(Q[0], Q[1], c='green', s=100, zorder=5, label=f'Q = {Q}')
ax.scatter(R[0], R[1], c='blue', s=100, zorder=5, label=f'R = {R}')


# Plot position vectors from the origin
ax.quiver(0, 0, P[0], P[1], angles='xy', scale_units='xy', scale=1, color='red', alpha=0.7)
ax.quiver(0, 0, Q[0], Q[1], angles='xy', scale_units='xy', scale=1, color='green', alpha=0.7)
ax.quiver(0, 0, R[0], R[1], angles='xy', scale_units='xy', scale=1, color='blue', alpha=0.7)


# --- 6. Add Labels and Formatting ---
# Add text labels for each point
ax.text(0, 0.5, 'O', fontsize=14)
ax.text(P[0] + 0.3, P[1], 'P', fontsize=14)
ax.text(Q[0] + 0.3, Q[1], 'Q', fontsize=14)
ax.text(R[0] + 0.3, R[1], 'R', fontsize=14)


# Set plot aesthetics
ax.set_title('Vector Visualization', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.axhline(0, color='grey', linewidth=0.5)
ax.axvline(0, color='grey', linewidth=0.5)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.set_aspect('equal', adjustable='box')
ax.legend()

plt.show()