import os
import numpy as np
import matplotlib.pyplot as plt

# save figure in figs folder
figs_folder = os.path.join("..", "figs")
os.makedirs(figs_folder, exist_ok=True)  # create folder if it doesn't exist

# solve system of equations directly using numpy
# 3x - y = 0
# 5x - 2y = -15
A = np.array([[3, -1],
              [5, -2]], dtype=float)

b = np.array([0, -15], dtype=float)

solution = np.linalg.solve(A, b)
x, y = solution
print("Solution from Python:", solution)

# create x range for plotting
x_vals = np.linspace(0, 50, 100)

# equations
y1 = 3 * x_vals - 0      # from 3x - y = 0  → y = 3x
y2 = (5 * x_vals + 15)/2  # from 5x - 2y = -15 → y = (5x + 15)/2

# plotting
plt.figure(figsize=(8, 6))

# plot the lines
plt.plot(x_vals, y1, color="green")
plt.plot(x_vals, y2, color="blue")

# plot the solution point
plt.scatter(x, y, color="red")
plt.text(x + 0.5, y + 0.5, f"P({x:.2f},{y:.2f})", fontsize=10, color="red")

# move line labels towards right
x_label1 = 20  # moved right from 10 → 20
y_label1 = 3 * x_label1 - 5  # slight downward offset for clarity
plt.text(x_label1, y_label1, "3x - y = 0", color="green", fontsize=10, rotation=0)

x_label2 = 40  # moved right from 30 → 40
y_label2 = (5 * x_label2 + 15)/2 - 5  # slight downward offset
plt.text(x_label2, y_label2, "5x - 2y = -15", color="blue", fontsize=10, rotation=0)

# labels and grid
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Intersection of Two Lines and Solution Point P")
plt.grid(True)

# save figure
plt.tight_layout()
plt.savefig(os.path.join(figs_folder, "solution.png"))
plt.show()

