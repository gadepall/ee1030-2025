import matplotlib.pyplot as plt

# Vertices of rhombus (centered at origin)
A = (-3, 0)
B = (0, 2)
C = (3, 0)
D = (0, -2)

# Collect points to plot closed rhombus
x = [A[0], B[0], C[0], D[0], A[0]]
y = [A[1], B[1], C[1], D[1], A[1]]

# Plot rhombus
plt.figure(figsize=(6,6))
plt.plot(x, y, 'b-o', linewidth=2)
plt.fill(x, y, 'skyblue', alpha=0.5)

# Mark vertices
plt.text(A[0]-0.3, A[1], "A(-3,0)", fontsize=12)
plt.text(B[0], B[1]+0.3, "B(0,2)", fontsize=12, ha="center")
plt.text(C[0]+0.3, C[1], "C(3,0)", fontsize=12)
plt.text(D[0], D[1]-0.3, "D(0,-2)", fontsize=12, ha="center")

# Add diagonals
plt.plot([-3, 3], [0, 0], 'r--')  # horizontal diagonal
plt.plot([0, 0], [-2, 2], 'r--')  # vertical diagonal

# Styling
plt.title("Rhombus with diagonals 4 cm and 6 cm")
plt.axis("equal")
plt.grid(True)

# Save figure
plt.savefig("rhombus.png", dpi=300)
plt.show()
