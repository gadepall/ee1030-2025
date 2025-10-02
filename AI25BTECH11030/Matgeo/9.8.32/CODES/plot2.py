import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C library
lib = ctypes.CDLL('./libmatfun.so')

# Set up function signatures
lib.solve_problem.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.solve_problem.restype = ctypes.c_int

# Main execution
if __name__ == "__main__":
    # Call C function to solve the problem
    center = (ctypes.c_double * 2)()
    radius = ctypes.c_double()
    
    result = lib.solve_problem(center, ctypes.byref(radius))
    
    if result:
        cx, cy, r = center[0], center[1], radius.value
        
        print(f"Center: ({cx:.6f}, {cy:.6f})")
        print(f"Radius: {r:.6f}")
        
        # Simple plotting
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Plot parabola y = x²
        x_para = np.linspace(-8, 4, 500)
        y_para = x_para**2
        mask = (y_para <= 12)  # Limit y range
        ax.plot(x_para[mask], y_para[mask], 'b-', linewidth=2, label='y = x²')
        
        # Plot circle
        theta = np.linspace(0, 2*np.pi, 500)
        x_circle = cx + r * np.cos(theta)
        y_circle = cy + r * np.sin(theta)
        ax.plot(x_circle, y_circle, 'r-', linewidth=2, label='Circle')
        
        # Mark points
        ax.plot(0, 1, 'go', markersize=8, label='P(0,1)')
        ax.plot(2, 4, 'mo', markersize=8, label='Q(2,4)')
        ax.plot(cx, cy, 'ro', markersize=8, label=f'Center({cx:.1f},{cy:.1f})')
        
        # Normal line
        ax.plot([cx, 2], [cy, 4], 'k--', alpha=0.7, label='Normal')
        
        # Tangent line y = 4x - 4
        x_tan = np.linspace(0.5, 3.5, 50)
        y_tan = 4*x_tan - 4
        ax.plot(x_tan, y_tan, 'g--', alpha=0.7, label='Tangent')
        
        # Set limits and format
        ax.set_xlim(cx-r-1, cx+r+1)
        ax.set_ylim(cy-r-1, cy+r+1)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Circle-Parabola Problem (C Library)')
        ax.legend()
        ax.set_aspect('equal')
        
        plt.show()
    else:
        print("Failed to solve problem")
