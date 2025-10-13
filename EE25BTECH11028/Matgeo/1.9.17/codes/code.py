import matplotlib.pyplot as plt

# Coordinates
A = (-2, 0)
B = (6, 0)
P = (2, 0)

# Plot points
plt.figure(figsize=(6,6))
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# A point
plt.scatter(A[0], A[1], color="red")
plt.text(A[0]-0.5, A[1]+0.3, "A (-2,0)")
plt.plot([A[0], P[0]], [A[1], P[1]], "r--")

# B point
plt.scatter(B[0], B[1], color="blue")
plt.text(B[0]+0.2, B[1]+0.3, "B (6,0)")
plt.plot([B[0], P[0]], [B[1], P[1]], "b--")

# P point (equidistant point)
plt.scatter(P[0], P[1], color="green", s=150, marker="*")
plt.text(P[0]-0.2, P[1]+0.3, "P (2,0)")

# Labels and grid
plt.title("Equidistant Point on X-axis")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend(["A (-2,0)", "B (6,0)", "P (2,0)"])
plt.axis("equal")
plt.show()

