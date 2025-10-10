import numpy as np
import matplotlib.pyplot as plt

def solve_and_plot_with_numpy():
    """
    Calculates and plots the triangle intersection using NumPy.
    """
    # --- Step 1: Define vertices as NumPy arrays ---
    # We choose A as the origin, consistent with the vector solution.
    A = np.array([0.0, 0.0])
    B = np.array([6.0, 1.0])
    C = np.array([2.0, 5.0])

    # --- Step 2: Calculate points D and E using vector arithmetic ---
    # Point D on BC such that BD:DC = 2:1
    # Vector formula: D = (1*B + 2*C) / 3
    D = (1 * B + 2 * C) / 3

    # Point E on AC such that AE:EC = 3:1
    # Vector formula: E = (1*A + 3*C) / 4
    E = (1 * A + 3 * C) / 4

    # --- Step 3: Calculate the intersection point P ---
    # From the vector solution, we found the ratio mu for the line BE is 8/11.
    # Vector formula: P = (1-mu)*B + mu*E
    mu = 8.0 / 11.0
    P = (1 - mu) * B + mu * E

    # --- Step 4: Plot the results ---
    points = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'P': P}
    
    print("Coordinates calculated by NumPy:")
    for name, coords in points.items():
        print(f"  Point {name}: ({coords[0]:.4f}, {coords[1]:.4f})")

    # Setup plot
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, linestyle=':', alpha=0.7)

    # Plot triangle, lines, and points
    triangle = plt.Polygon([A, B, C], edgecolor='darkblue', facecolor='lightblue', alpha=0.4, linewidth=2, label='Triangle ABC')
    ax.add_patch(triangle)

    ax.plot([A[0], D[0]], [A[1], D[1]], 'r--', label='Line AD')
    ax.plot([B[0], E[0]], [B[1], E[1]], 'g--', label='Line BE')

    for name, coords in points.items():
        color = 'red' if name == 'P' else 'black'
        size = 12 if name == 'P' else 8
        ax.plot(coords[0], coords[1], 'o', markersize=size, color=color, label=f'Point {name}')
        ax.text(coords[0] + 0.15, coords[1] + 0.15, name, fontsize=14, fontweight='bold', color=color)

    ax.set_title('Geometric Solution using Python and NumPy', fontsize=16)
    ax.set_xlabel('X-axis', fontsize=12)
    ax.set_ylabel('Y-axis', fontsize=12)
    ax.legend(loc="upper left")

    plt.savefig('numpy_plot.png')
    
    plt.show()

# --- Run the main function ---
if __name__ == "__main__":
    solve_and_plot_with_numpy()
