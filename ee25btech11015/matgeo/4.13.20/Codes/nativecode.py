import numpy as np
import matplotlib.pyplot as plt

# Define x range
x = np.linspace(-1, 6, 400)

# Original line: x + 3y = 3  -> y = (3 - x)/3
y1 = (3 - x) / 3

# Reflected line: 3y = x - 3 -> y = (x - 3)/3
y2 = (x - 3) / 3

# Plot the lines
plt.figure(figsize=(6,6))
plt.plot(x, y1, label="Incident Ray: $x + 3y = 3$", color="blue")
plt.plot(x, y2, label="Reflected Ray: $3y = x - 3$", color="red")

# Point of incidence
plt.scatter(3, 0, color="black", s=60, zorder=5)
plt.text(3.1, 0.2, "P(3,0)", fontsize=10)

# Axes
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)

plt.xlim(-1, 6)
plt.ylim(-2, 4)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Reflection of Ray $x+3y=3$ at the X-axis")
plt.legend()
plt.grid(True)
plt.gca().set_aspect("equal")

plt.show()
