import numpy as np
import matplotlib.pyplot as plt

# --- Step 1: Define the point and calculate the distance ---

# Define the coordinates of point P
P = np.array([2.0, 3.0])

# The distance of a point (x, y) from the x-axis is the absolute value of its y-coordinate.
distance = abs(P[1])

print(f"Coordinates of Point P: ({P[0]}, {P[1]})")
print(f"Distance from x-axis (calculated purely in Python): {distance:.4f}")


# --- Step 2: Plot the results ---

# The projection of P onto the x-axis is Q(x, 0)
Q = np.array([P[0], 0.0])

# Create a figure and axis object for the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle=':', alpha=0.7)

# Plot the dashed line representing the distance from P to its projection Q
ax.plot([P[0], Q[0]], [P[1], Q[1]], 'g--', label=f'Distance = {distance:.2f}')

# Plot and label Point P
ax.plot(P[0], P[1], 'o', markersize=12, color='red', label=f'Point P({P[0]}, {P[1]})')
ax.text(P[0] + 0.1, P[1] + 0.1, 'P', fontsize=14, fontweight='bold', color='red')

# Plot and label Point Q
ax.plot(Q[0], Q[1], 'o', markersize=8, color='blue', label=f'Projection Q({Q[0]}, {Q[1]})')
ax.text(Q[0] + 0.1, Q[1] + 0.1, 'Q', fontsize=14, fontweight='bold', color='blue')

# --- Step 3: Finalize the plot ---

# Draw the x and y axes for better visualization
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)

# Set the viewing limits of the plot
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)

# Add titles and labels
ax.set_title('Distance of Point P from the x-axis', fontsize=16)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.legend(loc="upper left")

# Save the plot to a file
plt.savefig('python_only_plot.png')

# Display the plot
plt.show()
