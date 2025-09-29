import numpy as np
import matplotlib.pyplot as plt

# Parameters
theta = np.pi / 4       # 45 degrees
alpha = np.pi / 6       # 30 degrees

# Vector P
P = np.array([np.cos(theta), np.sin(theta)])

# Clockwise rotation matrix by alpha
R = np.array([[np.cos(alpha), np.sin(alpha)],
              [-np.sin(alpha), np.cos(alpha)]])

# Vector Q
Q = R @ P

# Plot setup
plt.figure(figsize=(6,6))
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Draw X and Y axes
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Compute max range for good visibility
max_val = max(np.linalg.norm(P), np.linalg.norm(Q)) + 0.3
plt.xlim(-max_val, max_val)
plt.ylim(-max_val, max_val)

# Plot origin
plt.plot(0, 0, 'ko')

# Plot vectors P and Q
plt.quiver(0, 0, P[0], P[1], angles='xy', scale_units='xy', scale=1, color='blue', label=r'$\mathbf{P}$')
plt.quiver(0, 0, Q[0], Q[1], angles='xy', scale_units='xy', scale=1, color='red', label=r'$\mathbf{Q}$')

# Plot correct rotation arc from theta to theta - alpha
arc_theta = np.linspace(theta, theta - alpha, 100)
arc_x = 0.5 * np.cos(arc_theta)
arc_y = 0.5 * np.sin(arc_theta)
plt.plot(arc_x, arc_y, 'green', linestyle='--', label=r'Rotation by $\alpha$')

# Add text annotation for angle alpha
angle_deg = np.degrees(alpha)
text_angle_x = 0.5 * np.cos(theta - alpha / 2)
text_angle_y = 0.5 * np.sin(theta - alpha / 2)
plt.text(text_angle_x, text_angle_y, f'{angle_deg:.1f}°', fontsize=12, color='green')

# Labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.savefig('1.png')
plt.show()

