import numpy as np
import matplotlib.pyplot as plt

def line_gen(A, B, num=100):
    """
    Generates points on a line segment between points A and B.
    A, B are 2x1 numpy arrays (column vectors).
    Returns 2 x num numpy array of points.
    """
    lam = np.linspace(0, 1, num)
    return (1 - lam) * A + lam * B

# Points as column vectors
C = np.array([2, 0]).reshape(-1,1)   # Center
A = np.array([6, 0]).reshape(-1,1)   # One end of diameter
B = 2*C - A                         # Other end of diameter calculated

coords = np.block([[A,B,C]])

# Generate line points for diameter AB
AB = line_gen(A, B)

# Plot line AB
plt.plot(AB[0,:], AB[1,:], label='Diameter')

# Plot points
plt.scatter(coords[0,:], coords[1,:], color=['blue', 'green', 'red'])

# Annotations
plt.text(A[0], A[1]+0.1, 'A (6,0)', ha='center', color='blue')
plt.text(B[0], B[1]+0.1, 'B (-2,0)', ha='center', color='green')
plt.text(C[0], C[1]+0.1, 'C (2,0)', ha='center', color='red')

# Draw the circle centered at C with radius = half the distance AB
radius = np.linalg.norm(A - B) / 2

circle = plt.Circle((C[0], C[1]), radius, fill=False, color='orange', linestyle='--', linewidth=2, label='Circle')

# Add circle to plot
ax = plt.gca()
ax.add_patch(circle)

# Labels and grid
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid(True, linestyle='--')
plt.axis('equal')

# Save figure (adjust path as needed)
plt.savefig('circle_diameter_plot_with_circle.png', dpi=300)
plt.show() 
