import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use("TkAgg")

# Coefficient matrix and RHS vector
A = np.array([[2, 3],
              [4, 5]], dtype=float)
b = np.array([13, 23], dtype=float)

# Solve system Ax = b
x = np.linalg.solve(A, b)
print("Solution vector for the system of equations:", x)

# Prepare x values for plotting
x_vals = np.linspace(-2, 10, 400)

# Express y in terms of x for both equations
y1 = (13 - 2*x_vals) / 3      # from 2x + 3y = 13
y2 = (23 - 4*x_vals) / 5      # from 4x + 5y = 23

# Plot both lines
plt.plot(x_vals, y1, label=r"$2x + 3y = 13$")
plt.plot(x_vals, y2, label=r"$4x + 5y = 23$")

# Mark the solution point
plt.scatter(x[0], x[1], color="red", zorder=5)
plt.text(x[0] + 0.2, x[1], f"({x[0]:.1f}, {x[1]:.1f})", color="red")

# Formatting
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphical Solution of the Linear System")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.grid(True)

plt.show()

