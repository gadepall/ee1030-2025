import numpy as np
import matplotlib.pyplot as plt

def get_circle_properties(G, H, K):
    center = np.array([-G/2, -H/2])
    radius = np.sqrt(center[0]**2 + center[1]**2 - K)
    return center, radius

# --- Numerical Inputs are defined here in Python ---
# Circle 1: x^2 + y^2 - 2x - 4y - 20 = 0
G1, H1, K1 = -2.0, -4.0, -20.0
# Point of Tangency
p = np.array([5.0, 5.0])
# Radius of the new circle (Circle 2)
r2 = 5.0
# --------------------------------------------------

# --- Calculations ---
c1, r1 = get_circle_properties(G1, H1, K1)
m = p - c1
m_hat = m / np.linalg.norm(m)
c2 = p + r2 * m_hat

# --- Plotting ---
fig, ax = plt.subplots(figsize=(8, 8))
circle1 = plt.Circle(c1, r1, fill=False, edgecolor='gray', linestyle='--')
circle2 = plt.Circle(c2, r2, fill=False, edgecolor='gray', linestyle='-')
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.plot([c1[0], c2[0]], [c1[1], c2[1]], 'b-', label='Line of Centers')
ax.plot(c1[0], c1[1], 'ro', markersize=10, label=f'C1({c1[0]:.2f}, {c1[1]:.2f})')
ax.plot(c2[0], c2[1], 'go', markersize=10, label=f'C2({c2[0]:.2f}, {c2[1]:.2f})')
ax.plot(p[0], p[1], 'm*', markersize=15, label=f'P({p[0]:.2f}, {p[1]:.2f})')
ax.set_title('Figure')
ax.grid(True)
ax.axis('equal')
ax.legend()
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/7.4.34/figs/figure1.png")
plt.show()
