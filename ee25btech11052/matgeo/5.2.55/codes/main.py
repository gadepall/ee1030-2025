import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./libequationsolve.so")

# Define argument/return types
lib.solve_system.argtypes = [((ctypes.c_double*2)*2), (ctypes.c_double*2), (ctypes.c_double*2)]
lib.solve_system.restype = ctypes.c_int

# Define the system: 2/x + 3/y = 13, 5/x + 4/y = -2
# Let u = 1/x, v = 1/y: 2u + 3v = 13, 5u + 4v = -2
A = np.array([[2, 3], [5, 4]], dtype=np.double)
b = np.array([13, -2], dtype=np.double)

# Convert to C types
A_c = ((ctypes.c_double*2)*2)(*[((ctypes.c_double*2)(*row)) for row in A])
b_c = (ctypes.c_double*2)(*b)
result = (ctypes.c_double*2)()

# Solve using C function
success = lib.solve_system(A_c, b_c, result)

if success:
    u, v = result[0], result[1]
    x = 1.0 / u  # x = 1/u
    y = 1.0 / v  # y = 1/v
    
    print(f"u = {u:.6f}, v = {v:.6f}")
    print(f"Solution: x = {x:.6f}, y = {y:.6f}")
    
    # Verify in Python
    eq1 = 2/x + 3/y
    eq2 = 5/x + 4/y
    print(f"Verification: 2/x + 3/y = {eq1:.6f} (should be 13)")
    print(f"Verification: 5/x + 4/y = {eq2:.6f} (should be -2)")
    
    # Plot the curves
    xx = np.linspace(-2, 2, 1000)
    xx = xx[np.abs(xx) > 0.005]  # Avoid division by zero
    
    # Calculate y values for both equations
    y1 = 3 / (13 - 2/xx)  # From 2/x + 3/y = 13
    y2 = 4 / (-2 - 5/xx)  # From 5/x + 4/y = -2
    
    plt.figure(figsize=(8, 6))
    plt.plot(xx, y1, 'b-', label='2/x + 3/y = 13')
    plt.plot(xx, y2, 'r-', label='5/x + 4/y = -2')
    plt.plot(x, y, 'ro', markersize=8)
    plt.text(x + 0.01, y + 0.01, f'({x:.4f}, {y:.4f})')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('System of Equations')
    plt.legend()
    plt.grid(True)
    plt.xlim(-2,2)
    plt.ylim(-2,2)
    
    plt.savefig('/home/shriyasnh/Desktop/matgeonew/5.2.55/figs/equation_plot.png', dpi=300, bbox_inches='tight')
    plt.show()
    