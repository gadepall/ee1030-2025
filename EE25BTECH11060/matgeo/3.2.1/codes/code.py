import matplotlib.pyplot as plt

# Define vertices
A = (0, 0)
B = (4, 0)
C = (7.625, 4.781)

# Collect coordinates (close the triangle by repeating A at the end)
x_coords = [A[0], B[0], C[0], A[0]]
y_coords = [A[1], B[1], C[1], A[1]]

# Plot the triangle
plt.figure(figsize=(6,6))
plt.plot(x_coords, y_coords, 'b-', linewidth=2)      # Triangle edges
plt.fill(x_coords, y_coords, 'skyblue', alpha=0.3)   # Fill inside

# Plot vertices
plt.scatter(*A, color='red', s=60)
plt.scatter(*B, color='green', s=60)
plt.scatter(*C, color='purple', s=60)

# Label points
plt.text(A[0]-0.3, A[1]-0.3, 'A', fontsize=12, fontweight='bold')
plt.text(B[0]+0.2, B[1]-0.3, 'B', fontsize=12, fontweight='bold')
plt.text(C[0]+0.2, C[1]+0.2, 'C', fontsize=12, fontweight='bold')

# Formatting
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Triangle ABC")
plt.grid(True)
plt.show()

