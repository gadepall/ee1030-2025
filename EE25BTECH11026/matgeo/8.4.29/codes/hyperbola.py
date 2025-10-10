import ctypes
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt

# Load the shared library
lib = ctypes.CDLL("./libconfocal.so")

# Define argument and return types for the C function
lib.hyperbola_params.argtypes = [ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
lib.hyperbola_params.restype = None

def get_hyperbola_params(theta):
    arr = (ctypes.c_double * 2)()
    lib.hyperbola_params(theta, arr)
    return arr[0], arr[1]   # returns (a^2, b^2)

def plot_confocal(theta=pi/6):
    # Ellipse parameters
    a_e = 2.0
    b_e = sqrt(3.0)
    c = sqrt(a_e*a_e - b_e*b_e)   # foci distance = 1

    # Get hyperbola parameters from C
    a2, b2 = get_hyperbola_params(theta)
    a_h = sqrt(a2)
    b_h = sqrt(b2)

    # Print hyperbola equation
    print(f"Hyperbola: x^2/{a2:.3f} - y^2/{b2:.3f} = 1")

    # Ellipse parametric curve
    t = np.linspace(0, 2*np.pi, 800)
    x_ell = a_e * np.cos(t)
    y_ell = b_e * np.sin(t)

    # Hyperbola parametric curve
    u = np.linspace(-1.2, 1.2, 600)
    sec_u = 1.0/np.cos(u)
    tan_u = np.tan(u)
    x_h_pos = a_h * sec_u
    y_h_pos = b_h * tan_u
    x_h_neg = -a_h * sec_u
    y_h_neg = b_h * tan_u

    mask_pos = np.isfinite(x_h_pos) & np.isfinite(y_h_pos) & (np.abs(x_h_pos)<50) & (np.abs(y_h_pos)<50)
    mask_neg = np.isfinite(x_h_neg) & np.isfinite(y_h_neg) & (np.abs(x_h_neg)<50) & (np.abs(y_h_neg)<50)

    # Plot
    fig, ax = plt.subplots(figsize=(8,6))
    ax.plot(x_ell, y_ell, label="Ellipse")
    ax.plot(x_h_pos[mask_pos], y_h_pos[mask_pos], linestyle='--', label="Hyperbola (right branch)")
    ax.plot(x_h_neg[mask_neg], y_h_neg[mask_neg], linestyle='--', label="Hyperbola (left branch)")
    ax.scatter([c, -c], [0,0], marker='x', s=80, label="Foci")

    ax.set_aspect('equal', 'box')
    ax.grid(True)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Ellipse and Confocal Hyperbola (via C + Python)')
    ax.legend()
    plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/8.4.29/figs/figure_1.png")
    plt.show()

# Example run
plot_confocal(theta=pi/6)

