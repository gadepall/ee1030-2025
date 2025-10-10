import matplotlib.pyplot as plt

# Vertices of the triangle
A = (1, -1)
B = (-4, 6)
C = (-3, 5)

# Extract x and y coordinates for plotting
x_coords = [A[0], B[0], C[0], A[0]]  # repeat A to close the triangle
y_coords = [A[1], B[1], C[1], A[1]]

plt.figure()
plt.plot(x_coords, y_coords, 'b-', marker='o')  # Blue line with circle markers

# Annotate the points
plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
plt.text(B[0], B[1], 'B', fontsize=12, ha='right')
plt.text(C[0], C[1], 'C', fontsize=12, ha='right')

# Set equal scaling and grid
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)

plt.title('Triangle ABC')
plt.xlabel('x')
plt.ylabel('y')

# Save the plot as python_plot.png
plt.savefig('python_plot.png')

plt.show()
