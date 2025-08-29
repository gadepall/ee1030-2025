
import numpy as np
import matplotlib.pyplot as plt

# Read vector data from file
with open('vector.dat', 'r') as file:
    lines = file.readlines()

# Extract coordinates from the file
line1 = lines[0]
P_start = line1.split("P(")[1].split(")")[0]
Q_end = line1.split("Q(")[1].split(")")[0]

P = np.array(list(map(int, P_start.split(','))))
Q = np.array(list(map(int, Q_end.split(','))))
PQ = Q - P  # Vector from P to Q

# Set up the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot origin
ax.scatter(0, 0, 0, color='black', label='Origin')

# Plot points
ax.scatter(*P, color='blue', label='Point P')
ax.scatter(*Q, color='red', label='Point Q')

# Plot vector PQ (arrow from P to Q)
ax.quiver(*P, *PQ, color='green', arrow_length_ratio=0.1, label='Vector PQ')

# Annotate points
ax.text(*P, '  P', color='blue')
ax.text(*Q, '  Q', color='red')

# Set limits
max_range = np.max(np.abs([P, Q])) + 1
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])

# Labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Vector Visualization')
ax.legend()

# Save the figure as an image (e.g., PNG)
plt.savefig('vector_plot.png', dpi=300)  # Change filename/format if needed

print("Plot saved as vector_plot.png")

