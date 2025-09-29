import numpy as np
import matplotlib.pyplot as plt

# Define the points
A = np.array([0, 2*np.sqrt(5)])
B = np.array([-2*np.sqrt(5), 0])

# Compute distance
dx = B[0] - A[0]
dy = B[1] - A[1]
distance = np.sqrt(dx**2 + dy**2)

print(f"Distance between {A} and {B} = {distance:.2f}")

# Plot line AB
plt.plot([A[0], B[0]], [A[1], B[1]], 'k-', label=f'Distance = {distance:.2f}')

# Plot points
plt.scatter([A[0], B[0]], [A[1], B[1]], c=['red', 'blue'])
labels = [f'A(0, 2√5)', f'B(-2√5, 0)']
coords = [A, B]

# Annotate points
for label, coord in zip(labels, coords):
    plt.annotate(label,
                 (coord[0], coord[1]),
                 textcoords="offset points",
                 xytext=(10, -10),
                 ha='center')

# Decorations
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.title("Distance between Two Points")

# Save the figure
plt.savefig("distance_plot.png", dpi=150)
plt.show()
