import matplotlib.pyplot as plt

# Given and calculated vertices
A = (3, 3)
B = (6, 4)
C = (8, 7)
D = (5, 6)

# Extract x and y coordinates
x_coords = [A[0], B[0], C[0], D[0], A[0]]
y_coords = [A[1], B[1], C[1], D[1], A[1]]

# Plotting
plt.figure(figsize=(6,6))
plt.plot(x_coords, y_coords, 'b-o', label='Parallelogram')

# Label the points
for point, name in zip([A, B, C, D], ['A', 'B', 'C', 'D']):
    plt.text(point[0] + 0.1, point[1] + 0.1, f'{name}{point}')

plt.title('Parallelogram with vertices A, B, C, D')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
