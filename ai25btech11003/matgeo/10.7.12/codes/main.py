import numpy as np
import matplotlib.pyplot as plt

def read_data_from_files():
    """Read data from main.dat and main.so files"""
    points = []

    # Read from main.dat
    with open('main.dat', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() and not line.startswith('#'):
                parts = line.strip().split()
                if len(parts) == 2:
                    try:
                        x, y = float(parts[0]), float(parts[1])
                        if abs(x) < 1 and abs(y) < 1:  # Filter for contact points
                            points.append((x, y))
                    except ValueError:
                        continue

    return points[:2]  # Return first two points (q1 and q2)

def plot_ellipse_with_tangents():
    """Create plot with ellipse, tangents, and labeled points"""

    # Read contact points
    contact_points = read_data_from_files()
    if len(contact_points) != 2:
        print("Error reading contact points")
        return

    q1, q2 = contact_points
    print(f"q1 = {q1}")
    print(f"q2 = {q2}")

    # Create figure
    plt.figure(figsize=(10, 8))

    # Plot ellipse 4x^2 + 9y^2 = 1
    theta = np.linspace(0, 2*np.pi, 1000)
    # From 4x^2 + 9y^2 = 1, we get x^2/(1/4) + y^2/(1/9) = 1
    # So a^2 = 1/4, b^2 = 1/9, hence a = 1/2, b = 1/3
    a, b = 1/2, 1/3
    x_ellipse = a * np.cos(theta)
    y_ellipse = b * np.sin(theta)

    plt.plot(x_ellipse, y_ellipse, 'b-', linewidth=2, label='Ellipse: 4x² + 9y² = 1')

    # Plot tangent lines
    # For ellipse 4x^2 + 9y^2 = 1, tangent at (x0, y0) is: 4x0*x + 9y0*y = 1

    # Tangent at q1
    x0, y0 = q1
    # Tangent equation: 4*x0*x + 9*y0*y = 1
    # Solve for y: y = (1 - 4*x0*x)/(9*y0)
    x_range = np.linspace(-0.8, 0.8, 100)
    if abs(y0) > 1e-10:  # Avoid division by zero
        y_tangent1 = (1 - 4*x0*x_range)/(9*y0)
        # Limit the range for visualization
        mask1 = (abs(y_tangent1) < 1)
        plt.plot(x_range[mask1], y_tangent1[mask1], 'r--', linewidth=2, label='Tangent at q1')

    # Tangent at q2
    x0, y0 = q2
    if abs(y0) > 1e-10:  # Avoid division by zero
        y_tangent2 = (1 - 4*x0*x_range)/(9*y0)
        # Limit the range for visualization
        mask2 = (abs(y_tangent2) < 1)
        plt.plot(x_range[mask2], y_tangent2[mask2], 'g--', linewidth=2, label='Tangent at q2')

    # Plot and label the contact points
    plt.plot(q1[0], q1[1], 'ro', markersize=8, label=f'q1({q1[0]:.1f}, {q1[1]:.1f})')
    plt.plot(q2[0], q2[1], 'go', markersize=8, label=f'q2({q2[0]:.1f}, {q2[1]:.1f})')

    # Add text labels near the points
    plt.annotate(f'q1(-2/5, 1/5)', xy=q1, xytext=(q1[0]-0.15, q1[1]+0.05),
                fontsize=10, ha='center', va='bottom')
    plt.annotate(f'q2(2/5, -1/5)', xy=q2, xytext=(q2[0]+0.15, q2[1]-0.05),
                fontsize=10, ha='center', va='top')

    # Plot axes
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3, linewidth=0.8)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3, linewidth=0.8)

    # Set axis labels
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)

    # Set equal aspect ratio and grid
    plt.axis('equal')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)

    # Set axis limits
    plt.xlim(-0.8, 0.8)
    plt.ylim(-0.6, 0.6)

    # Save the figure
    plt.savefig('fig1.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("Plot saved as fig1.png")

if __name__ == "__main__":
    plot_ellipse_with_tangents()
