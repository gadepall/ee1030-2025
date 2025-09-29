import ctypes
import math
import matplotlib.pyplot as plt
from ctypes import CDLL, Structure, c_double

class Point(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]

# Load the shared library
lib = CDLL("./triangle.so")
lib.solve_point_A.argtypes = [c_double, c_double, c_double]
lib.solve_point_A.restype = Point

def solve_point_A(BC, angle_B_deg, angle_C_deg):
    result = lib.solve_point_A(BC, angle_B_deg, angle_C_deg)
    return (result.x, result.y)

def plot_triangle(A, B, C):
    x_coords = [A[0], B[0], C[0], A[0]]
    y_coords = [A[1], B[1], C[1], A[1]]

    plt.figure(figsize=(6, 6))
    plt.plot(x_coords, y_coords, 'ro-', linewidth=2)
    plt.fill(x_coords, y_coords, alpha=0.2, color='lightcoral')

    plt.text(A[0], A[1], 'A', fontsize=12, ha='right', va='bottom')
    plt.text(B[0], B[1], 'B', fontsize=12, ha='right', va='top')
    plt.text(C[0], C[1], 'C', fontsize=12, ha='left', va='top')

    plt.title("Triangle ABC (Linear Algebra Method)")
    plt.axis('equal')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    BC = 7.0
    angle_B = 45.0
    angle_C = 60.0

    A = solve_point_A(BC, angle_B, angle_C)
    B = (0.0, 0.0)
    C = (BC, 0.0)

    print(f"Point A (LA method): x = {A[0]:.4f}, y = {A[1]:.4f}")
    plot_triangle(A, B, C)

