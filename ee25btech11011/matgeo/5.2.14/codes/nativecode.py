import numpy as np
import matplotlib.pyplot as plt

# Coefficients of the system
# Equations:
# 1) x - 3y = 3
# 2) 3x - 9y = 2

a1, b1, c1 = 1, -3, 3
a2, b2, c2 = 3, -9, 2

# Solve the system
det = a1 * b2 - a2 * b1

if det == 0:
    if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
        print("Infinite solutions (coincident lines).")
    else:
        print("No solution (parallel lines).")
    x_sol = None
    y_sol = None
else:
    x_sol = (c1 * b2 - c2 * b1) / det
    y_sol = (a1 * c2 - a2 * c1) / det
    print(f"Unique solution: x = {x_sol:.2f}, y = {y_sol:.2f}")

# Plot the lines
x_vals = np.linspace(-5, 5, 400)
y1 = (c1 - a1 * x_vals) / b1
y2 = (c2 - a2 * x_vals) / b2

plt.figure(figsize=(6,6))
plt.plot(x_vals, y1, label="x - 3y = 3", color="blue")
plt.plot(x_vals, y2, label="3x - 9y = 2", color="red", linestyle="--")

# If there is a unique solution, mark it on the plot
if x_sol is not None and y_sol is not None:
    plt.plot(x_sol, y_sol, 'go', label="Intersection")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of Two Lines")
plt.legend()
plt.grid(True)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

# Save figure
plt.savefig("fig7.png", dpi=150)
plt.show()

print("Graph saved as fig7.png")
