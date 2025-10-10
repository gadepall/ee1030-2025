import matplotlib.pyplot as plt
import numpy as np

# Define lines
x = np.linspace(-1, 5, 400)

# L1: x + 3y - 5 = 0 → y = (5 - x)/3
y1 = (5 - x) / 3

# L2: 3x - k*y - 1 = 0 → y = (3x - 1)/k (example with k=5)
k = 5
y2 = (3*x - 1) / k

# L3: 5x + 2y - 12 = 0 → y = (12 - 5x)/2
y3 = (12 - 5*x) / 2

# Plot
plt.figure(figsize=(6,6))
plt.axhline(0, color="black", linewidth=0.8)  # x-axis
plt.axvline(0, color="black", linewidth=0.8)  # y-axis

plt.plot(x, y1, "r", label="L1: x+3y-5=0")
plt.plot(x, y2, "b", label=f"L2: 3x-{k}y-1=0")
plt.plot(x, y3, "g", label="L3: 5x+2y-12=0")

# Intersection point (2,1)
plt.plot(2, 1, "ko", markersize=6)
plt.text(2.1, 0.9, "(2,1)")

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphical Representation of L1, L2, L3")
plt.legend()
plt.grid(True)
plt.show()
