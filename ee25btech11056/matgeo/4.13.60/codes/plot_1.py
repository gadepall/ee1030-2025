import os
import numpy as np
import matplotlib.pyplot as plt

# Folder to save figures
figs_folder = os.path.join("..","figs")

# Given slope m
m_val = 0.04075

# Input values
l1 = (1.0/3.0, 1.0)
l2 = (2.0, 1.0)
l3 = (-1.0, 1.0)
c1, c2, c3 = -2.0/3.0, -4.0, -5.0

# Compute k1, k2, k3 using same formulas
k1 = (c1 - 5*l1[0] - 4*l1[1]) / (l1[0] + l1[1]*m_val)
k2 = (c2 - 5*l2[0] - 4*l2[1]) / (l2[0] + l2[1]*m_val)
k3 = (c3 - 5*l3[0] - 4*l3[1]) / (l3[0] + l3[1]*m_val)

# Points A, B, C, D
A = (5, 4)
B = (5 + k1, 4 + k1*m_val)
C = (5 + k2, 4 + k2*m_val)
D = (5 + k3, 4 + k3*m_val)

# Create figure
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the line through A with slope m
x_vals = np.linspace(-15, 15, 100)
y_line = 4 + m_val * (x_vals - 5)
ax.plot(x_vals, y_line, label=f"Line through A, slope={m_val:.3f}", color="blue")

# Plot the three given lines
y1 = (-1/3)*x_vals - 2/3
ax.plot(x_vals, y1, label="x+3y+2=0", color="red")

y2 = (-2)*x_vals - 4
ax.plot(x_vals, y2, label="2x+y+4=0", color="green")

y3 = x_vals - 5
ax.plot(x_vals, y3, label="x-y-5=0", color="purple")

# Plot points A, B, C, D
points = {"A": A, "B": B, "C": C, "D": D}
for label, (px, py) in points.items():
    ax.scatter(px, py, color="black", s=30)
    ax.annotate(f"{label}({px:.2f},{py:.2f})", (px, py),
                textcoords="offset points", xytext=(5, 5))

# Labels and legend
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_title(f"Line through A with slope m={m_val:.3f} and intersections with given lines")
ax.legend()
ax.grid(True)

# Save figure
plt.tight_layout()
fig.savefig(os.path.join(figs_folder,"lines_1.png"))
plt.show()

