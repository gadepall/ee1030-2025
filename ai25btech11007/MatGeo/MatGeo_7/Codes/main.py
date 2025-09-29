import numpy as np
import matplotlib.pyplot as plt

# Angles in degrees
alpha, beta, gamma = 30, 60, 90

# Direction cosines
lx = np.cos(np.radians(alpha))
ly = np.cos(np.radians(beta))
lz = np.cos(np.radians(gamma))

print("Direction cosines:")
print(f"cos(30°) = {lx:.3f}")
print(f"cos(60°) = {ly:.3f}")
print(f"cos(90°) = {lz:.3f}")

print("\nEquation of the line:")
print("y = x / sqrt(3),  z = 0")

# Generate sample points on the line
x_vals = np.linspace(0, 10, 6)
y_vals = x_vals / np.sqrt(3)
z_vals = np.zeros_like(x_vals)

print("\nSample points on the line:")
for x, y, z in zip(x_vals, y_vals, z_vals):
    print(f"({x:.2f}, {y:.2f}, {z:.2f})")

# Plot the line in 3D
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_vals, y_vals, z_vals, label=r'$y = \frac{x}{\sqrt{3}}, z=0$', color='blue', linewidth=2)

# Labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Line through origin making 30°, 60°, 90° with X, Y, Z axes')
ax.legend()

plt.show()
