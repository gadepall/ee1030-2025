import numpy as np
import matplotlib.pyplot as plt

# Input
n = np.array([np.sqrt(3.0), 1.0])
c = 2.0

# Compute norm, unit normal, and p
norm_n = np.linalg.norm(n)
unit_n = n / norm_n
p = -c / norm_n
theta = np.arctan2(unit_n[1], unit_n[0])

# Print results
print("n =", n)
print("c =", c)
print("||n|| =", norm_n)
print("unit normal =", unit_n)
print("p =", p)
print("theta =", theta, "rad (~", theta*180/np.pi, "degrees )")

# Plot the line: sqrt(3)x + y + 2 = 0 -> y = -sqrt(3)x - 2
x_vals = np.linspace(-4, 4, 400)
y_vals = -np.sqrt(3.0) * x_vals - 2

plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, label="Line: sqrt(3)x + y + 2 = 0")

# Plot unit normal arrow from origin
plt.quiver(0, 0, unit_n[0], unit_n[1],
           angles="xy", scale_units="xy", scale=1,
           color="red", label="Unit normal")

# Axes and labels
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.gca().set_aspect("equal")
plt.xlim(-4, 4)
plt.ylim(-6, 4)
plt.legend()
plt.title("Line and its Unit Normal")
plt.grid(True)
plt.savefig("normalform_new.png")
plt.show()

