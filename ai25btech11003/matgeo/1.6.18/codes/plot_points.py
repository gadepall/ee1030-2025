import matplotlib.pyplot as plt
import numpy as np

# Read the points from points.dat
points = []
with open("points.dat") as f:
    for line in f:
        x, y = map(float, line.split())
        points.append((x, y))

# Labels and colors for each point
labels = ['A(2,1)', 'B(0,5)', 'C(-1,2)']
colors = ['blue', 'orange', 'green']

plt.figure(figsize=(6, 6))

# Plot points and annotate
for (x, y), label, color in zip(points, labels, colors):
    plt.scatter(x, y, color=color, s=100, zorder=5)
    plt.text(x + 0.1, y + 0.1, label, fontsize=12, fontweight='bold')

# Draw dashed lines between B→A and C→A
# Assuming order in points.dat is A, B, C
A, B, C = points
plt.plot([B[0], A[0]], [B[1], A[1]], '--', color='gray', alpha=0.7, linewidth=1.5)
plt.plot([C[0], A[0]], [C[1], A[1]], '--', color='gray', alpha=0.7, linewidth=1.5)

# Grid, axes, and ticks
plt.grid(True, alpha=0.4, linestyle=':')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlim(-2, 4)
plt.ylim(0, 7)
plt.xticks(np.arange(-2, 5, 1))
plt.yticks(np.arange(0, 8, 1))

# Title only
plt.title('Points A, B, C', fontsize=14, fontweight='bold', pad=20)

# Remove axis labels
plt.xlabel('')
plt.ylabel('')

# Save the figure
plt.savefig('fig1.png', dpi=150, bbox_inches='tight')
plt.close()

