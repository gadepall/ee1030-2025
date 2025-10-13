import numpy as np
import matplotlib.pyplot as plt
import math

def plot_circle_solution():
    """
    Plots the two diameter lines and the resulting circle, highlighting the center.
    """
    
    ## 1. Solve for the center of the circle (intersection of the diameters)
    # The system of equations is:
    # 2x - 3y = 5
    # 3x - 4y = 7
    # Use Cramer's Rule to solve for x and y
    
    A = np.array([[2, -3], [3, -4]])
    B = np.array([5, 7])
    
    det_A = np.linalg.det(A)
    
    if det_A == 0:
        print("The lines are parallel or coincident; no unique solution exists.")
        return
        
    det_x = np.linalg.det(np.array([[5, -3], [7, -4]]))
    det_y = np.linalg.det(np.array([[2, 5], [3, 7]]))
    
    center_x = det_x / det_A
    center_y = det_y / det_A
    
    print(f"The center of the circle is at ({center_x:.2f}, {center_y:.2f})")
    
    ## 2. Calculate the radius from the area
    area = 154.0
    r_squared = area / math.pi
    radius = math.sqrt(r_squared)
    
    print(f"The radius of the circle is: {radius:.2f}")

    ## 3. Plot the solution
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Plot the diameter lines
    x_vals = np.linspace(center_x - 5, center_x + 5, 400)
    y_line1 = (2 * x_vals - 5) / 3
    y_line2 = (3 * x_vals - 7) / 4
    
    ax.plot(x_vals, y_line1, label='$2x - 3y = 5$')
    ax.plot(x_vals, y_line2, label='$3x - 4y = 7$')
    
    # Plot the circle
    circle = plt.Circle((center_x, center_y), radius, color='green', fill=False, linewidth=2, label='Circle')
    ax.add_patch(circle)
    
    # Plot the center point
    ax.plot(center_x, center_y, 'o', color='red', markersize=8, label='Center')
    ax.annotate(f'({center_x:.2f}, {center_y:.2f})', (center_x, center_y),
                textcoords="offset points", xytext=(0,10), ha='center')

    # Add labels, title, and legend
    ax.set_title('Equation of a Circle from its Diameters')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    
    plt.show()

# Run the plotting function
plot_circle_solution()