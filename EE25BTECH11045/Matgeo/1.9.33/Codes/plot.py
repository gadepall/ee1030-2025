import matplotlib.pyplot as plt

# Points
Q = (0, 1)
P = (5, -3)
R1 = (4, 6)
R2 = (-4, 6)

# Plot points with markers
plt.scatter(*Q, color='red', s=100, marker='o', label='Q(0,1)')
plt.scatter(*P, color='blue', s=100, marker='o', label='P(5,-3)')
plt.scatter(*R1, color='green', s=100, marker='o', label='R1(4,6)')
plt.scatter(*R2, color='purple', s=100, marker='o', label='R2(-4,6)')

# Draw lines QP, QR1, QR2
plt.plot([Q[0], P[0]], [Q[1], P[1]], 'b--')
plt.plot([Q[0], R1[0]], [Q[1], R1[1]], 'g--')
plt.plot([Q[0], R2[0]], [Q[1], R2[1]], 'm--')

# Annotate points
plt.text(Q[0]+0.2, Q[1], "Q(0,1)", fontsize=10, color='red')
plt.text(P[0]+0.2, P[1], "P(5,-3)", fontsize=10, color='blue')
plt.text(R1[0]+0.2, R1[1], "R1(4,6)", fontsize=10, color='green')
plt.text(R2[0]-1, R2[1], "R2(-4,6)", fontsize=10, color='purple')

# Labels and grid
plt.xlabel('X-axis') 
plt.ylabel('Y-axis')
plt.title('Equidistant Points from Q') 
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5)

plt.show() 