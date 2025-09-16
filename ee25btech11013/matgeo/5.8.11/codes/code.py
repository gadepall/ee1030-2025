import numpy as np
import matplotlib.pyplot as plt
import ctypes


lib = ctypes.CDLL("./code.so")   


lib.solve_2x2.argtypes = [ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double)]
lib.solve_2x2.restype = ctypes.c_int


A = np.array([[3, 6],
              [1, 3]], dtype=np.float64)
b = np.array([3900, 3300], dtype=np.float64)
x = np.zeros(2, dtype=np.float64)


status = lib.solve_2x2(A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                       b.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                       x.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

if status == 0:
    x_sol, y_sol = x
    print(f"The system has a unique solution:")
    print(f"x = {x_sol}")
    print(f"y = {y_sol}")

    x_vals = np.linspace(x_sol - 3000, x_sol + 3000, 400)
    y1 = (3900 - 3 * x_vals) / 6
    y2 = (3300 - x_vals) / 3

    plt.figure(figsize=(8, 8))
    plt.plot(x_vals, y1, label=r'$3x + 6y = 3900$')
    plt.plot(x_vals, y2, label=r'$x + 3y = 3300$')
    plt.plot(x_sol, y_sol, 'ro', label=f'Intersection ({x_sol:.2f}, {y_sol:.2f})')

    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("System of Equations with a Unique Solution")
    plt.legend()
    plt.grid(True)

    plt.savefig("Figure_1.png")
    plt.show()

else:
    print("The system does not have a unique solution.")
