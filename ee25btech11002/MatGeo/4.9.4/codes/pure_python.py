import numpy as np
import matplotlib.pyplot as plt

# --- Given point ---
P = np.array([3, -2])

# --- Define functions for lines ---
def line_y_given_x(a, b, c, x_vals):
    # Line: ax + by + c = 0 => y = (-a*x - c)/b
    return (-a * x_vals - c) / b

# --- Given line: sqrt(3)x + y - 1 = 0 ---
a1, b1, c1 = np.sqrt(3), 1, -1

# --- Required lines ---
# Line 1: y + 2 = 0 => 0*x + 1*y + 2 = 0
a2, b2, c2 = 0, 1, 2

# Line 2: sqrt(3)x - y - (3sqrt(3)+2) = 0
a3, b3, c3 = np.sqrt(3), -1, -(3*np.sqrt(3) + 2)

# --- Generate x values over a much wider range ---
x_vals = np.linspace(-20, 25, 400)

# --- Compute y values for each line ---
y1 = line_y_given_x(a1, b1, c1, x_vals)
y2 = line_y_given_x(a2, b2, c2, x_vals)
y3 = line_y_given_x(a3, b3, c3, x_vals)

# --- Plot ---
plt.figure(figsize=(12,8))

plt.plot(x_vals, y1, 'b-', linewidth=2)
plt.plot(x_vals, y2, 'r-', linewidth=2)
plt.plot(x_vals, y3, 'g-', linewidth=2)

# Plot the common point
plt.scatter(P[0], P[1], color='k', s=80, zorder=5)
plt.text(P[0]+0.9, P[1]-2.0, "(3,-2)", fontsize=10, color='k')

# --- Place labels on the lines directly in non-overlapping positions ---
# For the blue line, place the label in the bottom-right quadrant.
# A small vertical offset (+ 0.5) is added to prevent it from sitting directly on the line.
plt.text(9, line_y_given_x(a1, b1, c1, 9) + 0.6, r'$\sqrt{3}x+y=1$', color='b', fontsize=12)

# For the red line, place the label to the right of the intersection point.
plt.text(12, line_y_given_x(a2, b2, c2, 5), r'$y+2=0$', color='r', fontsize=12)

# For the green line, place the label in the upper-right quadrant, away from the blue line's label.
plt.text(9, line_y_given_x(a3, b3, c3, 9) + 0.5, r'$\sqrt{3}x - y -(3\sqrt{3}+2)=0$', color='g', fontsize=12)


# Axes settings
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Lines through (3,-2) at 60° to given line")

# --- Set plot boundaries to ensure lines touch the edge ---
plt.xlim(-200, 250)
plt.ylim(-100, 100)
plt.axis("equal") 
plt.show()