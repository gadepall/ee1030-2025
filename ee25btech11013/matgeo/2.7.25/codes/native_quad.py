import numpy as np
import matplotlib.pyplot as plt


def triangle_area(A, B, C):
    v1 = np.array(B) - np.array(A)
    v2 = np.array(C) - np.array(A)
    return 0.5 * abs(np.cross(v1, v2))


def quad_area(A, B, C, D):
    return triangle_area(A, B, C) + triangle_area(A, C, D)
    
A = (-3, -1)
B = (-2, -4)
C = (4, -1)
D = (3, 4)

area = quad_area(A, B, C, D)
print("Area of Quadrilateral ABCD =", area)

points = np.array([A, B, C, D, A])  
plt.plot(points[:,0], points[:,1], 'b-o')
plt.fill(points[:,0], points[:,1], color='lightgreen', alpha=0.5)

for point, label in zip([A, B, C, D], ["A", "B", "C", "D"]):
    plt.text(point[0], point[1], label, fontsize=12, ha='right')

plt.title(f"Quadrilateral ABCD (Area = {area:.2f})")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.savefig("/Users/bhargavkrish/Documents/ee1030-2025/ee25btech11013/matgeo/2.7.25/figs/Figure_1.png")
plt.show()