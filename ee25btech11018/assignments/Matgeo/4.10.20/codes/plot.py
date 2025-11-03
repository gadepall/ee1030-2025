import matplotlib.pyplot as plt
import numpy as np

# Input points
Ax, Ay = -1, 1
Bx, By = 3, 3

# Midpoint
Mx, My = (Ax + Bx) / 2, (Ay + By) / 2

# Direction vector of AB
dx, dy = Bx - Ax, By - Ay

# Equation of perpendicular bisector: a*x + b*y = c
a, b = dx, dy
c = a*Mx + b*My

# Intersection with y-axis (x=0)
y_inter = c / b

print(f"Equation of perpendicular bisector: {a}x + {b}y = {c}")
print(f"Intersection with y-axis: (0, {y_inter})")

# -------------------------
# Plotting
# -------------------------

# Line AB
x_AB = [Ax, Bx]
y_AB = [Ay, By]

# Perpendicular bisector line
x_line = np.linspace(-2, 5, 100)
y_line = (c - a*x_line) / b

plt.figure(figsize=(6,6))
plt.plot(x_AB, y_AB, 'r--', label="Line AB")
plt.scatter([Ax, Bx], [Ay, By], color='red', label="Points A & B")

plt.plot(x_line, y_line, 'b-', label="Perpendicular Bisector")
plt.scatter([0], [y_inter], color='green', s=80, label="Intersection with y-axis")

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.legend()
plt.grid(True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Perpendicular Bisector of AB and Intersection with Y-axis")
plt.show()

