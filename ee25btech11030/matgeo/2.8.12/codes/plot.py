import ctypes
import math
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object
tangent_lib = ctypes.CDLL("./func.so")

# Define the C function's argument and return types
tangent_lib.calculate_tangent.argtypes = [ctypes.c_double, ctypes.c_double]
tangent_lib.calculate_tangent.restype = ctypes.c_double

# Create a Python-callable function
calculate_tangent = tangent_lib.calculate_tangent


def plot_lines(a, b, tangent_value):
    """
    Plots the two lines and displays the tangent of the angle between them.
    """
    # Create a range of x-values for the plot.
    x_range = np.linspace(-abs(a) * 1.5, abs(a) * 1.5, 400)

    # Calculate the corresponding y-values for each line's equation.
    # Line 1: y = b * (1 - x/a)
    y1 = b * (1 - x_range / a)
    # Line 2: y = b * (x/a - 1)
    y2 = b * (x_range / a - 1)

    # Create the plot figure.
    plt.figure(figsize=(8, 8))
    plt.plot(x_range, y1, label=f'x/{a} + y/{b} = 1', color='blue')
    plt.plot(x_range, y2, label=f'x/{a} - y/{b} = 1', color='red')

    # Add plot enhancements for better visualization.
    plt.axhline(0, color='black', linewidth=0.7)
    plt.axvline(0, color='black', linewidth=0.7)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis('equal')  # Use 'equal' scaling to ensure angles are not distorted.

    # Set the plot title based on the tangent calculation result.
    if math.isnan(tangent_value):
        title = "Plot of the Lines\nTangent is undefined (lines are perpendicular)"
    else:
        title = f"Plot of the Lines\nTangent of the angle = {tangent_value:.4f}"
    plt.title(title)
    plt.savefig('figs/line.png')

    # Display the plot.
    plt.show()


def main():
    """
    Main function to define parameters, call the C function, and trigger the plot.
    """
    # Hardcoded values for 'a' and 'b'.
    a = 4.0
    b = 2.0

    # Call the C function with the hardcoded values.
    result = calculate_tangent(a, b)

    # Plot the lines using the results.
    plot_lines(a, b, result)


if __name__ == "__main__":
    main()


