import numpy as np
import matplotlib.pyplot as plt

def find_angle_between_lines_and_plot():
    # Line 1: y - sqrt(3)x - 5 = 0
    # Slope m1 = sqrt(3)
    m1 = np.sqrt(3)

    # Line 2: sqrt(3)y - x + 6 = 0 
    # Slope m2 = 1 / np.sqrt(3)
    m2 = 1 / np.sqrt(3)

    # Calculate the angle using the formula: tan(theta) = |(m1 - m2) / (1 + m1 * m2)|
    # We use arctan2 to handle different quadrants and ensure the angle is correctly calculated
    # The angle returned by atan2 is in radians.
    angle_radians = np.arctan2(m1 - m2, 1 + m1 * m2)

    # Convert the angle from radians to degrees
    angle_degrees = np.degrees(angle_radians)

    # Ensure the angle is between 0 and 180 degrees (acute angle)
    if angle_degrees < 0:
        angle_degrees += 180.0
    if angle_degrees > 90:
        angle_degrees = 180.0 - angle_degrees

    print(f"The angle between the lines is {angle_degrees:.2f} degrees")

    # --- Plotting the lines ---

    plt.figure(figsize=(10, 8))

    # Generate x values
    x_vals = np.linspace(-10, 10, 400)

    # Calculate y values for Line 1: y = sqrt(3)x + 5
    y1_vals = m1 * x_vals + 5

    # Calculate y values for Line 2: y = (1/sqrt(3))x - 6/sqrt(3)
    y2_vals = m2 * x_vals - 6 / np.sqrt(3)

    # Plot Line 1
    plt.plot(x_vals, y1_vals, label=f'Line 1: y - $\\sqrt{{3}}$x - 5 = 0 (m={m1:.2f})', color='blue')

    # Plot Line 2
    plt.plot(x_vals, y2_vals, label=f'Line 2: $\\sqrt{{3}}$y - x + 6 = 0 (m={m2:.2f})', color='red')

    # Find the intersection point for labeling and drawing the angle
    # Set equations equal: m1*x + c1 = m2*x + c2
    # x(m1 - m2) = c2 - c1
    # x = (c2 - c1) / (m1 - m2)
    c1 = 5
    c2 = -6 / np.sqrt(3)
    
    # Check for parallel lines (m1 == m2) to avoid division by zero
    if abs(m1 - m2) > 1e-9: 
        x_intersect = (c2 - c1) / (m1 - m2)
        y_intersect = m1 * x_intersect + c1
        plt.scatter(x_intersect, y_intersect, color='green', s=100, zorder=5, label='Intersection Point')
        plt.annotate(f'({x_intersect:.2f}, {y_intersect:.2f})', 
                     (x_intersect, y_intersect), 
                     textcoords="offset points", xytext=(5,5), ha='left')
    else:
        print("The lines are parallel.")
        x_intersect = None
        y_intersect = None


    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(f'Lines and the Angle Between Them ({angle_degrees:.2f} degrees)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.ylim(-10, 10)
    plt.xlim(-10, 10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig("fig2.png")
    plt.show()

    print("Figure saved as fig2.png")

# Call the function to execute the code and generate the plot
find_angle_between_lines_and_plot()
