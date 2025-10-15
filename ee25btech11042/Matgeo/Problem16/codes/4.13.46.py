import numpy as np
import matplotlib.pyplot as plt

# --- 1. Solve for the constant k in Python ---
# Area = 0.5 * |k| * |k/5| = 5 => k^2 = 50
k1 = np.sqrt(50)
k2 = -np.sqrt(50)

# --- 2. Set up data for plotting ---
x = np.linspace(-10, 10, 400)

# Original Line: 5x - y + 1 = 0  =>  y = 5x + 1
y_original = 5 * x + 1

# Solution Line 1 (L1): x + 5y = k1  =>  y = (-x + k1) / 5
y_L1 = (-x + k1) / 5

# Solution Line 2 (L2): x + 5y = k2  =>  y = (-x + k2) / 5
y_L2 = (-x + k2) / 5

# --- 3. Create the plot ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the three lines
ax.plot(x, y_original, color='red', linestyle='--', label='Original Line: $5x - y + 1 = 0$')
ax.plot(x, y_L1, color='blue', label=f'Line L1: $x + 5y - {k1:.2f} = 0$')
ax.plot(x, y_L2, color='green', label=f'Line L2: $x + 5y - {k2:.2f} = 0$')

# --- 4. Shade the area of the triangles ---
# Triangle 1 vertices: (0,0), (k1, 0), (0, k1/5)
ax.fill_between([0, k1], [0, 0], [k1/5, 0], color='blue', alpha=0.2, label='Triangle 1 (Area = 5)')
# Triangle 2 vertices: (0,0), (k2, 0), (0, k2/5)
ax.fill_between([k2, 0], [0, 0], [0, k2/5], color='green', alpha=0.2, label='Triangle 2 (Area = 5)')

# --- 5. Customize and show the plot ---
ax.set_title("Perpendicular Lines Forming Triangles of Area 5", fontsize=16)
ax.set_xlabel("x-axis", fontsize=12)
ax.set_ylabel("y-axis", fontsize=12)
ax.axhline(0, color='black', linewidth=0.7)
ax.axvline(0, color='black', linewidth=0.7)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True, which='both', linestyle=':', linewidth=0.7)
ax.set_aspect('equal', adjustable='box')
ax.legend()

plt.show()
