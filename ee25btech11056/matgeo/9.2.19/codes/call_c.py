import ctypes
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Folder to save figures
figs_folder = os.path.join("..", "figs")

# Load shared object
lib = ctypes.CDLL("./points.so")

# Define return type and argument types
lib.area_calculate.restype = ctypes.c_double
lib.area_calculate.argtypes = [ctypes.c_double, ctypes.c_double]

# Input: a = 1 (for calculation), but label as "a" on graph
a = 1.0
b = a / np.sqrt(2)   # x = a/sqrt(2)
c = a                # radius

# Call the C function
area = lib.area_calculate(b, c)
print("Smaller area from C:", area)

# Circle points using y^2 = a^2 - x^2
x_vals = np.linspace(-a, a, 500)   #range is [-1,1]
y_upper = np.sqrt(a**2 - x_vals**2)
y_lower = -np.sqrt(a**2 - x_vals**2)

# Line x = a/sqrt(2)
x_line = np.full_like(x_vals, b) #creates an numpy array with the same shape and dtype as x_vals filled every entry with b
y_line = np.linspace(-a, a, 500)

# Intersection points
y_inter = np.sqrt(a**2 - b**2)
points = [(b, y_inter), (b, -y_inter)]

# Plotting
fig, ax = plt.subplots(figsize=(8, 8))

# Plot circle (upper + lower)
ax.plot(x_vals, y_upper, 'g', label=r"$x^2+y^2=a^2$") #g for green color , r means raw string ,tells python not to treat \ as escape sequences
ax.plot(x_vals, y_lower, 'g')

# Plot line
ax.plot(x_line, y_line, 'b', label=r"$x=\frac{a}{\sqrt{2}}$") #r means raw string ,tells python not to treat \ as escape sequences

# Shade smaller region (right part of circle cut by line)
mask = x_vals >= b #numpy boolean array created by condition x_vlas>=b , x points towards right of b is true so array stores 1 as entry

ax.fill_betweenx(y_upper[mask], b, x_vals[mask], color="cyan", alpha=0.5) #shades region where points satisfy mask condition
ax.fill_betweenx(y_lower[mask], b, x_vals[mask], color="cyan", alpha=0.5, label="Smaller Region")

# Plot intersection points
for px, py in points:
    ax.scatter(px, py, color="red")
ax.text(b+0.05, y_inter, r"P1$(\frac{a}{\sqrt{2}}, \frac{a}{\sqrt{2}})$", fontsize=10)
ax.text(b+0.05, -y_inter, r"$P2(\frac{a}{\sqrt{2}}, -\frac{a}{\sqrt{2}})$", fontsize=10)

# Mark point (a,0) on the circle
ax.scatter(a, 0, color="purple")
ax.text(a+0.05, 0, r"A$(a,0)$", fontsize=10, color="purple")

# Axes
ax.axhline(0, color="black", linewidth=0.8) #draw horizontal line(x axis) at y=0
ax.axvline(0, color="black", linewidth=0.8) #draw vetical line(y axis) at x=0

ax.set_aspect("equal") #set equal units for x and y axes
ax.set_xlim(-1.2*a, 1.2*a)  #sets range for visible x ases
ax.set_ylim(-1.2*a, 1.2*a)
ax.set_title("Smaller Area Cut by Line and Circle")
ax.legend()
ax.grid(True)

# Save figure
plt.tight_layout()
fig.savefig(os.path.join(figs_folder, "circle_area.png"))
plt.show()

