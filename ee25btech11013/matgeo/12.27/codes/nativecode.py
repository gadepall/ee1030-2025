import numpy as np
import matplotlib.pyplot as plt

def hyperbola1(x):
    # From: xy - 1000x - 2400y = 0  =>  y = 1000x / (x - 2400)
    return (1000 * x) / (x - 2400)

def hyperbola2(x):
    # From: xy - 750x - 2700y = 0  =>  y = 750x / (x - 2700)
    return (750 * x) / (x - 2700)

# Centers (from completing the product form)
center1 = (2400, 1000)
center2 = (2700, 750)

x1 = np.linspace(-6000, 6000, 2000)

# Avoid division by zero at vertical asymptotes
x1 = x1[x1 != 2400]
x2 = x1[x1 != 2700]

y1 = hyperbola1(x1)
y2 = hyperbola2(x1)

plt.figure(figsize=(9, 7))

# Plot both hyperbolas
plt.plot(x1, y1, 'b', label='Hyperbola 1: xy - 1000x - 2400y = 0')
plt.plot(x1, y2, 'r', label='Hyperbola 2: xy - 750x - 2700y = 0')

# Plot asymptotes for each hyperbola
plt.axvline(x=2400, color='b', linestyle='--', alpha=0.6)
plt.axhline(y=1000, color='b', linestyle='--', alpha=0.6)
plt.axvline(x=2700, color='r', linestyle='--', alpha=0.6)
plt.axhline(y=750, color='r', linestyle='--', alpha=0.6)

# Plot centers
plt.scatter(*center1, color='blue', s=80, zorder=10)
plt.text(center1[0]+50, center1[1]+80, f"C₁({center1[0]}, {center1[1]})", fontsize=10, color='blue')

plt.scatter(*center2, color='red', s=80, zorder=10)
plt.text(center2[0]+50, center2[1]+80, f"C₂({center2[0]}, {center2[1]})", fontsize=10, color='red')

# Intersection point (from matrix solution)
intersection = (3600, 3000)
plt.scatter(*intersection, color='black', s=90, label=f'Intersection {intersection}')

plt.title("Both Branches of the Hyperbolas (1st & 3rd Quadrants)", fontsize=13)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='k', linewidth=0.8)
plt.axvline(0, color='k', linewidth=0.8)
plt.legend(fontsize=9, loc='upper left')
plt.axis('equal')
plt.xlim(-6000, 6000)
plt.ylim(-6000, 6000)
plt.tight_layout()
plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/12.27/figs/Figure_1.png")
plt.show()

