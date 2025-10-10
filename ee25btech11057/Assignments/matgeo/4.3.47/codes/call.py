import ctypes
import os

# Part 1: Call the C shared object
# Path to shared object (must be in same directory)
lib_path = os.path.abspath("./libline.so")

# Load the shared library
lib = ctypes.CDLL(lib_path)

# Tell Python return type of the function
lib.get_line_equation.restype = ctypes.c_char_p

# Call the function
c_result = lib.get_line_equation().decode("utf-8")
print("=== Result from C shared library ===")
print(c_result)
print()
# Part 2: Direct computation in Python

def line_equation(x0, y0, slope):
    dx, dy = 1.0, slope
    a, b = dy, -dx
    c = -(a * x0 + b * y0)
    print("=== Direct Python Computation ===")
    print(f"Point on line: ({x0}, {y0})")
    print(f"Slope: {slope}")
    print(f"Cartesian form: {a:.2f}x + {b:.2f}y + {c:.2f} = 0")
    print(f"Vector form: r = ({x0}, {y0}) + t({dx}, {dy})")
    print()

line_equation(-2, 3, -4)

# Part 3: Row reduction (manual)
def row_reduction():
    print("=== Row Reduction Verification ===")
    # Equations: a - 4b = 0, -2a + 3b + c = 0
    print("System of equations:")
    print("1) a - 4b = 0")
    print("2) -2a + 3b + c = 0")

    # From (1): a = 4b
    # Substitute into (2): -8b + 3b + c = 0 => -5b + c = 0 => c = 5b
    a = 4
    b = 1
    c = 5
    print(f"Solution (up to scale): (a, b, c) = ({a}, {b}, {c})")
    print(f"Equation: {a}x + {b}y + {c} = 0")
    print()

row_reduction()
