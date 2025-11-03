import numpy as np
import matplotlib.pyplot as plt

# --- Create a single figure and axis for the plot ---
fig, ax = plt.subplots(figsize=(11, 11))

# --- Plot shared elements ---
# The line L (y = -x) is the same for both cases
ax.plot([-10, 10], [10, -10], 'r-', linewidth=1.5, label='Line L (y=-x)', zorder=0)

# Lists to collect points for setting axis limits later
all_x, all_y = [], []

# --- Loop through the two edge cases ---
# (a_value, color, line_style)
cases = [(2.0, 'blue', '-'), (-2.0, 'green', '--')]

for a, color, style in cases:
    sqrt2 = np.sqrt(2)
    
    # --- Calculations for the given 'a' ---
    c_center = 0.25 * np.array([1 + sqrt2 * a, 1 - sqrt2 * a])
    c_radius = np.linalg.norm(c_center)
    P = 2 * c_center
    m_center = (P + c_center) / 2.0
    m_radius = np.linalg.norm(P - c_center) / 2.0
    
    # Calculate the single tangent midpoint
    quad_a = 2.0
    quad_b = 2.0 * (m_center[1] - m_center[0])
    x_m = -quad_b / (2 * quad_a)
    M = np.array([x_m, -x_m])
    
    # Store points to adjust plot limits later
    all_x.extend([P[0], c_center[0], M[0]])
    all_y.extend([P[1], c_center[1], M[1]])
    
    # --- Plotting for this 'a' value ---
    
    # Plot the main circle C
    circle_C = plt.Circle(c_center, c_radius, color=color, fill=False, lw=2, ls=style, label=f'Circle C (a={a})')
    ax.add_patch(circle_C)
    
    # Plot the locus of midpoints
    circle_M_locus = plt.Circle(m_center, m_radius, color='gray', fill=False, lw=1.5, ls=style, label=f'Locus of Midpoints (a={a})')
    ax.add_patch(circle_M_locus)
    
    # Plot the single chord
    ax.plot([P[0], M[0]], [P[1], M[1]], color=color, ls=style, lw=1, label=f'Single Chord (a={a})')
    
    # Plot key points, making them distinct for each case
    ax.plot(P[0], P[1], 'o', color=color, markersize=8)
    ax.text(P[0], P[1] + 0.2, f'P(a={a})', color=color, ha='center', fontsize=12)
    
    ax.plot(c_center[0], c_center[1], 'x', color=color, markersize=8, mew=2)
    ax.text(c_center[0], c_center[1] - 0.3, f'C(a={a})', color=color, ha='center', fontsize=12)
    
    # The midpoint is the same point of tangency for both cases
    ax.plot(M[0], M[1], 'o', markersize=10, color='orange', markeredgecolor='black', label='Single Midpoint (Tangent)' if a==2.0 else "")


# --- Final Plot Properties ---
ax.set_title('Overlay of Edge Cases: a = 2 and a = -2', fontsize=16)
ax.set_xlabel('x-axis', fontsize=12)
ax.set_ylabel('y-axis', fontsize=12)
ax.grid(True)

# Consolidate legends
handles, labels = ax.get_legend_handles_labels()
unique = dict(zip(labels, handles))
ax.legend(unique.values(), unique.keys(), loc='best')

ax.set_aspect('equal', adjustable='box')
ax.set_xlim(min(all_x) - 1, max(all_x) + 1)
ax.set_ylim(min(all_y) - 1, max(all_y) + 1)

plt.savefig('fig.png')
plt.show()
