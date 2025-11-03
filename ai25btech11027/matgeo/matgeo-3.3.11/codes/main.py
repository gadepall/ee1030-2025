import ctypes
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./main.so')

# Define ctypes arrays for 2 doubles (x,y)
A = (ctypes.c_double * 2)()
B = (ctypes.c_double * 2)()
C = (ctypes.c_double * 2)()

lib.compute_triangle.argtypes = [ctypes.c_double * 2, ctypes.c_double * 2, ctypes.c_double * 2]
lib.compute_triangle.restype = None

lib.compute_triangle(A, B, C)

print(f"A = ({A[0]:.2f}, {A[1]:.2f})")
print(f"B = ({B[0]:.2f}, {B[1]:.2f})")
print(f"C = ({C[0]:.2f}, {C[1]:.2f})")

x = [A[0], B[0], C[0], A[0]]
y = [A[1], B[1], C[1], A[1]]

plt.plot(x, y, 'b-', linewidth=2)
plt.fill(x, y, 'lightblue', alpha=0.4)
plt.text(A[0]+0.1, A[1]+0.1, 'A')
plt.text(B[0]+0.1, B[1]+0.1, 'B')
plt.text(C[0]+0.1, C[1]+0.1, 'C')
plt.axis('equal')
plt.grid(True)
plt.show()

