import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library (update path if needed)
lib = ctypes.CDLL("./1.so")   # <-- replace with your actual .so filename

# Define the Point struct in Python (matching C struct)
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

# Define C function signature
lib.findQuadrilateral.argtypes = [Point, Point, Point, Point]
lib.findQuadrilateral.restype = None

# Define points (same as problem)
A = Point(2, -2)
B = Point(7, 3)
C = Point(11, -1)
D = Point(6, -6)

# Call the C function (prints classification in terminal)
lib.findQuadrilateral(A, B, C, D)

# For plotting in Python
points = np.array([[A.x, A.y], [B.x, B.y], [C.x, C.y], [D.x, D.y], [A.x, A.y]])

# Function to compute distance
def distance(p1, p2):
    return np.round(np.linalg.norm(p1 - p2), 2)

# Plot quadrilateral
plt.figure(figsize=(6,6))
plt.plot(points[:,0], points[:,1], 'b-')
plt.scatter(points[:,0], points[:,1], color='red', zorder=5)

# Label vertices
labels = ['A(2,-2)', 'B(7,3)', 'C(11,-1)', 'D(6,-6)']
for i, txt in enumerate(labels):
    plt.text(points[i,0]+0.2, points[i,1]+0.2, txt, fontsize=10)

# Right angle marker function
def right_angle_marker(p, q, r, size=0.7):
    v1 = (p - q) / np.linalg.norm(p - q)
    v2 = (r - q) / np.linalg.norm(r - q)
    marker = np.array([q, q + v1*size, q + (v1+v2)*size/2, q + v2*size])
    plt.plot(marker[:,0], marker[:,1], 'k-')

# Show right angles
right_angle_marker(points[0], points[1], points[2])
right_angle_marker(points[1], points[2], points[3])
right_angle_marker(points[2], points[3], points[0])
right_angle_marker(points[3], points[0], points[1])

# Annotate side lengths
midpoints = [(points[i]+points[i+1])/2 for i in range(4)]
lengths = [distance(points[i], points[i+1]) for i in range(4)]
for mid, length in zip(midpoints, lengths):
    plt.text(mid[0], mid[1], f"{length}", color="green", fontsize=9, ha="center")

plt.title("Rectangle ABCD with Right Angles and Equal Opposite Sides")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)

# Save figure as 1.png
plt.savefig("1.png")
plt.show()

