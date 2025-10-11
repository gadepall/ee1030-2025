import numpy as np
import matplotlib.pyplot as plt

def read_data_files():
    """Read data from main.so and main.dat files created by C program"""

    # Read from main.dat file
    with open('main.dat', 'r') as f:
        lines = f.readlines()

    # Parse intersection points
    point1 = list(map(float, lines[0].strip().split()))
    point2 = list(map(float, lines[1].strip().split()))
    area = float(lines[2].strip())

    print(f"Point 1: ({point1[0]}, {point1[1]})")
    print(f"Point 2: ({point2[0]}, {point2[1]})")
    print(f"Area: {area} sq.units")

    return point1, point2, area

def create_bounded_region_plot(point1, point2, area):
    """Create the bounded region plot exactly like the reference image"""

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Define x range
    x = np.linspace(-3, 3, 1000)

    # Define the functions
    y_parabola = x**2
    y_line = x + 2

    # Plot the curves
    plt.plot(x, y_parabola, 'c-', linewidth=2, label='y = x²')
    plt.plot(x, y_line, 'r-', linewidth=2, label='y = x + 2')
    plt.axhline(y=0, color='g', linewidth=2, label='x-axis')

    # Fill the bounded region
    x_fill = np.linspace(point1[0], point2[0], 1000)
    y_parabola_fill = x_fill**2
    y_line_fill = x_fill + 2

    plt.fill_between(x_fill, y_parabola_fill, y_line_fill, 
                     alpha=0.3, color='lightblue')

    # Mark intersection points
    plt.plot(point1[0], point1[1], 'ko', markersize=8)
    plt.plot(point2[0], point2[1], 'ko', markersize=8)
    plt.plot(-2, 0, 'ko', markersize=8)  # x-intercept of line y = x + 2
    plt.plot(0, 0, 'ko', markersize=8)   # origin

    # Add point labels
    plt.annotate(f'({int(point1[0])}, {int(point1[1])})', 
                xy=(point1[0], point1[1]), xytext=(point1[0]-0.3, point1[1]+0.2),
                fontsize=12, ha='center')
    plt.annotate(f'({int(point2[0])}, {int(point2[1])})', 
                xy=(point2[0], point2[1]), xytext=(point2[0]+0.2, point2[1]+0.2),
                fontsize=12, ha='center')
    plt.annotate('(-2, 0)', xy=(-2, 0), xytext=(-2, -0.5),
                fontsize=12, ha='center')
    plt.annotate('(0, 0)', xy=(0, 0), xytext=(0.2, -0.3),
                fontsize=12, ha='left')

    # Set up the grid and axes
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)

    # Set axis limits and labels
    plt.xlim(-3, 3)
    plt.ylim(-2, 10)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)

    # Add title and legend
    plt.title('Area bounded between y=x² and y = x + 2', fontsize=16, fontweight='bold', pad=20)
    plt.legend(loc='upper left', fontsize=12)

    # Add grid lines at integer values
    plt.xticks(range(-3, 4))
    plt.yticks(range(-2, 11))

    # Make the plot look exactly like the reference
    plt.tight_layout()

    # Save the figure as fig1.png
    plt.savefig('fig1.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved as fig1.png")

    plt.show()

def main():
    """Main function that uses data from C program files"""

    print("Reading data from C program output files...")

    # Read the data from files created by C program
    point1, point2, area = read_data_files()

    print(f"\nCreating bounded region plot...")
    print(f"Area between curves: {area} sq.units")

    # Create the visualization
    create_bounded_region_plot(point1, point2, area)

    # Verify the calculation matches the PDF solution
    print(f"\nVerification:")
    print(f"From PDF: Area = 9/2 = 4.5 sq.units")
    print(f"Calculated: Area = {area} sq.units")
    print(f"Match: {'Yes' if abs(area - 4.5) < 0.001 else 'No'}")

if __name__ == "__main__":
    main()
