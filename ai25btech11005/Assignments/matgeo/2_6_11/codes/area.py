import matplotlib.pyplot as plt
# Given midpoints D, E, F
D = (-0.5, 2.5)
E = (7, 3)
F = (3.5, 3.5)
# Reconstruct vertices A, B, C using midpoint formulas
A = (F[0] + E[0] - D[0], F[1] + E[1] - D[1])
B = (D[0] + F[0] - E[0], D[1] + F[1] - E[1])
C = (D[0] + E[0] - F[0], D[1] + E[1] - F[1])
plt.figure(figsize=(8,8))
# Plot triangle ABC
triangle_x = [A[0], B[0], C[0], A[0]]
triangle_y = [A[1], B[1], C[1], A[1]]
plt.plot(triangle_x, triangle_y, 'b-', label='Triangle ABC')
# Mark midpoints D, E, F as red dots
plt.plot(D[0], D[1], 'ro')
plt.plot(E[0], E[1], 'ro')
plt.plot(F[0], F[1], 'ro')
 # Annotate vertices
plt.text(A[0], A[1], ' A', fontsize=12, color='blue')
plt.text(B[0], B[1], ' B', fontsize=12, color='blue')
plt.text(C[0], C[1], ' C', fontsize=12, color='blue')
# Annotate midpoints
plt.text(D[0], D[1], ' D', fontsize=12, color='red')
plt.text(E[0], E[1], ' E', fontsize=12, color='red')
plt.text(F[0], F[1], ' F', fontsize=12, color='red')
plt.title('Triangle ABC and Midpoints D, E, F')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()