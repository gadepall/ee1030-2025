import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C shared library
lib = ctypes.CDLL('./2.5.4.so')  

# Define return and arg types
lib.solve_y_matrix_form.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.solve_y_matrix_form.restype = ctypes.c_int

# Prepare output variables
y1 = ctypes.c_double()
y2 = ctypes.c_double()

# Call C function
res = lib.solve_y_matrix_form(ctypes.byref(y1), ctypes.byref(y2))
if res != 0:
    print("No real roots for y found.")
    exit()

y_values = [y1.value, y2.value]
print(f"Values of y computed using matrix multiplication in C: {y_values}")

# Plotting function
def plot_vectors_for_y(y_val):
    a = np.array([2, y_val, 1])
    b = np.array([1, 2, 3])
    a_plus_b = a + b
    a_minus_b = a - b
    origin = np.array([0, 0, 0])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    def draw(vec, color, label):
        ax.quiver(*origin, *vec, color=color, label=label, arrow_length_ratio=0.1)

    draw(a, 'red', 'a')
    draw(b, 'blue', 'b')
    draw(a_plus_b, 'green', 'a + b')
    draw(a_minus_b, 'purple', 'a - b')

    ax.set_xlim([-1, 6])
    ax.set_ylim([-4, 6])
    ax.set_zlim([-4, 6])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Vectors for y = {y_val}')
    ax.legend()
    plt.grid(True)
    plt.show()

# Plot for each y
for y in y_values:
    plot_vectors_for_y(y)

