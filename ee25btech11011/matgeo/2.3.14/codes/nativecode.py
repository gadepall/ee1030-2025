import numpy as np
import matplotlib.pyplot as plt
import os

# Create output directory if not present
os.makedirs("figs", exist_ok=True)

# Given angles
alpha = np.deg2rad(30)   # with X-axis
beta  = np.deg2rad(120)  # with Y-axis

# Direction cosines
cos_alpha = np.cos(alpha)
cos_beta  = np.cos(beta)

# Find cos(gamma) from unit vector condition
cos_gamma_sq = 1 - (cos_alpha**2 + cos_beta**2)
cos_gamma_sq = max(cos_gamma_sq, 0)  # prevent negatives due to rounding
cos_gamma = np.sqrt(cos_gamma_sq)

# Print numerical values (the "answer")
print("Direction Cosines:")
print(f"cos(alpha) = {cos_alpha:.4f}")
print(f"cos(beta)  = {cos_beta:.4f}")
print(f"cos(gamma) = {cos_gamma:.4f}")

# Angle with Z-axis
gamma = np.rad2deg(np.arccos(cos_gamma))
print(f"\nThe line makes an angle of {gamma:.2f}° with the positive Z-axis.\n")

# Direction vector
d = np.array([cos_alpha, cos_beta, cos_gamma])

# Line parameter t
t = np.linspace(-3, 3, 100)
x = d[0] * t
y = d[1] * t
z = d[2] * t

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the line
ax.plot(x, y, z, color="blue", label=r"$L : (\cos\alpha, \cos\beta, \cos\gamma)t$")

# Draw X, Y, Z axes with arrows
ax.quiver(0, 0, 0, 3, 0, 0, color="red", arrow_length_ratio=0.05)
ax.text(3.2, 0, 0, "X", color="red")

ax.quiver(0, 0, 0, 0, 3, 0, color="green", arrow_length_ratio=0.05)
ax.text(0, 3.2, 0, "Y", color="green")

ax.quiver(0, 0, 0, 0, 0, 3, color="black", arrow_length_ratio=0.05)
ax.text(0, 0, 3.2, "Z", color="black")

# Axis labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Line with Direction Cosines")

ax.legend()

# Set view limits
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

# Save figure
plt.title("Line with Direction Cosines")
plt.savefig("fig3.png", dpi=300, bbox_inches="tight")  # Save the figure
plt.show()
