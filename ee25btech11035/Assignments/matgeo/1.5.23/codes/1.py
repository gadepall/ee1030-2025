import ctypes
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

lib = ctypes.CDLL("/root/1.so")


lib.areCollinear3D.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int,
                               ctypes.c_int, ctypes.c_int, ctypes.c_int,
                               ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.areCollinear3D.restype = ctypes.c_int

A = (-2, 3, 5)
B = (1, 2, 3)
C = (7, 0, -1)

result = lib.areCollinear3D(A[0], A[1], A[2],
                            B[0], B[1], B[2],
                            C[0], C[1], C[2])

if result == 1:
    print("The points are collinear.")
else:
    print("The points are not collinear.")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(*A, color="red", s=100, label=f"A{A}")
ax.scatter(*B, color="green", s=100, label=f"B{B}")
ax.scatter(*C, color="blue", s=100, label=f"C{C}")

if result == 1:
    # Find extreme points among A, B, C
    points = [A, B, C]

    # Sort based on one coordinate where they differ (X works fine here)
    points_sorted = sorted(points, key=lambda p: p[0])

    P1, P2 = points_sorted[0], points_sorted[-1]

    # Draw solid line segment
    ax.plot([P1[0], P2[0]],
            [P1[1], P2[1]],
            [P1[2], P2[2]],
            color='black', linewidth=2, label="Line segment")

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
plt.savefig('1.png')
plt.show()
