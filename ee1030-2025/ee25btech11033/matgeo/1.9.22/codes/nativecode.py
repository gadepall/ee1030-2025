import numpy as np
import matplotlib.pyplot as plt

# Given point from the problem
P = np.array([2, -3]).reshape(-1, 1)

# Points for Q found in the solution
# The problem states y can be 3 or -9 for the point Q(10, y)
Q1 = np.array([10, 3]).reshape(-1, 1)
Q2 = np.array([10, -9]).reshape(-1, 1)

# Plotting the lines from P to Q1 and P to Q2
# This is done by providing the x and y coordinates of the start and end points
plt.plot([P[0,0], Q1[0,0]], [P[1,0], Q1[1,0]], label='$PQ_1$')
plt.plot([P[0,0], Q2[0,0]], [P[1,0], Q2[1,0]], label='$PQ_2$')

# Combining all points into a single array for easy plotting and labeling
coords = np.block([[P, Q1, Q2]])
plt.scatter(coords[0, :], coords[1, :])

# Adding labels for each point
vert_labels = ['P', 'Q₁', 'Q₂']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({coords[0, i]:.0f}, {coords[1, i]:.0f})',
                 (coords[0, i], coords[1, i]),
                 textcoords="offset points",
                 xytext=(0, 10), # Offset the text slightly above the point
                 ha='center')

# --- Plot Formatting ---
# Set the axes to pass through the origin (0,0)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Add legend, grid, and ensure the scale is equal on both axes
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')
# Save the plot to a file
plt.savefig('../figs/fig.png')
# Display the plot
plt.show()
