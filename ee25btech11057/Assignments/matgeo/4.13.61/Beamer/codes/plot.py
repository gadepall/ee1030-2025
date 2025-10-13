import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 0.5      # slope of PQ and the reference line y = mx
a = 2        # y = a
b = 3        # x = b
x_P = np.linspace(-1, 1, 100)  # vary x-coordinate of P

# Coordinates of Q, S, R
y_Q = m*(b - x_P) + a
y_S = a + (b + x_P)/m
x_R = -x_P
y_R = y_Q + y_S - a

# Pick an example rectangle
example_idx = 50
P = (x_P[example_idx], a)
Q = (b, y_Q[example_idx])
S = (-b, y_S[example_idx])
R = (x_R[example_idx], y_R[example_idx])

# Rectangle vertices order for plotting
rect_x = [P[0], Q[0], R[0], S[0], P[0]]
rect_y = [P[1], Q[1], R[1], S[1], P[1]]

plt.figure(figsize=(9,6))

# Plot rectangle
plt.plot(rect_x, rect_y, 'k-', linewidth=2)
plt.scatter([P[0], Q[0], R[0], S[0]], [P[1], Q[1], R[1], S[1]], color='red')

# Plot locus of R
plt.plot(x_R, y_R, 'g--', linewidth=2)
plt.text(x_R[-1]+0.1, y_R[-1], 'Locus of R', color='green', fontsize=12, verticalalignment='bottom')

# Constraint lines and labels
plt.axhline(a, color='blue', linestyle=':', linewidth=1.5)
plt.text(0.5, a+0.1, 'y = a', color='blue', fontsize=12)

plt.axvline(b, color='orange', linestyle=':', linewidth=1.5)
plt.text(b+0.1, -1.5, 'x = b', color='orange', fontsize=12, verticalalignment='bottom')

plt.axvline(-b, color='purple', linestyle=':', linewidth=1.5)
plt.text(-b-0.1, -1.5, 'x = -b', color='purple', fontsize=12, horizontalalignment='right', verticalalignment='bottom')

# Plot y = mx line passing through origin
x_line = np.linspace(-4, 4, 100)
y_line = m * x_line
plt.plot(x_line, y_line, 'r--', linewidth=1.8)
plt.text(2, m*2+0.1, 'y = mx', color='red', fontsize=12)

# Label rectangle vertices
plt.text(P[0], P[1]+0.1, 'P', fontsize=12)
plt.text(Q[0]+0.1, Q[1], 'Q', fontsize=12)
plt.text(R[0], R[1]+0.1, 'R', fontsize=12)
plt.text(S[0]-0.3, S[1], 'S', fontsize=12)

# Set limits to see full rectangle and lines
plt.xlim(-4, 4)
plt.ylim(min(min(y_R), -2), max(max(y_R), 4))

plt.xlabel('x')
plt.ylabel('y')
plt.title('Rectangle PQRS, Locus of R, and y = mx')
plt.grid(True)
plt.axis('equal')
plt.savefig("../figs/locus.png")
plt.show()

