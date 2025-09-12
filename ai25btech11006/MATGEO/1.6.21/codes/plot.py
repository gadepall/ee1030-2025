import numpy as np
import matplotlib.pyplot as plt
import os

# Example values
a, b, c = 1, 2, 3

# Define points
points = np.array([
    [a, b+c],  # A
    [b, c+a],  # B
    [c, a+b]   # C
])

# Read points
x, y = points[:,0], points[:,1]

# Plot
plt.scatter(x, y, color="red", label="Points A, B, C")
plt.plot(x, y, linestyle="--", color="blue")

for i, txt in enumerate(["A", "B", "C"]):
    plt.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(5, 5))

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)
plt.axis("equal")

# --- Ensure folder exists ---
save_path = "../figs"
os.makedirs(save_path, exist_ok=True)

# Save BEFORE showing
plt.savefig(os.path.join(save_path, "img.png"), dpi=300, bbox_inches='tight')
plt.show()

