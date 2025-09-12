import matplotlib.pyplot as plt

# Given point
A = (3, -5)
d = 15  # distance

# Solve for x
# |x - 3| = 15  →  x = 18 or -12
x1 = 18
x2 = -12

B1 = (x1, -5)
B2 = (x2, -5)

print("Solutions for x: ", x1, "and", x2)

# Plotting
plt.figure(figsize=(8,6))
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Points
plt.scatter(*A, color='black', s=80)
plt.text(A[0]+0.3, A[1]+0.5, "A(3,-5)", fontsize=12)

plt.scatter(*B1, color='blue', s=80)
plt.text(B1[0]+0.3, B1[1]+0.5, "B1(18,-5)", fontsize=12, color='blue')

plt.scatter(*B2, color='red', s=80)
plt.text(B2[0]+0.3, B2[1]+0.5, "B2(-12,-5)", fontsize=12, color='red')

# Lines
plt.plot([A[0], B1[0]], [A[1], B1[1]], color='blue', linewidth=2, label="15 units")
plt.plot([A[0], B2[0]], [A[1], B2[1]], color='red', linewidth=2, linestyle='--', label="15 units")

# Labels
plt.legend()
plt.xlim(-15,20)
plt.ylim(-10,5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Distance between (3,-5) and (x,-5) = 15 units")
plt.grid(True)
plt.show()
