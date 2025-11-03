import os
import numpy as np
import matplotlib.pyplot as plt

# save figure in figs folder
figs_folder = os.path.join("..", "figs")
os.makedirs(figs_folder, exist_ok=True)  # create folder if it doesn't exist

# solve system of equations directly using numpy
# -3x + y = 3
# -2x + y = 13
A = np.array([[-3, 1],
              [-2, 1]], dtype=float)

b = np.array([3, 13], dtype=float)

solution = np.linalg.solve(A, b)
x, y = solution
print("Solution from Python:", solution)

# create x range for plotting
x_vals = np.linspace(0, 15, 100)

# equations solved for y
y1 = 3 * x_vals + 3      # from y = 3x + 3
y2 = 2 * x_vals + 13 - 2*x_vals? let's compute properly
# original equation: -2x + y = 13 → y = 2x + 13

y2 = 2 * x_vals + 13     # from -2x + y = 13 → y = 2x + 13

# plotting
plt.figure(figsize=(8, 6))

# plot the lines
plt.plot(x_vals, y1, label="y = 3x + 3", color="green")
plt.plot(x_vals, y2, label="y = 2x + 13", color="blue")

# plot the solution point
plt.scatter(x, y, color="red", label=f"P({x:.2f},{y:.2f})")
plt.text(x + 0.3, y + 0.3, f"P({x:.2f},{y:.2f})", fontsize=10, color="red")

# labels and grid
plt.xlabel("X axis (Son's Age)")
plt.ylabel("Y axis (Father's Age)")
plt.title("Father-Son Age Problem: Intersection Point")
plt.legend()
plt.grid(True)

# save figure
plt.tight_layout()
plt.savefig(os.path.join(figs_folder, "solution.png"))
plt.show()

