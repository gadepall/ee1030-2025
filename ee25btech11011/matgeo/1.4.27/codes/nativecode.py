import matplotlib.pyplot as plt

# --- Data ---
# Position vectors (points A and B)
A = (2, 3)   # Example coordinates of A
B = (5, -1)  # Example coordinates of B

# Ratio for external division (C divides AB externally in 3:1)
k = 3  

# Section formula for external division:
# C = (k*b - a) / (k - 1)
Cx = (k*B[0] - A[0]) / (k - 1)
Cy = (k*B[1] - A[1]) / (k - 1)
C = (Cx, Cy)

print(f"Position vector of C is: {C}")

# --- Plotting ---
points = [A, B, C]
x_coords, y_coords = zip(*points)

plt.figure(figsize=(7, 6))

# Plot points
plt.scatter(x_coords, y_coords, color='red', s=80, zorder=5)

# Connect A-B (main line)
plt.plot([A[0], B[0]], [A[1], B[1]], color='blue', label='Line AB')

# Show extended line through A-B-C
plt.plot(x_coords, y_coords, '--g', label='Line with C')

# Labels
labels = ['A'+str(A), 'B'+str(B), 'C'+str(C)]
for (x, y), label in zip(points, labels):
    plt.text(x + 0.2, y + 0.2, label, fontsize=10)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('External Division (C divides AB in ratio 3:1)')
plt.legend()
plt.grid(True)
import os

# Your plotting code above...
plt.savefig("figs/fig1.png", dpi=300, bbox_inches="tight")
plt.show()

# Add this to check where the file is saved
print("Figure saved in folder:", os.getcwd())
