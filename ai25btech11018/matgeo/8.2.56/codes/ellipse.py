import numpy as np
import matplotlib.pyplot as plt

def plot_ellipse_solution():
    # Given equation: 9x^2 + 25y^2 = 225
    
    # 1. Find a, b, e, and the foci
    a = np.sqrt(25)
    b = np.sqrt(9)
    
    eccentricity = np.sqrt(1 - (b**2 / a**2))
    
    # Distance from center to foci
    c_foci = a * eccentricity
    
    foci_coords = [(-c_foci, 0), (c_foci, 0)]
    
    print(f"Semi-major axis (a): {a}")
    print(f"Semi-minor axis (b): {b}")
    print(f"Eccentricity (e): {eccentricity:.2f}")
    print(f"Foci: ({foci_coords[0][0]:.2f}, {foci_coords[0][1]:.2f}) and ({foci_coords[1][0]:.2f}, {foci_coords[1][1]:.2f})")

    # 2. Plotting
    theta = np.linspace(0, 2 * np.pi, 100)
    x = a * np.cos(theta)
    y = b * np.sin(theta)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.plot(x, y, label=r'Ellipse $9x^2 + 25y^2 = 225$')
    
    # Plot the foci
    ax.plot(foci_coords[0][0], foci_coords[0][1], 'ro', label=f'Foci')
    ax.plot(foci_coords[1][0], foci_coords[1][1], 'ro')
    
    # Annotate the foci and center
    ax.annotate(f'({foci_coords[0][0]:.0f}, {foci_coords[0][1]:.0f})', foci_coords[0], textcoords="offset points", xytext=(-15, 10), ha='center')
    ax.annotate(f'({foci_coords[1][0]:.0f}, {foci_coords[1][1]:.0f})', foci_coords[1], textcoords="offset points", xytext=(15, 10), ha='center')
    ax.plot(0, 0, 'go', label='Center')
    
    # Add eccentricity label to the plot title
    ax.set_title(f'Ellipse with Eccentricity e = {eccentricity:.2f}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, linestyle='--')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_aspect('equal', adjustable='box')
    ax.legend()
    plt.show()

plot_ellipse_solution()