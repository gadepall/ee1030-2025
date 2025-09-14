import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import art3d

# --- Create the Figure ---
fig = plt.figure(figsize=(16, 14))
ax = fig.add_subplot(111, projection='3d')

# --- Generate Grid and Define Boundaries ---
lim = 10
x_range = np.linspace(-lim, lim, 50)
y_range = np.linspace(-lim, lim, 50)
X, Y = np.meshgrid(x_range, y_range)

# --- AESTHETIC AND COLOR DEFINITIONS ---
# Define surface colors and darker corresponding outline colors
colors = {
    'P+':  {'surface': '#E57373', 'outline': '#C62828'}, # Light Red / Dark Red
    'P-':  {'surface': '#64B5F6', 'outline': '#1565C0'}, # Light Blue / Dark Blue
    'Π':   {'surface': '#81C784', 'outline': '#2E7D32'}, # Light Green / Dark Green
    'P':   {'surface': '#BDBDBD', 'outline': '#424242'}  # Light Grey / Dark Grey
}

# --- PLOTTING PLANES WITH SURFACES AND OUTLINES ---

# Function to plot a plane with its surface and a dark outline
def plot_complete_plane(Z, color_pair):
    # Plot the highly transparent surface
    ax.plot_surface(X, Y, Z, alpha=0.15, color=color_pair['surface'], rstride=5, cstride=5, edgecolor='none')
    
    # Plot a crisp, dark wireframe outline
    ax.plot_wireframe(X, Y, Z, color=color_pair['outline'], linewidth=1.2, rstride=100, cstride=100)

# 1. Plane Π: x + y + z = 7
Z_Pi = 7 - X - Y
plot_complete_plane(Z_Pi, colors['Π'])

# 2. Plane P+: 3x+2y+3z=18
Z_P_plus = (18 - 3*X - 2*Y) / 3
plot_complete_plane(Z_P_plus, colors['P+'])

# 3. Plane P-: 3x+2y+3z=14
Z_P_minus = (14 - 3*X - 2*Y) / 3
plot_complete_plane(Z_P_minus, colors['P-'])

# 4. Original Plane P: 3x+2y+3z=16
Z_P = (16 - 3*X - 2*Y) / 3
plot_complete_plane(Z_P, colors['P'])


# --- EMPHASIZE AND LABEL LINES/POINTS ---
FOREGROUND_ZORDER = 10
t_start, t_end = -15, 15
t_lines = np.linspace(t_start, t_end, 100)
d = np.array([1, 0, -1])  # Direction vector

# Line L1
a = np.array([0, 3, 4])
L1 = a + t_lines[:, np.newaxis] * d
ax.plot(L1[:, 0], L1[:, 1], L1[:, 2], color='#BF360C', lw=5, zorder=FOREGROUND_ZORDER) # Deep Orange

# Line L2
b = np.array([0, 7, 0])
L2 = b + t_lines[:, np.newaxis] * d
ax.plot(L2[:, 0], L2[:, 1], L2[:, 2], color='#0D47A1', lw=5, zorder=FOREGROUND_ZORDER) # Deep Blue

# Points u, v, w
point_size = 250
u, s = b, 4 * np.sqrt(2)
t_proj = np.dot(u - a, d) / np.dot(d, d)
M = a + t_proj * d
dist_M_v = s/2
v = M + (dist_M_v / np.linalg.norm(d)) * d
w = M - (dist_M_v / np.linalg.norm(d)) * d

ax.scatter([u[0],v[0],w[0]], [u[1],v[1],w[1]], [u[2],v[2],w[2]],
           color=['cyan','magenta','yellow'], s=point_size, ec='black', lw=1.5, zorder=FOREGROUND_ZORDER + 1)

# --- ADDING ALL LABELS (PLANES, LINES, AND POINTS) ---
# Plane Labels
plane_label_props = {'ha':'center', 'va':'center', 'fontsize':10, 'bbox':dict(facecolor='white', alpha=0.7, ec='none', pad=0.2)}
ax.text(-8,-8, 7-(-8)-(-8), " Π: x+y+z=7 ", color=colors['Π']['outline'], **plane_label_props)
ax.text(8, 8, (18-3*8-2*8)/3, " P+: 3x+2y+3z=18 ", color=colors['P+']['outline'], **plane_label_props)
ax.text(8,-8, (14-3*8-2*(-8))/3, " P-: 3x+2y+3z=14 ", color=colors['P-']['outline'], **plane_label_props)
ax.text(-8, 8, (16-3*(-8)-2*8)/3, " P: 3x+2y+3z=16 ", color=colors['P']['outline'], **plane_label_props)

# Line Endpoint Labels
line_label_props = {'ha':'center', 'va':'center', 'fontsize':14, 'fontweight':'bold'}
l1_start_pos = a + t_start * d
l2_start_pos = b + t_start * d
ax.text(l1_start_pos[0], l1_start_pos[1], l1_start_pos[2] + 1.5, "L1", color='#BF360C', **line_label_props)
ax.text(l2_start_pos[0] + 2, l2_start_pos[1], l2_start_pos[2] , "L2", color='#0D47A1', **line_label_props)

# Point Labels (u, v, w)
point_label_props = {'ha':'center', 'va':'bottom', 'fontsize':14, 'fontweight':'bold'}
ax.text(u[0], u[1], u[2] + 0.5, 'u', color='black', **point_label_props)
ax.text(v[0], v[1], v[2] + 0.5, 'v', color='black', **point_label_props)
ax.text(w[0], w[1], w[2] - 1.5, 'w', color='black', **point_label_props) # slight offset for w


# --- FINAL PLOT SETUP ---
ax.view_init(elev=28, azim=-55)
ax.set_xlim(-15, 15); ax.set_ylim(-15, 15); ax.set_zlim(-15, 15)
ax.set_xlabel('X-axis', fontsize=12); ax.set_ylabel('Y-axis', fontsize=12); ax.set_zlabel('Z-axis', fontsize=12)
ax.set_title('Final Geometric Construction with Full Labeling', fontsize=20, pad=20)

# Clean background
ax.xaxis.pane.fill=False; ax.yaxis.pane.fill=False; ax.zaxis.pane.fill=False
ax.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.savefig("../figs/fig5_.png")
plt.show()
