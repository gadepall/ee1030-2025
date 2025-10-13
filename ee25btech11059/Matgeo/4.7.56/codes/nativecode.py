import matplotlib.pyplot as plt
import numpy as np

# Constants
sqrt3 = np.sqrt(3)
A = 2 + sqrt3
B = 1
C = 8 * np.sqrt(2 + sqrt3)

# Create x values
x = np.linspace(-10, 10, 400)

# Two lines: one for +C and one for -C
y1 = -A * x + C  # Line 1
y2 = -A * x - C  # Line 2

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r'$(2+\sqrt{3})x + y = +8\sqrt{2+\sqrt{3}}$', color='blue')
plt.plot(x, y2, label=r'$(2+\sqrt{3})x + y = -8\sqrt{2+\sqrt{3}}$', color='green')

# === Calculate the foot of the perpendicular from origin to line1 ===
x0, y0 = 0, 0
A_val = A
B_val = 1
C_val = -C  # Rewrite as Ax + By + C = 0

denominator = A_val**2 + B_val**2
x_foot = (B_val * (B_val * x0 - A_val * y0) - A_val * C_val) / denominator
y_foot = (A_val * (A_val * y0 - B_val * x0) - B_val * C_val) / denominator

# === Draw extended solid normal line through origin and foot ===
# Direction vector of normal = (A, B)
normal_length = 15  # increase to make longer
unit_normal = np.array([A_val, B_val]) / np.sqrt(denominator)
start_point = -normal_length * unit_normal
end_point = normal_length * unit_normal

plt.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]],
         color='red', linewidth=2, label='Normal (Extended)')

# Plot origin and foot point
plt.plot(0, 0, 'ro', label='Origin')
plt.plot(x_foot, y_foot, 'ko', label='Foot of Perpendicular')

# Axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Formatting
plt.title('Graph with Extended Normal Line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.axis('equal')
plt.legend()

# Save and show plot
plt.savefig("graph7_with_extended_normal.png")
plt.show()
