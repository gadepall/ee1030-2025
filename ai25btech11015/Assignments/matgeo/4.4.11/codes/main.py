import numpy as np
import matplotlib.pyplot as plt

# Points A and B
A = np.array([2, 1])
B = np.array([5, -8])

# Vector AB
AB = B - A

# Trisection points
P = A + (1/3) * AB
Q = A + (2/3) * AB

# Line condition: 2x - y + k = 0 with P on it
k = -(2*P[0] - P[1])
print(f"P = {P}, Q = {Q}, k = {k}")

# Plotting
fig, ax = plt.subplots()

# Plot line segment AB and trisection points
ax.plot([A[0], B[0]], [A[1], B[1]], 'b-', label="AB")
ax.scatter(*A, color='red')
ax.text(*A, "A", fontsize=12, ha='right', va='bottom')

ax.scatter(*B, color='red')
ax.text(*B, "B", fontsize=12, ha='left', va='bottom')

ax.scatter(*P, color='green')
ax.text(*P, "P", fontsize=12, ha='left', va='top')

ax.scatter(*Q, color='purple')
ax.text(*Q, "Q", fontsize=12, ha='left', va='top')

# Plot the line 2x - y + k = 0
x_vals = np.linspace(0, 6, 200)
y_vals = 2*x_vals + k
ax.plot(x_vals, y_vals, 'r--', label=f"2x - y + {k:.0f} = 0")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)
ax.set_aspect("equal")

# Save figure
fig.savefig("../figs/fig.png", dpi=300)
plt.close(fig)
