import numpy as np
import matplotlib.pyplot as plt

# Plane coefficients: 2x - 3y + 4z - 6 = 0
a, b, c, d = 2, -3, 4, -6

# Denominator
den = a*a + b*b + c*c

# Origin
origin = np.array([0.0, 0.0, 0.0])

# Foot of perpendicular from origin to plane
foot = np.array([
    -a*d/den,
    -b*d/den,
    -c*d/den
])

# Distance from origin to plane
distance = abs(d) / np.sqrt(den)

print("Foot of perpendicular:", foot)
print("Distance:", distance)

# Create grid for plane
grid_size = 3.0
num = 40
X = np.linspace(foot[0] - grid_size, foot[0] + grid_size, num)
Y = np.linspace(foot[1] - grid_size, foot[1] + grid_size, num)
X, Y = np.meshgrid(X, Y)
Z = (6 - 2*X + 3*Y) / 4.0   # from plane equation

# Plot
fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111, projection='3d')

# Plane
ax.plot_surface(X, Y, Z, alpha=0.5, color='orange')

# Origin and foot points
ax.scatter(*origin, color='red', s=80, label="Origin")
ax.scatter(*foot, color='blue', s=80, label="Foot of perpendicular")

 # Perpendicular line (distance line)
ax.plot(
    [origin[0], foot[0]],
    [origin[1], foot[1]],
    [origin[2], foot[2]],
    color='black', linewidth=4, linestyle='--',
    zorder=10, label=f"Distance = {distance:.2f}"
)       

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Plane 2x - 3y + 4z - 6 = 0 and Distance from Origin')

# Equal aspect ratio
max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
mid_x = (X.max()+X.min()) * 0.5
mid_y = (Y.max()+Y.min()) * 0.5
mid_z = (Z.max()+Z.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

# Legend
ax.legend()
plt.savefig("fig7.png") 
plt.show()