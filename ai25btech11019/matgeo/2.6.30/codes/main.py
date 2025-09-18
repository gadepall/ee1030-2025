import matplotlib.pyplot as plt

# Common vertices
A = (2, 6)
B = (5, -4)

# Two cases for k
k1 = -4.4
k2 = 9.6

C1 = (k1, 4)
C2 = (k2, 4)

# Plot first triangle (k = -4.4)
x1 = [A[0], B[0], C1[0], A[0]]
y1 = [A[1], B[1], C1[1], A[1]]
plt.plot(x1, y1, color='blue', label='Triangle (k=-4.4)')
plt.scatter(*A, color='red')
plt.scatter(*B, color='red')
plt.scatter(*C1, color='red')
plt.text(A[0], A[1], f"A{A}")
plt.text(B[0], B[1], f"B{B}")
plt.text(C1[0], C1[1], f"C{C1}")

# Plot second triangle (k = 9.6)
x2 = [A[0], B[0], C2[0], A[0]]
y2 = [A[1], B[1], C2[1], A[1]]
plt.plot(x2, y2, color='brown', linestyle='--', label='Triangle (k=9.6)')
plt.scatter(*C2, color='red')
plt.text(C2[0], C2[1], f"C{C2}")

# Axis labels and title
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Triangles with vertices (2,6), (5,-4), and (k,4)")
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.show()
