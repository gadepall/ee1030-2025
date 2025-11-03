import numpy as np
import matplotlib.pyplot as plt
import ctypes

lib = ctypes.CDLL("./libcode.so")
lib.determinant3.restype = ctypes.c_double

# Example use of determinant from C
A = ((ctypes.c_double * 3) * 3)()
data = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]
for i in range(3):
    for j in range(3):
        A[i][j] = data[i][j]

det_val = lib.determinant3(A)
print("Determinant (computed in C):", det_val)
def hyperbola1(x):
    return (1000 * x) / (x - 2400)

def hyperbola2(x):
    return (750 * x) / (x - 2700)

center1 = (2400, 1000)
center2 = (2700, 750)
intersection = (3600, 3000)

# Plot both branches
x_vals = np.linspace(-6000, 6000, 2000)
x_vals1 = x_vals[x_vals != 2400]
x_vals2 = x_vals[x_vals != 2700]

y1 = hyperbola1(x_vals1)
y2 = hyperbola2(x_vals2)

plt.figure(figsize=(9, 7))

plt.plot(x_vals1, y1, 'b', label='Hyperbola 1: xy - 1000x - 2400y = 0')
plt.plot(x_vals2, y2, 'r', label='Hyperbola 2: xy - 750x - 2700y = 0')

# Centers and asymptotes
plt.scatter(*center1, color='blue', s=70)
plt.scatter(*center2, color='red', s=70)
plt.axvline(x=2400, color='b', linestyle='--', alpha=0.6)
plt.axhline(y=1000, color='b', linestyle='--', alpha=0.6)
plt.axvline(x=2700, color='r', linestyle='--', alpha=0.6)
plt.axhline(y=750, color='r', linestyle='--', alpha=0.6)

# Intersection
plt.scatter(*intersection, color='black', s=90, label='Intersection (3600,3000)')
plt.text(intersection[0]+80, intersection[1]+80, f"({intersection[0]}, {intersection[1]})", fontsize=10)

# Formatting
plt.title("Hyperbolas in Original Coordinates (1st & 3rd Quadrants)", fontsize=13)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='k', linewidth=0.8)
plt.axvline(0, color='k', linewidth=0.8)
plt.axis('equal')
plt.xlim(-6000, 6000)
plt.ylim(-6000, 6000)
plt.legend(fontsize=9, loc='upper left')
plt.tight_layout()
plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/12.27/figs/Figure_1.png")

plt.show()

