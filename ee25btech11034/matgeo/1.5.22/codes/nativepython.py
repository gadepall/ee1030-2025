import numpy as np
import matplotlib.pyplot as plt

def find_external_dividing_point(X, Y, k):

    V = (k * Y - X) / (k - 1)
    return V

def generate_line_points(point1, point2, num_points):
    t_values = np.linspace(-2, 3, num_points)
    direction = point2 - point1
    points = np.array([point1 + t * direction for t in t_values])
    return points

    # Define 2D unit vectors as column vectors
a = np.array([1, 0])
b = np.array([0, 1])

# Position vectors
X = 3*a + b
Y = a - 3*b

# Find external dividing point for ratio 2:1
V = find_external_dividing_point(X, Y, 2)

# Plot the vectors and line
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

ax.set_aspect('equal')

# Generate line points
line_points = generate_line_points(X, Y, 50)
ax.plot(line_points[:, 0], line_points[:, 1], 'k--', alpha=0.7, linewidth=1)
# Plot origin
ax.scatter([0], [0], color='black', s=20, marker='o', zorder=5)

# Plot points
ax.scatter(*X, color='red', s=20, marker='o', label = f"X ({int(X[0])}, {int(X[1])})", zorder=5)
ax.scatter(*Y, color='blue', s=20, marker='o', label = f"Y ({int(Y[0])}, {int(Y[1])})", zorder=5)
ax.scatter(*V, color='green', s=20, marker='^', label = f"V ({int(V[0])}, {int(V[1])})", zorder=5)

# Draw vectors from origin
ax.arrow(0, 0, X[0], X[1], head_width=0.2, head_length=0.2, fc='red', ec='red', alpha=0.7, width=0.03)
ax.arrow(0, 0, Y[0], Y[1], head_width=0.2, head_length=0.2, fc='blue', ec='blue', alpha=0.7, width=0.03)
ax.arrow(0, 0, V[0], V[1], head_width=0.2, head_length=0.2, fc='green', ec='green', alpha=0.8, width=0.04)

ax.grid(True, alpha=1)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
ax.set_title('External Division')

plt.tight_layout()
plt.show()
plt.savefig("fig.png")
