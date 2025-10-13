import numpy as np
import matplotlib.pyplot as plt

def plot_locus():
    """
    Plots the two circle equations representing the locus of the point.
    """
    # Define the range for x and y
    x_range = np.linspace(-10, 10, 400)
    y_range = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x_range, y_range)

    # Define the two implicit functions for the circles
    # Equation 1: 13x^2 + 13y^2 - 83x + 64y + 172 = 0
    F1 = 13*X**2 + 13*Y**2 - 83*X + 64*Y + 172

    # Equation 2: 13x^2 + 13y^2 - 73x + 40y + 166 = 0
    F2 = 13*X**2 + 13*Y**2 - 73*X + 40*Y + 166

    plt.figure(figsize=(8, 8))

    # Plot the first circle
    plt.contour(X, Y, F1, levels=[0], colors='blue', linewidths=2)
    
    # Plot the second circle
    plt.contour(X, Y, F2, levels=[0], colors='red', linewidths=2)

    # Plot the fixed point (3, -2)
    plt.plot(3, -2, 'o', color='green', markersize=8, label='Fixed Point (3, -2)')

    # Plot the line 5x - 12y = 3
    # Rearrange to y = (5x - 3) / 12
    x_line = np.linspace(-10, 10, 100)
    y_line = (5 * x_line - 3) / 12
    plt.plot(x_line, y_line, '--', color='gray', label='Line 5x - 12y = 3')

    plt.title('Locus of the Point (Two Circles)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.axis('equal') # Ensure circles appear as circles
    plt.legend()
    plt.xlim(-5, 10) # Adjust x-axis limits for better visualization
    plt.ylim(-7, 5)  # Adjust y-axis limits for better visualization
    
    plt.show()

# Run the plotting function
plot_locus()
