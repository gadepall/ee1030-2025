import numpy as np
import matplotlib.pyplot as plt

def rotate_point(point, pivot, R):
    translated_point = point - pivot
    rotated_point = R @ translated_point
    new_point = rotated_point + pivot
    return new_point

P = np.array([1, 3])
Q = np.array([4, 5])
R_vertex = np.array([5, 3.5])

R_matrix = np.array([
    [0.8, 0.6],
    [-0.6, 0.8]
])

Q_new = rotate_point(Q, P, R_matrix)
R_new = rotate_point(R_vertex, P, R_matrix)

plt.figure(figsize=(8, 8))

orig_triangle = np.array([P, Q, R_vertex, P])
plt.plot(orig_triangle[:, 0], orig_triangle[:, 1], 'b-o', label='Original Triangle (PQR)')
new_triangle = np.array([P, Q_new, R_new, P])
plt.plot(new_triangle[:, 0], new_triangle[:, 1], 'r-o', label="Rotated Triangle (PQ'R')")

points_orig = {'P': P, 'Q': Q, 'R': R_vertex}
for name, point in points_orig.items():
    label = f'{name} ({point[0]:.1f}, {point[1]:.1f})'
    plt.text(point[0] + 0.1, point[1] + 0.1, label, fontsize=12, color='blue')

points_new = {"Q'": Q_new, "R'": R_new}
for name, point in points_new.items():
    label = f"{name} ({point[0]:.2f}, {point[1]:.2f})"
    plt.text(point[0] + 0.1, point[1] - 0.2, label, fontsize=12, color='red')
    
plt.title('Clockwise Rotation of a Triangle about Vertex P')
plt.axhline()
plt.axvline()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.legend()
plt.savefig("../figs/plot_p.jpg")
plt.show()
