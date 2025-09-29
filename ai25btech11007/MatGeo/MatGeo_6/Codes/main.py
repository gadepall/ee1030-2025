import math
import matplotlib.pyplot as plt

# Given data
a = 5.0        # BC
K = 7.5        # AB + AC = b + c
cosB = 0.5     # cos(60°)
sinB = math.sqrt(3) / 2  # sin(60°)

# Formula from solution
c = (K**2 - a**2) / (2 * (K - a * cosB))
b = K - c

# Coordinates with B=(0,0), C=(a,0)
Ax = (c * cosB) / sinB
Ay = c / sinB
Bx, By = 0.0, 0.0
Cx, Cy = a, 0.0

print("Computed values:")
print(f"c (AC) = {c:.6f}")
print(f"b (AB) = {b:.6f}")
print(f"A = ({Ax:.6f}, {Ay:.6f})")
print(f"B = ({Bx:.6f}, {By:.6f})")
print(f"C = ({Cx:.6f}, {Cy:.6f})")

# Plotting the triangle
fig, ax = plt.subplots()
triangle_x = [Ax, Bx, Cx, Ax]
triangle_y = [Ay, By, Cy, Ay]
ax.plot(triangle_x, triangle_y, 'b-', linewidth=2)

# Mark points
ax.scatter([Ax, Bx, Cx], [Ay, By, Cy], color='red', zorder=5)
ax.text(Ax, Ay+0.2, "A", fontsize=12, ha='center')
ax.text(Bx, By-0.2, "B", fontsize=12, ha='center')
ax.text(Cx, Cy-0.2, "C", fontsize=12, ha='center')

# Formatting
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title("Construction of Triangle ABC")

plt.show()
