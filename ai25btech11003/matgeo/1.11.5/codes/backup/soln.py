import numpy as np
import matplotlib.pyplot as plt

# Define vectors
a = np.array([1, 1, 1])
b = np.array([2, 4, -5])
lambda_val = 1
c = np.array([lambda_val, 2, 3])

# b + c and its unit vector
bc = b + c
bc_unit = bc / np.linalg.norm(bc)

# Set up 3D plot
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-1, 7])
ax.set_ylim([-1, 7])
ax.set_zlim([-6, 4])

# Origin
origin = np.zeros(3)

def plot_vec(ax, v, color, label):
    ax.quiver(*origin, *v, color=color, arrow_length_ratio=0.1, linewidth=2)
    ax.text(*(v*1.12), label, color=color, fontsize=13)

plot_vec(ax, a, 'blue', 'a')
plot_vec(ax, b, 'orange', 'b')
plot_vec(ax, c, 'green', 'c')
plot_vec(ax, bc_unit, 'red', '(b+c)/|b+c|')

# Labels and style
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vectors a, b, c and unit vector along (b+c)')
plt.tight_layout()

# Save the figure
plt.savefig('fig1.png')
plt.close()

