import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi, sqrt

def plot_confocal_hyperbola(theta=pi/6):
    # Ellipse parameters
    a_e = 2.0
    b_e = sqrt(3.0)
    c = sqrt(a_e*a_e - b_e*b_e)   # foci distance = 1
    
    # Hyperbola parameters
    a_h = abs(sin(theta))  # transverse semi-axis
    b_h = abs(cos(theta))  # conjugate semi-axis
    if a_h == 0:
        raise ValueError("theta leads to a_h = 0 (sin(theta)=0). Choose a different theta.")

    eq_hyperbola = f"Hyperbola: x^2/{a_h**2:.3f} - y^2/{b_h**2:.3f} = 1"
    print(eq_hyperbola)

    # Parametric ellipse
    t = np.linspace(0, 2*np.pi, 800)
    x_ell = a_e * np.cos(t)
    y_ell = b_e * np.sin(t)

    # Parametric hyperbola branches
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
    ax.set_title(r'Ellipse and Confocal Hyperbola for theta=$\pi$/6')
    ax.legend()
    plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/8.4.29/figs/Figure_1.png")
    plt.show()

# Example run with theta = pi/6
plot_confocal_hyperbola(theta=pi/6)

