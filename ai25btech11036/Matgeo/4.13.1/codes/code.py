import numpy as np
import matplotlib.pyplot as plt

# Define range for x
x_vals = np.linspace(-10, 10, 400)

# Line equations
def y_L1(x): return (5 - x) / 3
def y_L2(x, k): return (3*x - 1) / k if k != 0 else np.full_like(x, np.nan)
def y_L3(x): return (12 - 5*x) / 2

# Choose k values for cases
k_values = [5, -6/5, 9]  # concurrent, parallel, triangle

# Create 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each set of lines for different k
for k in k_values:
    ax.plot(x_vals, y_L1(x_vals), np.zeros_like(x_vals), label=f"L1")
    ax.plot(x_vals, y_L2(x_vals, k), np.zeros_like(x_vals), label=f"L2 (k={k:.2f})")
    ax.plot(x_vals, y_L3(x_vals), np.zeros_like(x_vals), label=f"L3")

# Labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Representation of Lines L1, L2, L3 in z=0 plane")
ax.legend()
plt.show()
