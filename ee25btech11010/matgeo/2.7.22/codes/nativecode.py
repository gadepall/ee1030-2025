import numpy as np
import matplotlib.pyplot as plt

# Triangle vertices
A = (5, 0)
B = (8, 0)
C = (8, 4)

# Extract x and y coordinates for plotting
x_coords = [A[0], B[0], C[0], A[0]]  # Close the triangle by returning to A
y_coords = [A[1], B[1], C[1], A[1]]

# Plot the triangle
plt.figure(figsize=(6,6))
plt.plot(x_coords, y_coords, 'bo-', label='Triangle')
plt.fill(x_coords, y_coords, 'skyblue', alpha=0.3)  # shaded area

# Label the points
plt.text(A[0], A[1]-0.3, 'A(5,0)', ha='center')
plt.text(B[0], B[1]-0.3, 'B(8,0)', ha='center')
plt.text(C[0]+0.2, C[1], 'C(8,4)', ha='center')

# Add grid, axis, and title
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Triangle with vertices A(5,0), B(8,0), C(8,4)\nArea = 6 sq. units')
plt.axis('equal')  # Equal scaling on both axes
plt.legend()
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/2.7.22/figs/q4.png")
plt.show()
