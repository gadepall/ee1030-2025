import ctypes
import numpy as np
import matplotlib.pyplot as plt

N_POINTS = 200
ELLIPSE_A = 3.0
ELLIPSE_B = 1.0
CIRCLE_R = 3.0
LINE_M = -1.0 / 3.0
LINE_C = 1.0
LINE_X_MIN = -4.0  
LINE_X_MAX = 4.0

O = (0.0, 0.0)
A = (3.0, 0.0)
B = (0.0, 1.0)
M = (-12.0 / 5.0, 9.0 / 5.0)
AREA = (1.0/2.0) * A[0] * M[1]


lib = ctypes.CDLL('./shapes.so')

np_double_pointer = np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS')

lib.generate_ellipse.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, np_double_pointer, np_double_pointer]
lib.generate_ellipse.restype = None

lib.generate_circle.argtypes = [ctypes.c_double, ctypes.c_int, np_double_pointer, np_double_pointer]
lib.generate_circle.restype = None

lib.generate_line.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int, np_double_pointer, np_double_pointer]
lib.generate_line.restype = None

x_ellipse = np.zeros(N_POINTS, dtype=np.float64)
y_ellipse = np.zeros(N_POINTS, dtype=np.float64)

x_circle = np.zeros(N_POINTS, dtype=np.float64)
y_circle = np.zeros(N_POINTS, dtype=np.float64)

x_line = np.zeros(N_POINTS, dtype=np.float64)
y_line = np.zeros(N_POINTS, dtype=np.float64)

lib.generate_ellipse(ELLIPSE_A, ELLIPSE_B, N_POINTS, x_ellipse, y_ellipse)
lib.generate_circle(CIRCLE_R, N_POINTS, x_circle, y_circle)
lib.generate_line(LINE_M, LINE_C, LINE_X_MIN, LINE_X_MAX, N_POINTS, x_line, y_line)

print(f"Plotting shapes...")
print(f"Area of Triangle OAM: 27/10 = {AREA}")
plt.figure(figsize=(9, 9))

plt.plot(x_ellipse, y_ellipse, label=f'Ellipse: $x^2/9 + y^2/1 = 1$')
plt.plot(x_circle, y_circle, label=f'Auxiliary Circle: $x^2 + y^2 = 9$', linestyle='--', color='orange')
plt.plot(x_line, y_line, label=f'Line AB: $y = -x/3 + 1$', color='green')

points_x = [O[0], A[0], B[0], M[0]]
points_y = [O[1], A[1], B[1], M[1]]
labels = ['O (0, 0)', 'A (3, 0)', 'B (0, 1)', 'M (-12/5, 9/5)']
plt.scatter(points_x, points_y, color='red', zorder=5)

for label, x, y in zip(labels, points_x, points_y):
    plt.text(x + 0.1, y + 0.1, label, fontsize=9)

triangle_x = [O[0], A[0], M[0], O[0]]
triangle_y = [O[1], A[1], M[1], O[1]]
plt.plot(triangle_x, triangle_y, 'r-', label=f'Triangle OAM (Area = {AREA})')

plt.title('Ellipse, Auxiliary Circle, and Intersecting Line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.axis('equal') 
plt.savefig("./figs/ellipse.png")
plt.show()
