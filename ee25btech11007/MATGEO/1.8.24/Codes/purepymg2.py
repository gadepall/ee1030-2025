import numpy as np
import matplotlib.pyplot as plt

# Given data
A = np.array([10, -6])
B = np.array([22, 4])
O = (A + B) // 2   # midpoint (integer division gives exact midpoint here)

# Convert to Python tuples for clean display
A_t = tuple(A.tolist())
B_t = tuple(B.tolist())
O_t = tuple(O.tolist())

# Print results
print("A =", A_t)
print("B =", B_t)
print("O =", O_t)

# Plotting
plt.figure()
plt.plot([A[0], B[0]], [A[1], B[1]], 'k-', label="Segment AB")  # line AB
plt.scatter(*A, color='red', label=f"A{A_t}")
plt.scatter(*B, color='blue', label=f"B{B_t}")
plt.scatter(*O, color='green', label=f"O{O_t}")

# Annotate points with clean integer tuples
plt.text(A[0]+0.5, A[1], f"A{A_t}")
plt.text(B[0]+0.5, B[1], f"B{B_t}")
plt.text(O[0]+0.5, O[1], f"O{O_t}")

plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Segment AB and Midpoint O")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()	
