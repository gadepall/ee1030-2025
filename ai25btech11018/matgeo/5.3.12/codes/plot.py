import numpy as np
import matplotlib.pyplot as plt

def plot_solution():
    # Define the equations of the lines
    # Line 1: x + y = 6  =>  y = 6 - x
    # Line 2: 2x - 3y = 4  =>  y = (2x - 4) / 3

    # Generate x values to plot the lines
    x = np.linspace(-10, 10, 400)

    # Calculate corresponding y values for each line
    y1 = 6 - x
    y2 = (2 * x - 4) / 3

    # The solution is x = 22/5 = 4.4 and y = 8/5 = 1.6
    solution_x = 22 / 5
    solution_y = 8 / 5

    # Set up the plot
    plt.figure(figsize=(8, 8))
    plt.title('Solution of the System of Linear Equations')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.axis('equal') # Ensures correct aspect ratio

    # Plot the lines
    plt.plot(x, y1, label='x + y = 6', color='blue')
    plt.plot(x, y2, label='2x - 3y = 4', color='red')

    # Plot and annotate the intersection point
    plt.plot(solution_x, solution_y, 'o', color='green', markersize=10, label=f'Solution ({solution_x:.1f}, {solution_y:.1f})')
    plt.annotate(f'({solution_x:.1f}, {solution_y:.1f})',
                 (solution_x, solution_y),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center')

    # Add a legend and display the plot
    plt.legend()
    plt.show()

# Run the plotting function
plot_solution()
