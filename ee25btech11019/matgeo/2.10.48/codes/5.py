import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./5.so')

# Define output array
b = (ctypes.c_double * 3)()
lib.find_b(b)

# Extract b components
bx, by, bz = b[0], b[1], b[2]
print(f"Vector b = ({bx}, {by}, {bz})")

# Define vector a
a = np.array([1, 1, 1])
b_vec = np.array([bx, by, bz])

# Origin
O = np.array([0, 0, 0])

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors
ax.quiver(O[0], O[1], O[2], a[0], a[1], a[2], color='r', label='a = i+j+k')
ax.quiver(O[0], O[1], O[2], b_vec[0], b_vec[1], b_vec[2], color='b', label='b')

# Label endpoints with coordinates
points = {
    'O': O,
    'A (1,1,1)': a,
    f'B ({bx:.0f},{by:.0f},{bz:.0f})': b_vec
}
for label, coord in points.items():
    ax.text(coord[0], coord[1], coord[2],
            f'{label}',
            fontsize=10, ha='center')

# Axes limits and labels
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_zlim([0, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title("Vectors a and b with coordinates")

plt.show()
