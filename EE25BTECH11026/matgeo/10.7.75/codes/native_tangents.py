import numpy as np
import matplotlib.pyplot as plt

def tangents_from_origin(r, h):
    """
    Finds tangent lines from origin to the circle
    x^2 + y^2 - 2rx - 2hy + h^2 = 0.
    
    Returns:
        tangents: list of (a,b) representing ax+by=0
        tangent_eqs: list of pretty string equations
    """
    tangents = []
    tangent_eqs = []

    # Case 1: x=0
    tangents.append((1, 0))
    tangent_eqs.append("x = 0")

    # Case 2
    if (h**2 - r**2) != 0:
        a, b = (h**2 - r**2, -2*r*h)
        tangents.append((a, b))
        tangent_eqs.append(f"{a}x {b:+}y = 0")
    else:
        tangents.append((0, 1))
        tangent_eqs.append("y = 0")

    return tangents, tangent_eqs


def plot_tangents(r, h):
    tangents, tangent_eqs = tangents_from_origin(r, h)

    # Print immediately
    print("Tangents from origin:")
    for eq in tangent_eqs:
        print("   ", eq)

    # Circle: center = (r,h), radius = r
    theta = np.linspace(0, 2*np.pi, 400)
    x_circ = r + r*np.cos(theta)
    y_circ = h + r*np.sin(theta)

    plt.figure(figsize=(6,6))
    plt.plot(x_circ, y_circ, 'b', label="Circle")

    # Tangents
    x_vals = np.linspace(-2*r, 2*r, 400)
    for (a,b), eq in zip(tangents, tangent_eqs):
        if b == 0:
            plt.axvline(0, color='r', linestyle='--', label=eq)
        else:
            y_vals = -(a/b)*x_vals
            plt.plot(x_vals, y_vals, 'r--', label=eq)

    # Mark origin & center
    plt.scatter([0],[0], color='k', marker='o', label="Origin (0,0)")
    plt.scatter([r],[h], color='g', marker='x', label=f"Center ({r},{h})")

    plt.gca().set_aspect('equal', adjustable='box')
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.legend()
    plt.title(f"Tangents from Origin to Circle (r={r}, h={h})")
    plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/10.7.75/figs/Figure_1.png")
    plt.show()


# Example usage
plot_tangents(r=3, h=4)

