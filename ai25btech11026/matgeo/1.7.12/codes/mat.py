import matplotlib.pyplot as plt

# Given points
P = (5, 4)
R = (9, -2)

# Find k using collinearity condition
slope_PR = (R[1] - P[1]) / (R[0] - P[0])
k = slope_PR * (7 - 5) + 4
Q = (7, k)

# Plotting the points and line
plt.figure(figsize=(6,6))
plt.plot([P[0], Q[0], R[0]], [P[1], Q[1], R[1]], 'ro')  # points
plt.plot([P[0], Q[0], R[0]], [P[1], Q[1], R[1]], 'b-')  # line

# Annotating points
plt.text(P[0]+0.1, P[1], f"P{P}")
plt.text(Q[0]+0.1, Q[1], f"Q{Q}")
plt.text(R[0]+0.1, R[1], f"R{R}")

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.title("Collinear Points Diagram")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# Save as image
plt.savefig("collinear_points.png", dpi=300)
plt.show()

print("Value of k:", k)
print("Graph saved as 'collinear_points.png'")
