from ctypes import CDLL, c_double
import os, math
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library (libcode.so must be in the same folder)
_lib_path = os.path.join(os.path.dirname(__file__), "code.so")
_lib = CDLL(_lib_path)

# Define arg and return types
_lib.angle_between.argtypes = [c_double, c_double, c_double, c_double]
_lib.angle_between.restype  = c_double

def angle_between(p, q, r, s):
    """Call the C function and return angle in radians"""
    return _lib.angle_between(p, q, r, s)

if __name__ == "__main__":
    # Specific case: p=2, q=3, r=3, s=-2
    p, q, r, s = 2, 3, 3, -2
    theta = angle_between(p, q, r, s)
    print("Angle (radians):", theta)
    print("Angle (degrees):", math.degrees(theta))

    # Pick two unit vectors with the computed angle
    # Take a = (1,0), then b = (cosθ, sinθ)
    a = np.array([1, 0])
    b = np.array([math.cos(theta), math.sin(theta)])

    # Scale them for visualization
    a_scaled = p * a
    b_scaled = q * b

    plt.figure(figsize=(6,6))
    ax = plt.gca()
    ax.set_aspect('equal')

    # Plot vectors from origin
    plt.quiver(0,0, a_scaled[0], a_scaled[1], angles='xy', scale_units='xy', scale=1, color='r', label=f'{p}a')
    plt.quiver(0,0, b_scaled[0], b_scaled[1], angles='xy', scale_units='xy', scale=1, color='b', label=f'{q}b')

    # Draw angle arc
    angle_arc = np.linspace(0, theta, 100)
    plt.plot(0.7*np.cos(angle_arc), 0.7*np.sin(angle_arc), 'k--')
    plt.text(0.9*math.cos(theta/2), 0.9*math.sin(theta/2), f"{math.degrees(theta):.0f}°")

    # Axes
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlim(-1, max(p,q)+2)
    plt.ylim(-1, max(p,q)+2)
    plt.legend()
    plt.title("Vectors and angle between them")
    plt.grid(True)
    plt.show()
