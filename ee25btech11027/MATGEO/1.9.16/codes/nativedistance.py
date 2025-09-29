
import math
import matplotlib.pyplot as plt

# Fixed values
a, b = 4, 4

# Points
A = (a, b)
B = (-a, -b)

# Midpoint
M = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)

# Distance
d = 2 * math.sqrt(a**2 + b**2)
print(f"Distance between {A} and {B} = {d:.2f}")

# Plot
plt.figure(figsize=(6,6))
plt.plot([A[0], B[0]], [A[1], B[1]], 'ro-', label="Line AB")  # line + points
plt.plot(M[0], M[1], 'bo', markersize=8, label="Midpoint")    # midpoint

# Annotate points
plt.text(A[0], A[1], f"A{A}", fontsize=10, ha='right', color='red')
plt.text(B[0], B[1], f"B{B}", fontsize=10, ha='left', color='red')
plt.text(M[0], M[1], f"M{M}", fontsize=10, ha='center', va='bottom', color='blue')

# Labels and grid
plt.title(f"Distance AB = {d:.2f}")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.savefig("/media/indhiresh-s/New Volume/matgeo/figs/figure1.png")
plt.show()
