import ctypes
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL('./libtriangle.so')

# Create array for coordinates
coords = (ctypes.c_double * 6)()

# Call C function
lib.get_triangle_coords(coords)

# Extract points
A = (coords[0], coords[1])
B = (coords[2], coords[3])
C = (coords[4], coords[5])

# Plot
x_coords = [A[0], B[0], C[0], A[0]]
y_coords = [A[1], B[1], C[1], A[1]]

plt.figure(figsize=(6,6))
plt.plot(x_coords, y_coords, 'b-', linewidth=2)
plt.fill(x_coords, y_coords, 'lightblue', alpha=0.5)

for point, name in zip([A, B, C], ['A', 'B', 'C']):
    plt.text(point[0], point[1]+0.3, name, fontsize=12, ha='center')
    plt.plot(point[0], point[1], 'ro')

plt.plot([0, 0.5, 0.5, 0], [0, 0, 0.5, 0.5], 'k-')  # right angle marker

plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-1, 13)
plt.ylim(-1, 7)
plt.title("Right Triangle ABC (from C function)")
plt.savefig("/sdcard/matrix/ee1030-2025/ai25btech11016/matgeo/3.2.32/figs/3.2.32.png")
plt.show()
