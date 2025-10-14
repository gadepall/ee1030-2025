import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Points
P = np.array([4, 2, -6])
Q = np.array([5, -3, 1])
R = np.array([12, 4, 5])
S = np.array([11, 9, -2])
O = (P + R) / 2   # intersection

# Diagonals
PR = np.vstack((P, R))
QS = np.vstack((Q, S))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot edges of parallelogram
edges = [(P, Q), (Q, R), (R, S), (S, P)]
for edge in edges:
    ax.plot(*zip(*edge), color='black')

# Plot diagonals
ax.plot(*zip(*PR), color='red', linestyle='--', label='Diagonal PR')
ax.plot(*zip(*QS), color='blue', linestyle='--', label='Diagonal QS')

# Scatter points
for pt in [P, Q, R, S]:
    ax.scatter(*pt, color='green', s=70, marker='x')
ax.scatter(*O, color='darkblue', s=100, marker='x', label="Intersection")

# Format coords for labels
def clean_coords(arr):
    return tuple(int(x) if float(x).is_integer() else round(float(x),2) for x in arr)

# Labels placed with small offset
offset = 0.3
labels = {
    "P": (P, (offset, offset, offset)),
    "Q": (Q, (offset, offset, offset)),
    "R": (R, (offset, offset, offset)),
    "S": (S, (offset, offset, offset)),
    "O": (O, (offset, offset, offset)),
}

for name, (point, delta) in labels.items():
    label_pos = point + np.array(delta)
    ax.text(*label_pos, f"{name}{clean_coords(point)}",
            fontsize=11, fontweight="bold",
            color="darkblue" if name=="O" else "green",
            bbox=dict(facecolor="white", edgecolor="none", pad=2, alpha=0.8))

# Axes and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Parallelogram PQRS with Diagonals and Intersection")

ax.legend()
plt.show()