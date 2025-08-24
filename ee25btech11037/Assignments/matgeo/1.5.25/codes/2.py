import matplotlib.pyplot as plt

# Points
P = (2, -2)
Q = (3, 7)
R = (24/11, -4/11)   # from your earlier setup

# Plot the points
plt.figure(figsize=(6, 6))
plt.scatter(*P, color='red', s=100, label='P')
plt.scatter(*Q, color='green', s=100, label='Q')
plt.scatter(*R, color='blue', s=100, label='R')

# Add coordinate labels next to points
plt.text(P[0]+0.2, P[1], f'P{P}', fontsize=12, color='red')
plt.text(Q[0]+0.2, Q[1], f'Q{Q}', fontsize=12, color='green')
plt.text(R[0]+0.2, R[1], f'R({R[0]:.2f}, {R[1]:.2f})', fontsize=12, color='blue')

# Connect P and Q for context (optional)
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'k--', alpha=0.5)

# Formatting
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.title("Points P, Q, and R")

# Save and show
plt.savefig('2.png')
plt.show()
