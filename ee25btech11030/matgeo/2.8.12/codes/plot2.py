import math
import numpy as np
import matplotlib.pyplot as plt


def calculate_tangent_py(a, b):
    """
    Calculates the tangent of the angle between the two lines directly in Python.
    The formula is derived from the slopes of the lines x/a + y/b = 1 and x/a - y/b = 1.
    """
    # Calculate the denominator of the tangent formula.
    denominator = a**2 - b**2

    # Check for division by zero, which occurs when a = b or a = -b.
    # In this case, the lines are perpendicular, and the tangent is undefined.
    if denominator == 0:
        return math.nan  # Return Not-a-Number for an undefined tangent.

    # Calculate the numerator.
    numerator = 2 * a * b

    return numerator / denominator


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
    plt.savefig('figs/line2.png')

    # Display the plot.
    plt.show()


def main():
    """
    Main function to define parameters, call the Python function, and trigger the plot.
    """
    # Hardcoded values for 'a' and 'b'.
    a = 4.0
    b = 2.0

    # Call the Python function with the hardcoded values.
    result = calculate_tangent_py(a, b)

    # Plot the lines using the results.
    plot_lines(a, b, result)


if __name__ == "__main__":
    main()


