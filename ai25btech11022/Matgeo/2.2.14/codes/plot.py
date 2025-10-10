import numpy as np
import matplotlib.pyplot as plt

# Line data
P = np.array([5, -1, -4])   # point on line
d = np.array([2, -1, 1])    # line direction

# Plane data
n = np.array([3, -4, -1])   # normal to plane
d0 = -5                     # constant term in plane eqn

# Angle calculation
cos_angle = abs(np.dot(d, n)) / (np.linalg.norm(d) * np.linalg.norm(n))
theta = np.degrees(np.arcsin(cos_angle))
print("Angle between line and plane:", theta, "degrees")

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# --- Plot line ---
t = np.linspace(-5, 5, 100)
line = P.reshape(3,1) + t * d.reshape(3,1)
ax.plot(line[0], line[1], line[2], 'r', label="Line")

# --- Plot plane ---
xx, yy = np.meshgrid(range(0, 10), range(-10, 5))
zz = (-n[0]*xx - n[1]*yy - d0) / n[2]
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Angle between Line and Plane")

# Legend
ax.legend()

# --- Annotate angle in the plot ---
# Pick a point slightly above the starting point P
ax.text(P[0]+2, P[1]+2, P[2]+2, f"Angle = {theta:.2f}°", 
        color="black", fontsize=12, bbox=dict(facecolor='white', alpha=0.6))

plt.show()



















