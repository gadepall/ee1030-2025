import numpy as np
import matplotlib.pyplot as plt

# Plane: 2x - 4y + z = 7
# Line parametric: x = 4 + t, y = 2 + t, z = k + 2*t

# Normal vector of plane
n = np.array([2, -4, 1])

# Point on line: [4,2,k], direction: [1,1,2]
d = np.array([1,1,2])
p_line = np.array([4,2,0])  # initial guess k=0 (will solve next)

# Solve for k using matrix approach: n . (p_line + t*d) = 7 for all t => n . d = 0
# n . d = 2*1 -4*1 +1*2 = 0, so line is parallel to plane direction => check point
# n . p_line + k*1 = 7 => 2*4 -4*2 + k = 7 => 8-8+k=7 => k=7
k = 7
print("Value of k =", k)

# Updated line point with correct k
p_line = np.array([4,2,k])

# Create points along the line
t = np.linspace(-5,5,100)
x_line = p_line[0] + d[0]*t
y_line = p_line[1] + d[1]*t
z_line = p_line[2] + d[2]*t

# Create a meshgrid for the plane
xx, yy = np.meshgrid(np.linspace(-5,10,20), np.linspace(-5,10,20))
zz = 7 - 2*xx + 4*yy  # from plane equation: z = 7 -2x +4y

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plane
ax.plot_surface(xx, yy, zz, alpha=0.3, color='cyan', rstride=1, cstride=1)

# Line
ax.plot(x_line, y_line, z_line, color='red', linewidth=2, label='Line')

# Mark point on line
ax.scatter(*p_line, color='blue', s=50)
ax.text(*p_line, 'Point on line', color='blue')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.grid(True)

# Save figure
fig.savefig('../figs/fig.png', dpi=300)
plt.show()
