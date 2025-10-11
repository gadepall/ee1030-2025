import numpy as np
import matplotlib.pyplot as plt

def line_gen_num(A, B, num_points):
    A = A.flatten()
    B = B.flatten()
    t = np.linspace(0, 1, num_points)
    points = np.outer(A, (1 - t)) + np.outer(B, t)
    return points

def plot_line_with_intercepts(mid_x, mid_y):
    # Calculate the x-intercept (a) and y-intercept (b)
    # Since (mid_x, mid_y) is the midpoint of (a, 0) and (0, b)
    # mid_x = (a + 0) / 2  => a = 2 * mid_x
    # mid_y = (0 + b) / 2  => b = 2 * mid_y
    a = 2 * mid_x
    b = 2 * mid_y

    # The equation of the line is x/a + y/b = 1
    # We can express y as: y = - (b/a) * x + b

    # Generate points for the line
    x_intercept = np.array([a, 0]).reshape(-1, 1)
    y_intercept = np.array([0, b]).reshape(-1, 1)
    
    line_points = line_gen_num(x_intercept, y_intercept, 100)

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(line_points[0, :], line_points[1, :], "blue", label=f"Line: x/{a} + y/{b} = 1")

    # Plot the intercepts
    plt.scatter([a, 0], [0, b], color='red', s=100, zorder=5)
    plt.text(a + 0.5, 0, f'({a:.0f}, 0)', color='red')
    plt.text(0.5, b + 0.5, f'(0, {b:.0f})', color='red')

    # Plot the midpoint
    plt.scatter([mid_x], [mid_y], color='green', s=100, zorder=5, label=f"Midpoint: ({mid_x}, {mid_y})")
    plt.text(mid_x + 0.5, mid_y + 0.5, f'({mid_x:.0f}, {mid_y:.0f})', color='green')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='best')
    plt.grid()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title(f"Line Intercepted by Coordinate Axes with Midpoint ({mid_x}, {mid_y})")
    plt.axis('equal')
    plt.xlim(min(0, a, mid_x) - 2, max(0, a, mid_x) + 2)
    plt.ylim(min(0, b, mid_y) - 2, max(0, b, mid_y) + 2)
    plt.savefig("fig2.png")
    plt.show()

    print(f"The x-intercept is ({a}, 0)")
    print(f"The y-intercept is (0, {b})")
    print(f"The equation of the line is x/{a} + y/{b} = 1")
    print("Figure saved as fig2.png")

# Given midpoint coordinates
mid_x_coord = 3
mid_y_coord = 2

# Call the function to plot and calculate the equation
plot_line_with_intercepts(mid_x_coord, mid_y_coord)
