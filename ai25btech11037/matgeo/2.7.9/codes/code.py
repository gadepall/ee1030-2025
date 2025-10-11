import matplotlib.pyplot as plt
import numpy as np

# Vertices
P = np.array([1, 0])
Q = np.array([2, 2])
R = np.array([3, 1])

# Function to compute area using determinant formula
def triangle_area(A, B, C):
    return 0.5 * abs(A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[1]-B[1]))

# Compute area
area = triangle_area(P, Q, R)
print("Area of triangle:", area)

# Plotting
x = [P[0], Q[0], R[0], P[0]]  # closing the triangle
y = [P[1], Q[1], R[1], P[1]]

plt.figure(figsize=(6,6))
plt.plot(x, y, 'b-o', linewidth=2)  # triangle edges
plt.fill(x, y, 'skyblue', alpha=0.5)  # fill triangle

# Mark vertices
plt.text(P[0], P[1]-0.2, "P(1,0)", fontsize=12, ha="center")
plt.text(Q[0], Q[1]+0.2, "Q(2,2)", fontsize=12, ha="center")
plt.text(R[0], R[1]-0.2, "R(3,1)", fontsize=12, ha="center")

# Display area on plot
plt.title(f"Triangle PQR, Area = {area}")
plt.axis("equal")
plt.grid(True)

# Save figure
plt.savefig("triangle_area.png", dpi=300)
plt.show()
