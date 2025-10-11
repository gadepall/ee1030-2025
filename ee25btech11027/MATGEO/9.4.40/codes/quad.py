import ctypes
import platform
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Load the C library ---
lib_name = 'quad.so'
if platform.system() == 'Windows':
    lib_name = 'quad.dll'

try:
    c_lib = ctypes.CDLL(f'./{lib_name}')
except OSError as e:
    print(f"Error loading shared library: {e}")
    print(f"Please make sure you have compiled solver.c into {lib_name}")
    exit()

# --- 2. Define the C function signature for Python ---
c_lib.solve_quadratic.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]
c_lib.solve_quadratic.restype = ctypes.c_int

def solve_with_c(a, b, c):
    """A Python wrapper that calls the C function."""
    root1 = ctypes.c_double()
    root2 = ctypes.c_double()
    
    num_roots = c_lib.solve_quadratic(a, b, c, ctypes.byref(root1), ctypes.byref(root2))
    
    if num_roots == 0: return None
    if num_roots == 1: return (root1.value,)
    return (root1.value, root2.value)

def plot_solution(a, b, c, roots):
    """Plots the quadratic function and its intersection points with the x-axis."""
    s_values = np.linspace(min(roots) - 20, max(roots) + 20, 400)
    y_values = a * s_values**2 + b * s_values + c

    plt.figure(figsize=(10, 6))
    
    # Plot the parabola
    plt.plot(s_values, y_values, label=f'Parabola: $y = s^2 + 5s - 1800$')
    
    # Plot the x-axis for reference
    plt.axhline(0, color='black', linestyle='--')
    
    # Plot the intersection points (roots)
    plt.plot(roots, [0]*len(roots), 'ro', markersize=8, label=f'Intersection Points')
    for root in roots:
        plt.text(root, 100, f'({root:.1f}, 0)', ha='center', fontsize=10)
    positive_root = next(r for r in roots if r > 0)
    plt.title(f"Solution to the Train Problem (s = {positive_root:.0f} km/hr)")
    plt.xlabel("Speed (s)")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/9.4.40/figs/figure1.png")
    plt.show()

# --- Main execution ---
if __name__ == "__main__":
    # Coefficients from the train problem: s^2 + 5s - 1800 = 0
    a, b, c = 1.0, 5.0, -1800.0
    
    roots = solve_with_c(a, b, c)

    if roots:
        sorted_roots = sorted(roots)
        print(f"Roots found via C function: {sorted_roots}")
        plot_solution(a, b, c, sorted_roots)
    else:
        print("No real roots found.")
