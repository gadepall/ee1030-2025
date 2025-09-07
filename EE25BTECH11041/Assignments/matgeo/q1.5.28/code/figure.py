import matplotlib.pyplot as plt
import numpy as np

# --- Function Definition (similar to the C code) ---
# This function calculates the coordinates (a, b) of a point that divides
# the line segment from (x1, y1) to (x2, y2) in the ratio k:1.
# This is derived from the section formula: (n*x1 + m*x2)/(m+n)
# by setting the ratio as k = m/n.
def trisec(k, x1, y1, x2, y2):
    """
    Calculates the coordinates of a point dividing a line segment.
    
    Args:
        k (float): The ratio m/n for the section formula.
        x1, y1 (float): Coordinates of the first point (A).
        x2, y2 (float): Coordinates of the second point (B).
        
    Returns:
        tuple: A tuple containing the (x, y) coordinates of the dividing point.
    """
    a = (x1 + k * x2) / (1 + k)
    b = (y1 + k * y2) / (1 + k)
    return (a, b)

# --- Problem Setup ---
# Given points for the line segment
A = (7, -2)
B = (1, -5)

# --- Calculations ---
# The points of trisection divide the segment in ratios 1:2 and 2:1.

# 1. Calculate Point P (divides AB in ratio 1:2)
# Here, m=1, n=2, so k = m/n = 1/2 = 0.5
k_p = 0.5
P_calculated = trisec(k_p, A[0], A[1], B[0], B[1])

# 2. Calculate Point Q (divides AB in ratio 2:1)
# Here, m=2, n=1, so k = m/n = 2/1 = 2.0
k_q = 2.0
Q_calculated = trisec(k_q, A[0], A[1], B[0], B[1])

# Extract the y-coordinate for the answer
y_solution = Q_calculated[1]

# --- Output the Results to Console ---
print("--- Trisection Calculation ---")
print(f"Point A: {A}")
print(f"Point B: {B}\n")

print(f"Calculated coordinates for P (ratio 1:2, k={k_p}): {P_calculated}")
print(f"Calculated coordinates for Q (ratio 2:1, k={k_q}): {Q_calculated}\n")

print("--- Solution ---")
print(f"The problem states Q is (3, y). Our calculation gives Q as {Q_calculated}.")
print(f"Therefore, the value of y is {int(y_solution)}.")


# --- Plotting the Figure ---
plt.figure(figsize=(10, 8))
ax = plt.gca()

# Plot the main line segment
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label='Line Segment AB', zorder=1)

# Plot the points and their labels
points = {'A': A, 'B': B, 'P': P_calculated, 'Q': Q_calculated}
colors = {'A': 'red', 'B': 'red', 'P': 'green', 'Q': 'green'}
for name, (px, py) in points.items():
    plt.scatter(px, py, color=colors[name], s=100, zorder=2)
    plt.text(px + 0.1, py + 0.1, f'{name}({px:.1f}, {py:.1f})', fontsize=12)

# --- Styling the Plot ---
plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)
ax.set_aspect('equal', adjustable='box')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlim(0, 8)
plt.ylim(-6, 0)
# The line ax.invert_yaxis() has been removed to show the negative y-axis below the origin.

# Save the figure as a PNG file
plt.savefig('trisection_diagram.png')
print("\nDiagram saved as 'trisection_diagram.png'")

# Display the plot
plt.show()
