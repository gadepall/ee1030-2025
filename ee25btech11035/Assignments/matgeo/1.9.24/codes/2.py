import matplotlib.pyplot as plt
import numpy as np

# Define the points
# Q(2, -5), R(-3, 6), k = 8, so P(2k, k) = P(16, 8)
Q = (2, -5)
R = (-3, 6)
k = 8
P = (2 * k, k)  # P(16, 8)

print(f"Point Q: {Q}")
print(f"Point R: {R}")
print(f"Point P: {P}")

# Create the plot
plt.figure(figsize=(12, 10))

# Plot the points
plt.scatter(Q[0], Q[1], color='red', s=150, label=f'Q{Q}', zorder=5, edgecolor='white', linewidth=2)
plt.scatter(R[0], R[1], color='blue', s=150, label=f'R{R}', zorder=5, edgecolor='white', linewidth=2)
plt.scatter(P[0], P[1], color='green', s=150, label=f'P{P}', zorder=5, edgecolor='white', linewidth=2)

# Connect points with dashed lines
plt.plot([Q[0], R[0]], [Q[1], R[1]], 'k--', alpha=0.7, linewidth=1.5, label='QR')
plt.plot([Q[0], P[0]], [Q[1], P[1]], 'k--', alpha=0.7, linewidth=1.5, label='QP')
plt.plot([R[0], P[0]], [R[1], P[1]], 'k--', alpha=0.7, linewidth=1.5, label='RP')

# Add point labels
plt.annotate('Q', Q, xytext=(8, 8), textcoords='offset points', 
             fontsize=14, fontweight='bold', color='red')
plt.annotate('R', R, xytext=(8, 8), textcoords='offset points', 
             fontsize=14, fontweight='bold', color='blue')
plt.annotate('P', P, xytext=(8, 8), textcoords='offset points', 
             fontsize=14, fontweight='bold', color='green')

# Customize the plot
plt.grid(True)
plt.axhline(y=0, color='black', linewidth=0.8)
plt.axvline(x=0, color='black', linewidth=0.8)

plt.xlabel('X-coordinate', fontsize=12)
plt.ylabel('Y-coordinate', fontsize=12)
plt.title('Points Q(2, -5), R(-3, 6), and P(16, 8) in 2D Space', fontsize=14, fontweight='bold')

# Set equal aspect ratio
plt.axis('equal')

# Add legend
plt.legend(fontsize=12, loc='upper left')

# Set appropriate axis limits to show all points clearly
all_x = [Q[0], R[0], P[0]]
all_y = [Q[1], R[1], P[1]]

x_range = max(all_x) - min(all_x)
y_range = max(all_y) - min(all_y)
margin = max(x_range, y_range) * 0.15

plt.xlim(min(all_x) - margin, max(all_x) + margin)
plt.ylim(min(all_y) - margin, max(all_y) + margin)

# Make the plot look professional
plt.tight_layout()

# Save the plot as 2.png
plt.savefig('2.png', dpi=300, bbox_inches='tight')

plt.show()
