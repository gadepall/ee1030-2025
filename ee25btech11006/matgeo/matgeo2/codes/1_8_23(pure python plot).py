import matplotlib.pyplot as plt

# Points
A = (2, -4)
P = (3, 8)
Q1 = (-10, -5)
Q2 = (-10, -3)

# Plot points with markers
plt.scatter(*A, color='red', s=100, marker='o', label='A(2,-4)')
plt.scatter(*P, color='blue', s=100, marker='o', label='P(3,8)')
plt.scatter(*Q1, color='green', s=100, marker='o', label='Q(-10,-5)')
plt.scatter(*Q2, color='purple', s=100, marker='o', label='Q2(-10,-3)')

# Draw lines AP, AQ1, AQ2
plt.plot([A[0], P[0]], [A[1], P[1]], 'b--')
plt.plot([A[0], Q1[0]], [A[1], Q1[1]], 'g--')
plt.plot([A[0], Q2[0]], [A[1], Q2[1]], 'm--')

# Annotate points
plt.text(A[0]+0.2, A[1], "A(2,-4)", fontsize=10, color='red')
plt.text(P[0]+0.2, P[1], "P(3,8)", fontsize=10, color='blue')
plt.text(Q1[0]+0.2, Q1[1], "Q1(-10,-5)", fontsize=10, color='green')
plt.text(Q2[0]-1, Q2[1], "Q2(-10,-3)", fontsize=10, color='purple')

# Labels and grid
plt.xlabel('X-axis') 
plt.ylabel('Y-axis')
plt.title('Equidistant Points from A') 
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5)

plt.show() 