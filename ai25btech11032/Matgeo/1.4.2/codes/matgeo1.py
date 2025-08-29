import numpy as np
import matplotlib.pyplot as plt

# Define vectors
P = np.array([1, 3])
Q = np.array([2, 5])

# λ = 3/5
lam = 3/5
R = P + lam * (Q - P)

# Plot line PQ
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'k--', label="Line PQ")

# Plot points
plt.scatter(*P, color='red', label="P(1,3)")
plt.scatter(*Q, color='blue', label="Q(2,5)")
plt.scatter(*R, color='green', label=f"R{tuple(R)}")

# Annotate points
plt.text(P[0]-0.1, P[1]-0.2, "P", fontsize=12, color='red')
plt.text(Q[0]+0.1, Q[1], "Q", fontsize=12, color='blue')
plt.text(R[0]+0.1, R[1], "R", fontsize=12, color='green')

# Style
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Point R dividing PQ in ratio 3:2 (vector method)")
plt.legend()
plt.grid(True)
plt.axis("equal")

# Save plot to file
plt.savefig("PQ_R_plot.png", dpi=300)   # Saves in current folder
# plt.savefig("PQ_R_plot.pdf")         # Alternative format

plt.show()
