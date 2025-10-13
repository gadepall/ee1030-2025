import numpy as np
import matplotlib.pyplot as plt

def line_gen_num(point1, point2, num_points):
    """
    Generates points along a line segment between two 3D points.
    """
    point1 = np.array(point1).flatten()
    point2 = np.array(point2).flatten()
    t = np.linspace(0, 1, num_points)
    points = np.outer(point1, (1-t)) + np.outer(point2, t)
    return points

def plot_3d_line(ax, point1, point2, label="", color="blue", linestyle="-"):
    """
    Plots a 3D line segment on a given matplotlib axis.
    """
    line_points = line_gen_num(point1, point2, 2)
    ax.plot(line_points[0], line_points[1], line_points[2], color=color, linestyle=linestyle, label=label)

# Given point P
P = np.array([2, 3, -8])

# Given line in symmetric form: (4-x)/2 = y/6 = (1-z)/3
# Rewrite in standard form: (x-4)/(-2) = (y-0)/6 = (z-1)/(-3)
# This means the line passes through point A = (4, 0, 1) and has direction vector d = (-2, 6, -3)
A_line = np.array([4, 0, 1])
d_line = np.array([-2, 6, -3])

# The foot of the perpendicular M on the line can be represented as:
# M = A_line + t * d_line = (4 - 2t, 6t, 1 - 3t)

# The vector PM is perpendicular to the direction vector d_line
# PM = M - P = (4 - 2t - 2, 6t - 3, 1 - 3t - (-8))
# PM = (2 - 2t, 6t - 3, 9 - 3t)

# The dot product of PM and d_line must be zero: PM . d_line = 0

# Calculate the coordinates of the foot of the perpendicular M
t_val = 1
M = A_line + t_val * d_line
M = np.array([4 - 2 * t_val, 6 * t_val, 1 - 3 * t_val])
print(f"The foot of the perpendicular is M = ({M[0]}, {M[1]}, {M[2]})")

# Calculate the perpendicular distance from P to the line
perpendicular_distance = np.linalg.norm(P - M)
print(f"The perpendicular distance from P0 to the line is = {perpendicular_distance:.2f}")

# --- Plotting the 3D scene ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the given point P
ax.scatter(P[0], P[1], P[2], color='black', s=100, label=f'Point P({P[0]},{P[1]},{P[2]})')
ax.text(P[0], P[1], P[2] + 0.5, '  P  ', color='black')

# Plot the foot of the perpendicular M
ax.scatter(M[0], M[1], M[2], color='green', s=100, label=f'Foot of Perpendicular M({M[0]},{M[1]},{M[2]})')
ax.text(M[0], M[1], M[2] + 0.5, '  M  ', color='green')

# Plot the line 
# We have A_line and M is also on the line. Pick another point using t = 0 (A_line) and t = 2
point_on_line_1 = A_line
point_on_line_2 = A_line + 2 * d_line # Another point on the line

line_points_for_plot = np.array([
    A_line,
    A_line + 5 * d_line,
    A_line - 5 * d_line
])

ax.plot(line_points_for_plot[:,0], line_points_for_plot[:,1], line_points_for_plot[:,2], color='blue', label='Line')

# Plot the perpendicular line segment PM
plot_3d_line(ax, P, M, label='Perpendicular PM', color='purple', linestyle='--')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Foot of Perpendicular and Perpendicular Distance')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("fig2.png")
plt.show()

print("3D plot saved as fig2.png")
