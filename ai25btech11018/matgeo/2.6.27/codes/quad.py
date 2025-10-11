import matplotlib.pyplot as plt

# Coordinates of the vertices
A = (-5, 7)
B = (-4, -5)
C = (-1, -6)
D = (4, 5)

# Extract x and y coordinates for plotting, closing the shape by returning to A
x = [A[0], B[0], C[0], D[0], A[0]]
y = [A[1], B[1], C[1], D[1], A[1]]

plt.figure(figsize=(8, 8))
plt.plot(x, y, 'b-o', label='Quadrilateral ABCD')

# Fill the quadrilateral for visualization
plt.fill(x, y, 'skyblue', alpha=0.4)

# Label the vertices
for point, label in zip([A, B, C, D], ['A', 'B', 'C', 'D']):
    plt.text(point[0], point[1], label, fontsize=12, fontweight='bold',
             ha='right', color='darkblue')

plt.title('Quadrilateral ABCD')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis('equal')
plt.tight_layout()

# Save the plot as PNG file
plt.savefig('quadrilateral_ABCD.png', dpi=200)
plt.close()

print('Plot saved as quadrilateral_ABCD.png')
