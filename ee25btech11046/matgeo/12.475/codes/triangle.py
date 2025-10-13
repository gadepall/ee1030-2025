import numpy as np
import matplotlib.pyplot as plt
import ctypes

triangle = ctypes.CDLL('./triangle.so')

triangle.function.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), 
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), 
    ctypes.POINTER(ctypes.c_double)
]
triangle.function.restype = None

def rotation(point, pivot, R_matrix):
    p_c = point.astype(np.float64)
    pivot_c = pivot.astype(np.float64)
    R_c = R_matrix.flatten().astype(np.float64)
    q_new_x, q_new_y = ctypes.c_double(0), ctypes.c_double(0)
    triangle.function(
        p_c.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        pivot_c.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        R_c.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        ctypes.byref(q_new_x),
        ctypes.byref(q_new_y)
    )
    return np.array([q_new_x.value, q_new_y.value])

P = np.array([1, 3])
Q = np.array([4, 5])
R_vertex = np.array([5, 3.5])
R_matrix = np.array([[0.8, 0.6], [-0.6, 0.8]])

Q_new = rotation(Q, P, R_matrix)
R_new = rotation(R_vertex, P, R_matrix)

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
plt.savefig("../figs/plot_c.jpg")
plt.show()
