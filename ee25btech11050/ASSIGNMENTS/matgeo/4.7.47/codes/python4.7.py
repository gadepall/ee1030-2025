import numpy as np
import matplotlib.pyplot as plt

# Given point P and line y = 3x + 4
P = np.array([2.0, 3.0])

# Normal vector (from line 3x - y + 4 = 0) and direction vector
n = np.array([3.0, -1.0])  # normal vector
m = np.array([1.0, 3.0])   # direction vector, since m.T n = 0
c = -4.0                   # constant term (3x - y = -4)

# Construct linear system [m^T; n^T] Q = [m^T P; c]
A = np.array([[1.0, 3.0],
              [3.0, -1.0]])
b = np.array([np.dot(m, P), c])

# Solve for Q using numpy
Q = np.linalg.solve(A, b)
print(f"Foot of perpendicular Q = ({Q[0]:.3f}, {Q[1]:.3f})")

# Prepare line for plotting
x = np.linspace(-3, 4, 400)
y_line = 3*x + 4  # line: y = 3x + 4

# Plot setup (same style as before)
plt.figure(figsize=(7,6))
plt.plot(x, y_line, label='Line: y = 3x + 4', linewidth=2)

# Plot points P and Q
plt.scatter(P[0], P[1], color='blue', s=80, label='P (2,3)')
plt.scatter(Q[0], Q[1], color='red', s=80, label=f'Q ({Q[0]:.2f}, {Q[1]:.2f})')

# Draw perpendicular PQ
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'k--', linewidth=1.8, label='Perpendicular PQ')

# Draw a small arrow showing the line direction at Q
dir_vec = m / np.linalg.norm(m)
plt.arrow(Q[0], Q[1], 0.6*dir_vec[0], 0.6*dir_vec[1],
          head_width=0.12, head_length=0.18,
          length_includes_head=True, color='green')

# Axes formatting
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(min(-3, P[0]-2), max(4, P[0]+2))
plt.ylim(min(-1, P[1]-2), max(6, P[1]+3))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Foot of Perpendicular from P=(2,3) to line y=3x+4')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

