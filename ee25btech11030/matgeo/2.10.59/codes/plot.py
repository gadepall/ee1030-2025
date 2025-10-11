import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import os # Import os to check for directory

# --- Ctypes setup to interface with the C library ---

# Define the Vector structure in Python, ensuring it mirrors the C struct
class Vector(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# Load the compiled shared library (.so file)
try:
    vector_lib = ctypes.CDLL('./plot.so')
    # Define the C function's signature for ctypes
    vector_lib.calculate_ad_prime.argtypes = [Vector, Vector]
    vector_lib.calculate_ad_prime.restype = Vector
except OSError as e:
    print("Error: Could not load 'plot.so'.")
    print("Please compile 'plot.c' first using: gcc -shared -o plot.so -fPIC plot.c")
    exit()


# --- Helper function to draw angle arcs in 3D ---
def draw_angle_arc(ax, center, v1, v2, radius, color, label, label_pos_factor=1.3):
    """Draws an arc between two vectors in 3D space."""
    v1_u = v1 / np.linalg.norm(v1)
    v2_u = v2 / np.linalg.norm(v2)
    
    angle = np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
    
    axis = np.cross(v1_u, v2_u)
    if np.linalg.norm(axis) < 1e-6: return
    axis_u = axis / np.linalg.norm(axis)
    
    t = np.linspace(0, angle, 50)
    arc_points = np.array([
        center + radius * (np.cos(ti) * v1_u + np.sin(ti) * np.cross(axis_u, v1_u) + (1 - np.cos(ti)) * np.dot(axis_u, v1_u) * axis_u)
        for ti in t
    ])
    
    ax.plot(arc_points[:, 0], arc_points[:, 1], arc_points[:, 2], color=color, linewidth=2)
    
    mid_angle = angle / 2
    label_vec = (np.cos(mid_angle) * v1_u + np.sin(mid_angle) * np.cross(axis_u, v1_u) + (1 - np.cos(mid_angle)) * np.dot(axis_u, v1_u) * axis_u)
    label_pos = center + label_pos_factor * radius * label_vec
    ax.text(label_pos[0], label_pos[1], label_pos[2], label, color=color, fontsize=16, ha='center', va='center')


# --- Main Logic ---

# Define the vectors from the problem
O = np.array([0, 0, 0])
AB = np.array([2, 10, 11])
AD = np.array([-1, 2, 2])

# Use the C library to calculate AD'
ab_c = Vector(*AB)
ad_c = Vector(*AD)
ad_prime_c = vector_lib.calculate_ad_prime(ab_c, ad_c)
AD_prime = np.array([ad_prime_c.x, ad_prime_c.y, ad_prime_c.z])

# Calculate the fourth vertex of the parallelogram
C = AB + AD

# --- Plotting ---

fig = plt.figure(figsize=(13, 11))
ax = fig.add_subplot(111, projection='3d')
fig.patch.set_facecolor('white')
ax.set_facecolor('#f0f0f0')

ax.quiver(O[0], O[1], O[2], AB[0], AB[1], AB[2], color='r', arrow_length_ratio=0.08, label='AB', linewidth=2)
ax.quiver(O[0], O[1], O[2], AD[0], AD[1], AD[2], color='b', arrow_length_ratio=0.15, label='AD', linewidth=2)
ax.quiver(O[0], O[1], O[2], AD_prime[0], AD_prime[1], AD_prime[2], color='g', linestyle='--', arrow_length_ratio=0.15, label="AD' (rotated)", linewidth=2)

verts = [O, AB, C, AD]
ax.add_collection3d(Poly3DCollection([verts], facecolors='cyan', linewidths=1.5, edgecolors='k', alpha=.25))

draw_angle_arc(ax, O, AD, AB, 3.0, 'purple', 'θ')
draw_angle_arc(ax, O, AD, AD_prime, 2.5, 'orange', 'α')

v_ab_u = AB / np.linalg.norm(AB)
v_ad_prime_u = AD_prime / np.linalg.norm(AD_prime)
p1 = 2.0 * v_ab_u
p2 = 2.0 * (v_ab_u + v_ad_prime_u)
p3 = 2.0 * v_ad_prime_u
ax.plot([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], [p1[2], p2[2], p3[2]], color='g', linewidth=2)

ax.set_xlabel('X axis', fontsize=12, fontweight='bold')
ax.set_ylabel('Y axis', fontsize=12, fontweight='bold')
ax.set_zlabel('Z axis', fontsize=12, fontweight='bold')
ax.legend(fontsize=11)

max_limit = max(np.linalg.norm(AB), np.linalg.norm(C)) * 1.1
ax.set_xlim([-max_limit, max_limit])
ax.set_ylim([-max_limit, max_limit])
ax.set_zlim([-max_limit, max_limit])

ax.view_init(elev=1, azim=86)
plt.tight_layout()

# Create 'figs' directory if it doesn't exist
if not os.path.exists('figs'):
    os.makedirs('figs')
# CORRECTED typo from .savefigs to .savefig
plt.savefig('figs/plot.png')

plt.show()
