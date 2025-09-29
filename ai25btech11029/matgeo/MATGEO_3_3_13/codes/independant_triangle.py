import matplotlib.pyplot as plt


# Extract coordinates
A = (-2.574, -2.574)
B = (0, 0)
C = (7, 0)

# Plot triangle
x = [A[0], B[0], C[0], A[0]]
y = [A[1], B[1], C[1], A[1]]

plt.figure(figsize=(6,6))
plt.plot(x, y, 'bo-')
plt.text(*A, 'A', fontsize=12, ha='right')
plt.text(*B, 'B', fontsize=12, ha='right')
plt.text(*C, 'C', fontsize=12, ha='left')
plt.grid(True)
plt.axis('equal')
plt.title('Triangle ABC with BC = 7 cm, ∠B = 45°, ∠C = 60°')
plt.show()

