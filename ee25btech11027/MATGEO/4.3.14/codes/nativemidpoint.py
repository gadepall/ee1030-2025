import matplotlib.pyplot as plt

# Given midpoint
M = (2, 5)

# From calculation
P = (0, 10)
Q = (4, 0)

plt.plot([P[0], Q[0]], [P[1], Q[1]], 'b-', label="Line PQ")

plt.scatter(*P, color="red", s=100, label=f"P{P}")
plt.scatter(*Q, color="green", s=100, label=f"Q{Q}")
plt.scatter(*M, color="purple", s=150, marker="*", label=f"M{M}")

plt.text(P[0]+0.2, P[1], f"P{P}", fontsize=10)
plt.text(Q[0]+0.2, Q[1], f"Q{Q}", fontsize=10)
plt.text(M[0]+0.2, M[1], f"M{M}", fontsize=10, color="purple")

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.title("Figure")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/4.3.14/figs/figure1.png")
plt.show()
