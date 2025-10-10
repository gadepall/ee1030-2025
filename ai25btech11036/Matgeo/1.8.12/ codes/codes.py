import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Triangle vertices
vertices = np.array([[0, 4], [0, 0], [3, 0]])
labels = ['A(0,4)', 'B(0,0)', 'C(3,0)']

# Calculate side lengths
ab = np.linalg.norm(vertices[0] - vertices[1])  # A to B
bc = np.linalg.norm(vertices[1] - vertices[2])  # B to C
ca = np.linalg.norm(vertices[2] - vertices[0])  # C to A
perimeter = ab + bc + ca

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal')

# Draw the triangle
triangle = patches.Polygon(vertices, closed=True, fill=True, 
                          edgecolor='blue', facecolor='lightblue', alpha=0.7, linewidth=2)
ax.add_patch(triangle)

# Plot vertices and add labels
for i, (vertex, label) in enumerate(zip(vertices, labels)):
    ax.plot(vertex[0], vertex[1], 'ro', markersize=8)
    ax.text(vertex[0] + 0.1, vertex[1] + 0.1, label, fontsize=12, fontweight='bold')

# Add side length labels
ax.text((vertices[0][0] + vertices[1][0])/2, (vertices[0][1] + vertices[1][1])/2 - 0.2, 
        f'AB = {ab:.1f}', fontsize=11, ha='center', color='darkred', fontweight='bold')
ax.text((vertices[1][0] + vertices[2][0])/2 + 0.1, (vertices[1][1] + vertices[2][1])/2, 
        f'BC = {bc:.1f}', fontsize=11, va='center', color='darkred', fontweight='bold')
ax.text((vertices[2][0] + vertices[0][0])/2 - 0.2, (vertices[2][1] + vertices[0][1])/2, 
        f'CA = {ca:.1f}', fontsize=11, ha='center', va='center', color='darkred', fontweight='bold')

# Set plot limits and labels
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 5)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.set_title(f'Triangle with Perimeter = {ab:.1f} + {bc:.1f} + {ca:.1f} = {perimeter:.1f}', 
             fontsize=14, fontweight='bold')

# Add grid
ax.grid(True, linestyle='--', alpha=0.7)

# Add coordinate axes
ax.axhline(y=0, color='k', linewidth=1)
ax.axvline(x=0, color='k', linewidth=1)

# Add some additional points on Y-axis as mentioned in the problem
y_points = ['D', 'E', 'F', 'G', 'H']
for i, point in enumerate(y_points, 1):
    ax.plot(0, i, 's', color='purple', markersize=8)
    ax.text(0.2, i, point, fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()



