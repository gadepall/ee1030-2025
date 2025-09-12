import matplotlib.pyplot as plt

# Coordinates of the vertices
B = (0, 0)
C = (12, 0)
A = (0, 5)

# Extract x and y coordinates
x_coords = [A[0], B[0], C[0], A[0]]
y_coords = [A[1], B[1], C[1], A[1]]

# Plot triangle
plt.figure(figsize=(6,6))
plt.plot(x_coords, y_coords, 'b-', linewidth=2)
plt.fill(x_coords, y_coords, 'lightblue', alpha=0.5)

# Mark vertices
for point, name in zip([A, B, C], ['A', 'B', 'C']):
    plt.text(point[0], point[1]+0.3, name, fontsize=12, ha='center')
    plt.plot(point[0], point[1], 'ro')

# Right angle marker at B
plt.plot([0, 0.5, 0.5, 0], [0, 0, 0.5, 0.5], 'k-')

# Axes setup
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-1, 13)
plt.ylim(-1, 7)
plt.xlabel('x-axis (cm)')
plt.ylabel('y-axis (cm)')
plt.title('Right Triangle ABC')
plt.grid(True)
plt.savefig("/sdcard/matrix/ee1030-2025/ai25btech11016/matgeo/3.2.32/figs/3.2.32.png")
plt.show()