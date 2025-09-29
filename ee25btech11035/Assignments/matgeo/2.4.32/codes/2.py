import matplotlib.pyplot as plt
import numpy as np

# Define points
A = np.array([-1, -2])
B = np.array([4, 3])
C = np.array([2, 5])
D = np.array([-3, 0])

points = np.array([A, B, C, D, A])  # closed loop

# Function to compute distance
def distance(p1, p2):
    return np.round(np.linalg.norm(p1 - p2), 2)

# Plot quadrilateral
plt.figure(figsize=(6,6))
plt.plot(points[:,0], points[:,1], 'b-')  # edges
plt.scatter(points[:,0], points[:,1], color='red', zorder=5)

# Label vertices
labels = ['A(-1,-2)', 'B(4,3)', 'C(2,5)', 'D(-3,0)']
for i, txt in enumerate(labels):
    plt.text(points[i,0]+0.2, points[i,1]+0.2, txt, fontsize=10)

# Right angle marker function
def right_angle_marker(p, q, r, size=0.7):
    """
    Draws a right angle marker at point q given segment p-q-r
    """
    v1 = (p - q) / np.linalg.norm(p - q)
    v2 = (r - q) / np.linalg.norm(r - q)
    marker = np.array([q, q + v1*size, q + (v1+v2)*size/2, q + v2*size])
    plt.plot(marker[:,0], marker[:,1], 'k-')

# (Markers will only look right if shape has right angles, but kept for consistency)
right_angle_marker(A, B, C)
right_angle_marker(B, C, D)
right_angle_marker(C, D, A)
right_angle_marker(D, A, B)

# Annotate side lengths
midpoints = [(A+B)/2, (B+C)/2, (C+D)/2, (D+A)/2]
lengths = [distance(A,B), distance(B,C), distance(C,D), distance(D,A)]
for mid, length in zip(midpoints, lengths):
    plt.text(mid[0], mid[1], f"{length}", color="green", fontsize=9, ha="center")

plt.title("Quadrilateral ABCD")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.savefig('2.png')
plt.show()
