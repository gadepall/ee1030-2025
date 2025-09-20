import numpy as np
import matplotlib.pyplot as plt

# Given vectors
a = np.array([1, 1, 1])
b = np.array([0, 1, -1])

# Computed vector c from the solution
c = np.array([5/3, 2/3, 2/3])

# Check dot product condition
dot_ac = np.dot(a, c)
print(f"a · c = {dot_ac} (should be 3)")

# Check cross product condition
cross_ac = np.cross(a, c)
print(f"a × c = {cross_ac} (should be {b})")

# Verify if cross product approximately equals b (allow small numerical error)
if np.allclose(cross_ac, b, atol=1e-9):
    print("Cross product condition holds: a × c ≈ b")
else:
    print("Cross product condition does NOT hold!")

# Verify dot product condition
if np.isclose(dot_ac, 3, atol=1e-9):
    print("Dot product condition holds: a · c = 3")
else:
    print("Dot product condition does NOT hold!")

# Plotting setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

origin = np.zeros(3)

# Plot vectors from origin
ax.quiver(*origin, *a, color='r', label='a')
ax.quiver(*origin, *b, color='g', label='b')
ax.quiver(*origin, *c, color='b', label='c')

# Set plot limits
lims = [-1, 2]
ax.set_xlim(lims)
ax.set_ylim(lims)
ax.set_zlim(lims)

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vectors a, b, and c')

ax.legend()
plt.show()

