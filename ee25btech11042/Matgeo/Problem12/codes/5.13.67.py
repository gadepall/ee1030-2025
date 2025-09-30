import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the value of k for a non-trivial solution
k = 33/2

# Define the equations of the planes:
# P1: x + ky + 3z = 0   => z = (-x - ky) / 3
# P2: 3x + ky - 2z = 0  => z = (3x + ky) / 2
# P3: 2x + 3y - 4z = 0  => z = (2x + 3y) / 4

# Create a meshgrid for x and y values
x_vals = np.linspace(-5, 5, 50)
y_vals = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x_vals, y_vals)

# Calculate Z values for each plane
Z1 = (-X - k * Y) / 3
Z2 = (3 * X + k * Y) / 2
Z3 = (2 * X + 3 * Y) / 4

# Setup the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the three planes
ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100, color='skyblue', label='Plane 1')
ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100, color='lightcoral', label='Plane 2')
ax.plot_surface(X, Y, Z3, alpha=0.5, rstride=100, cstride=100, color='lightgreen', label='Plane 3')

# --- Plot the line of intersection ---
# To find the line of intersection for a homogeneous system, we need to find the null space
# of the coefficient matrix with k = 33/2.
# Let's find one vector in the null space.
# We can represent the system as:
# x + (33/2)y + 3z = 0
# 3x + (33/2)y - 2z = 0
# 2x + 3y - 4z = 0

# If we set, for instance, x=6 (to clear fractions and get nice numbers)
# 6 + (33/2)y + 3z = 0  => 12 + 33y + 6z = 0  => 4 + 11y + 2z = 0 (Eq A)
# 18 + (33/2)y - 2z = 0 => 36 + 33y - 4z = 0 (Eq B)
# 12 + 3y - 4z = 0      => 3y - 4z = -12 (Eq C)

# From (Eq A): 2z = -4 - 11y
# Substitute 2z into (Eq B): 36 + 33y - 2(-4 - 11y) = 0
# 36 + 33y + 8 + 22y = 0
# 44 + 55y = 0 => 55y = -44 => y = -44/55 = -4/5

# Now find z using y = -4/5 in Eq A:
# 4 + 11(-4/5) + 2z = 0
# 4 - 44/5 + 2z = 0
# (20 - 44)/5 + 2z = 0
# -24/5 + 2z = 0 => 2z = 24/5 => z = 12/5

# So, one point on the line is (6, -4/5, 12/5).
# The vector direction is proportional to (6, -4/5, 12/5).
# For integer components, multiply by 5: (30, -4, 12).
# Divide by 2: (15, -2, 6).
# Let's verify this vector (15, -2, 6) with the original equations:
# 1(15) + (33/2)(-2) + 3(6) = 15 - 33 + 18 = 0 (Correct)
# 3(15) + (33/2)(-2) - 2(6) = 45 - 33 - 12 = 0 (Correct)
# 2(15) + 3(-2) - 4(6) = 30 - 6 - 24 = 0 (Correct)

# The direction vector of the line of intersection is `v = (15, -2, 6)`
# The line passes through the origin (0,0,0).
t = np.linspace(-5, 5, 100) # Parameter for the line
line_x = 15 * t
line_y = -2 * t
line_z = 6 * t

ax.plot(line_x, line_y, line_z, color='purple', linewidth=3, label='Line of Intersection')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title(f'Intersection of Three Planes when k = {k} (Line of Solutions)')
ax.legend(['Plane 1: $x + {:.1f}y + 3z = 0$'.format(k),
           'Plane 2: $3x + {:.1f}y - 2z = 0$'.format(k),
           'Plane 3: $2x + 3y - 4z = 0$',
           'Line of Intersection'])

# Adjust view for better visibility
ax.view_init(elev=20, azim=-45) # You can adjust these angles

plt.grid(True)
plt.show()
