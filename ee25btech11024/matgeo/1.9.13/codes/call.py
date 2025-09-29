mport ctypes #for interacting with c code (datatypes such as .so)
import numpy as np
import matplotlib.pyplot as plt

so = ctypes.CDLL("./find_distance.so") #loads my shared c library so that python can use it

so.find_distance.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
so.find_distance.restype = ctypes.c_double

O = np.array([0,0])
A = np.array([-5,0])
B = np.array([-5,12])

d_OA = so.find_distance(O[0], O[1], A[0], A[1])
d_AB = so.find_distance(A[0], A[1], B[0], B[1])
d_OB = so.find_distance(O[0], O[1], B[0], B[1])

plt.figure(figsize = (7,7))
plt.plot([O[0], A[0]], [O[1], A[1]], 'g-', label = f"OA = {d_OA:.0f} units")
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label = f"AB = {d_AB:.0f} units")
plt.plot([O[0], B[0]], [O[1], B[1]], 'r-', label = f"OB = {d_OB:.0f} units")

plt.scatter(*O, color = 'green')
plt.scatter(*A, color = 'blue')
plt.scatter(*B, color = 'red')

plt.text(O[0]+0.2, O[1]+0.2, "O(0,0)")
plt.text(A[0]+0.2, A[1]+0.2, "A(-5,0)")
plt.text(B[0]+0.2, B[1], "B(-5, 10)")

plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.title("Distance from starting point when man walks from O to A and from A to B")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.savefig("fig.png")
plt.show()
