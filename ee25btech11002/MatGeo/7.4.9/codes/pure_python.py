import numpy as np
import matplotlib.pyplot as plt


# Circle parameters: x^2 + y^2 = 6
r = np.sqrt(6)

# Line: 2x - 3y = 1 => y = (2x-1)/3
x_line = np.linspace(-3, 3, 400)
y_line = (2*x_line - 1) / 3

# Points
points = {
    "$p_1$(2, 3/4)": (2, 3/4),
 
    "$p_3$ (1/4, -1/4)": (0.25, -0.25),
    "$p_4$ (1/8, 1/4)": (0.125, 0.25)
}
point = {
       "$p_2$(5/2 ,3/4)": (2.5, 0.75),
}

# Circle
theta = np.linspace(0, 2*np.pi, 500)
x_circle = r * np.cos(theta)
y_circle = r * np.sin(theta)

plt.figure(figsize=(7,7))
plt.plot(x_circle, y_circle, 'b')
plt.text(r*np.cos(np.pi/4), r*np.sin(np.pi/4), "x² + y² = 6", color='b', fontsize=10)

# Line
plt.plot(x_line, y_line, 'r')
plt.text(-2.5, -2.5, "2x - 3y = 1", color='r', fontsize=10)

# Shaded region (smaller part)
xx, yy = np.meshgrid(np.linspace(-r, r, 400), np.linspace(-r, r, 400))
mask_circle = xx**2 + yy**2 <= 6
mask_line = 2*xx - 3*yy - 1 > 0
mask = mask_circle & mask_line

plt.contourf(xx, yy, mask, levels=[0.5, 1], colors=['#ffcccc'], alpha=0.5)
plt.text(0, -2, "Smaller region", color='darkred', fontsize=10)

# Points
for label, (x, y) in points.items():
    plt.scatter(x, y, s=70)
    plt.text(x-0.5, y-0.35, label, fontsize=9)

# Point
for label, (x, y) in point.items():
    plt.scatter(x, y, s=70)
    plt.text(x-0.3, y-0.3, label, fontsize=9)

# Formatting
plt.gca().set_aspect('equal', adjustable='box')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.grid(True)
plt.title("Circle cut by the Line")
plt.show()