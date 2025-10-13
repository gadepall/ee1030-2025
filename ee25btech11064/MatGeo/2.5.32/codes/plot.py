import matplotlib.pyplot as plt
import numpy as np

# Points A(7,10), B(-2,5), C(3,4)
A = np.array([7, 10])
B = np.array([-2, 5])
C = np.array([3, 4])

# Function to calculate distance between two points
def distance(p1, p2):
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Calculate distances
AB = distance(A, B)
BC = distance(B, C)
CA = distance(C, A)

# Plotting the triangle
plt.figure(figsize=(6, 6))
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label="AB")
plt.plot([B[0], C[0]], [B[1], C[1]], 'b-', label="BC")
plt.plot([C[0], A[0]], [C[1], A[1]], 'b-', label="CA")

# Annotating points
plt.text(A[0], A[1], 'A(7,10)', fontsize=12, ha='right', va='bottom')
plt.text(B[0], B[1], 'B(-2,5)', fontsize=12, ha='right', va='top')
plt.text(C[0], C[1] - 0.2, 'C(3,4)', fontsize=12, ha='center', va='top')

# Highlighting the vertices
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='red')

# Displaying distances on the plot with offset adjustments
mid_AB = (A + B) / 2
mid_BC = (B + C) / 2
mid_CA = (C + A) / 2

# Adjusting text placement for better spacing
plt.text(mid_AB[0], mid_AB[1] + 0.6, f'{AB:.2f}', fontsize=12, color='blue', ha='center')
plt.text(mid_BC[0], mid_BC[1] - 0.6, f'{BC:.2f}', fontsize=12, color='blue', ha='center')
plt.text(mid_CA[0], mid_CA[1] - 1.3, f'{CA:.2f}', fontsize=12, color='blue', ha='center')

# Setting plot limits and labels
plt.xlim(-5, 10)
plt.ylim(0, 12)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Triangle Check')

# Show the plot
plt.grid(True)
plt.show()

