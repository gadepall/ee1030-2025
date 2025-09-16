import matplotlib.pyplot as plt
import numpy as np

# Define vectors
a = np.array([1, 0, 0])
b = np.array([0.5, np.sqrt(3)/2, 0])  # 60° rotated in xy-plane

# Compute u = a - (a·b)b
u = a - np.dot(a, b) * b

# Compute v = a × b
v = np.cross(a, b)

print("a =", a)
print("b =", b)
print("u =", u)
print("v =", v)

# ================== 3D Plot ==================
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

def draw_vec(ax, vec, color, label):
    ax.quiver(0, 0, 0, vec[0], vec[1], vec[2],
              color=color, arrow_length_ratio=0.1, linewidth=2)
    ax.text(vec[0]*1.1, vec[1]*1.1, vec[2]*1.1,
            label, color=color, fontsize=12)

# Draw vectors
draw_vec(ax, a, "blue", r"$\vec{a}$")
draw_vec(ax, b, "green", r"$\vec{b}$")
draw_vec(ax, u, "red", r"$\vec{u}$")
draw_vec(ax, v, "purple", r"$\vec{v}$")

# Set limits
ax.set_xlim([-1, 1.5])
ax.set_ylim([-1, 1.5])
ax.set_zlim([-1, 1.5])

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Vectors a, b, u, v", fontsize=14)

plt.tight_layout()

# Save figure
plt.savefig("vector_plot_3D.png", dpi=300)
plt.show()

