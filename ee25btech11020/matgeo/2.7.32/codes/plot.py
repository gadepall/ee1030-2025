import matplotlib.pyplot as plt

A = (2, 3)
B = (3, 5)
C = (4, 4)

x = [A[0], B[0], C[0], A[0]]
y = [A[1], B[1], C[1], A[1]]

plt.figure(figsize=(6,6))
plt.plot(x, y, 'b-', linewidth=2)   

plt.scatter(*A, color='red', label='A(2,3)')
plt.scatter(*B, color='red', label='B(3,5)')
plt.scatter(*C, color='red', label='C(4,4)')

plt.text(A[0], A[1], "A(2,3)")
plt.text(B[0], B[1], "B(3,5)")
plt.text(C[0], C[1], "C(4,4)")

plt.title("Triangle ABC")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")

plt.savefig("../figs/triangle.png", dpi=300)

