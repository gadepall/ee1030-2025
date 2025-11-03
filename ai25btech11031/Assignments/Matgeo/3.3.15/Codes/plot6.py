import matplotlib.pyplot as plt
import numpy as np

# Define B and C
B = np.array([0, 0])
C = np.array([7, 0])

# Midpoint D
D = (B + C) / 2

# Median circle parameters
radius_AD = 5

# Circle radius for angle condition
R = 7 / np.sqrt(3)

# Centres O1 and O2 of the angle-locus circles
O1 = D + np.array([0, R])
O2 = D - np.array([0, R])

# Function to find circle intersections
def circle_intersections(c1, r1, c2, r2):
    x1, y1 = c1
    x2, y2 = c2
    dx, dy = x2 - x1, y2 - y1
    d = np.hypot(dx, dy)
    if d > r1 + r2 or d < abs(r1 - r2) or d == 0:
        return []
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = np.sqrt(max(r1**2 - a**2, 0))
    xm = x1 + a * dx / d
    ym = y1 + a * dy / d
    rx = -dy * (h / d)
    ry = dx * (h / d)
    p1 = (xm + rx, ym + ry)
    p2 = (xm - rx, ym - ry)
    return [p1, p2]

# Find intersections (possible A points)
A_candidates = []
for O in [O1, O2]:
    intersections = circle_intersections(D, radius_AD, O, R)
    A_candidates.extend(intersections)

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))

# Plot base BC
ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=2, label='Base BC')

# Plot points B, C, D
ax.plot(B[0], B[1], 'ro', label='B(0,0)')
ax.plot(C[0], C[1], 'bo', label='C(7,0)')
ax.plot(D[0], D[1], 'go', label='D midpoint')

# Plot the circle with center D and radius 5 (median circle)
theta = np.linspace(0, 2*np.pi, 400)
ax.plot(D[0] + radius_AD*np.cos(theta), D[1] + radius_AD*np.sin(theta),
        'g:', lw=2, alpha=0.8, label='Circle (D,5)')

# Plot all possible triangles
for i, A in enumerate(A_candidates, 1):
    A = np.array(A)
    ax.plot(A[0], A[1], 'ms', label=f'A{i}')
    ax.plot([A[0], B[0]], [A[1], B[1]], 'm-')
    ax.plot([A[0], C[0]], [A[1], C[1]], 'm-')
    ax.plot([A[0], D[0]], [A[1], D[1]], 'm--', alpha=0.7)  # Median

# Formatting
ax.set_aspect('equal', 'box')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('All possible triangles ABC with ∠A=60°, BC=7 and AD=5')
ax.legend(loc='upper right')   # Legend at the corner
ax.grid(True)

# Save the figure
plt.savefig("fig6.png", dpi=300, bbox_inches='tight')
plt.show()

