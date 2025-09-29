import matplotlib.pyplot as plt

# Hardcoded values
P = (2, 4)
A = (5, 3)
B = (3, 7)

# Plot points
plt.figure(figsize=(6,6))
plt.scatter(*P, color="red", label=f"P{P}")
plt.scatter(*A, color="blue", label=f"A{A}")
plt.scatter(*B, color="green", label=f"B{B}")

# Connect visually
plt.plot([P[0], A[0]], [P[1], A[1]], "b--", alpha=0.6)
plt.plot([P[0], B[0]], [P[1], B[1]], "g--", alpha=0.6)

# Formatting
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.title("Points P, A, and B (Hardcoded)")

# Save the plot
plt.savefig("2.png")

# Show the plot
plt.show()
