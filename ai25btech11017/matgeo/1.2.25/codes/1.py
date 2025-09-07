import matplotlib.pyplot as plt
import numpy as np

# Given data
boat_speed = 26  # km/h
current_speed = 11  # km/h
angle_current = 61  # degrees east of south

# Convert angle to radians
theta = np.radians(angle_current)

# Velocity components
# Boat moving north → along positive y-axis
v_boat = np.array([1, boat_speed, 0])  # (x, y, z)

# Current direction: 60° east of south means south is -y, east is +x
v_current = np.array([current_speed * np.sin(theta),
                      -current_speed * np.cos(theta),
                      0])

# Resultant velocity
v_resultant = v_boat + v_current

# Plotting
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Origin
origin = np.array([[0, 0, 0]])

# Plot vectors
ax.quiver(*origin[0], *v_boat, color='b', label='Boat (North 25 km/h)', arrow_length_ratio=0.1)
ax.quiver(*origin[0], *v_current, color='g', label='Current (10 km/h, 60° E of S)', arrow_length_ratio=0.1)
ax.quiver(*origin[0], *v_resultant, color='r', label='Resultant Velocity', arrow_length_ratio=0.1)

# Axis limits
ax.set_xlim(0, 15)
ax.set_ylim(-30, 30)
ax.set_zlim(0, 5)

# Labels
ax.set_xlabel('East (X-axis)')
ax.set_ylabel('North (Y-axis)')
ax.set_zlabel('Z-axis')

# Title and legend
ax.set_title('Resultant Velocity of Motorboat')
ax.legend()

# Save as image
plt.savefig("/home/balu/matgeo/figs/fig.png", dpi=300)

plt.show()
