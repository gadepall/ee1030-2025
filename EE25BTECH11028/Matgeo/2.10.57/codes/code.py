import numpy as np
import matplotlib.pyplot as plt

# Define base vectors for parallelism
a = np.array([1.0, 0.0, 0.0])                     # a along x-axis
b = np.array([0.5, np.sqrt(3)/2, 0.0])            # b at 60° in xy-plane
c = b.copy()                                      # c || b
d = a.copy()                                      # d || a

# Small offsets so the arrows don't overlap visually
offset_c = np.array([0.0, 0.0, 0.05])  # shift c slightly up in z
offset_d = np.array([0.0, 0.0, -0.05]) # shift d slightly down in z

# Compute values
val = np.dot(np.cross(a, b), np.cross(c, d))
dot_ac = np.dot(a, c)

# Plot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

origin = np.zeros(3)

# Assign distinct colors for clarity
vectors = {
    'a': (origin, a, 'r'),
    'd': (offset_d, d, 'b'),   # Blue
    'b': (origin, b, 'g'),
    'c': (offset_c, c, 'm')    # Magenta
}

for name, (start, vec, col) in vectors.items():
    ax.quiver(start[0], start[1], start[2],
              vec[0], vec[1], vec[2],
              length=1.0, linewidth=3, arrow_length_ratio=0.12,
              color=col, label=name)
    ax.text(start[0]+vec[0]*1.05, start[1]+vec[1]*1.05, start[2]+vec[2]*1.05,
            name, fontsize=12)

# Add legend in top-right corner
ax.legend(loc='upper right')

ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.set_zlim(-0.5, 0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title(f"(a×b)·(c×d) = {val:.6f},  a·c = {dot_ac:.6f}")

plt.tight_layout()
plt.show()