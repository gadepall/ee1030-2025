import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt

HOME = os.path.expanduser("~")
so_path = os.path.join(HOME, "1.so")
lib = ctypes.CDLL(so_path)

# lib = ctypes.CDLL("/data/data/com.termux/files/home/1.so") 

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

lib.findQuadrilateral.argtypes = [Point, Point, Point, Point]
lib.findQuadrilateral.restype = None

A = Point(-1, -2)
B = Point(4, 3)
C = Point(2, 5)
D = Point(-3, 0)

lib.findQuadrilateral(A, B, C, D)

# For plotting in Python
points = np.array([[A.x, A.y], [B.x, B.y], [C.x, C.y], [D.x, D.y], [A.x, A.y]])

# Function to compute distance
def distance(p1, p2):
    return np.round(np.linalg.norm(p1 - p2), 2)

plt.figure(figsize=(6,6))
plt.plot(points[:,0], points[:,1], 'b-')
plt.scatter(points[:,0], points[:,1], color='red', zorder=5)

labels = ['A(-1,-2)', 'B(4,3)', 'C(2,5)', 'D(-3,0)']
for i, txt in enumerate(labels):
    plt.text(points[i,0]+0.2, points[i,1]+0.2, txt, fontsize=10)

def right_angle_marker(p, q, r, size=0.7):
    v1 = (p - q) / np.linalg.norm(p - q)
    v2 = (r - q) / np.linalg.norm(r - q)
    marker = np.array([q, q + v1*size, q + (v1+v2)*size/2, q + v2*size])
    plt.plot(marker[:,0], marker[:,1], 'k-')

right_angle_marker(points[0], points[1], points[2])
right_angle_marker(points[1], points[2], points[3])
right_angle_marker(points[2], points[3], points[0])
right_angle_marker(points[3], points[0], points[1])

midpoints = [(points[i]+points[i+1])/2 for i in range(4)]
lengths = [distance(points[i], points[i+1]) for i in range(4)]
for mid, length in zip(midpoints, lengths):
    plt.text(mid[0], mid[1], f"{length}", color="green", fontsize=9, ha="center")

plt.title("Quadrilateral ABCD")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)

plt.savefig("1.png")
plt.show()
