import math
import numpy as np
import matplotlib.pyplot as plt

def find_common_tangents_py(c1, r1, c2, r2):
    """
    Calculates the number of common tangents between two circles using native Python.
    """
    # Calculate the distance between the centers
    d = math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)

    # Calculate the sum and difference of the radii
    r_sum = r1 + r2
    r_diff = abs(r1 - r2)
    
    # Use a small tolerance for float comparisons
    epsilon = 1e-9

    # Determine the relationship between the circles
    if d > r_sum + epsilon:
        return 4  # Circles are separate
    elif abs(d - r_sum) < epsilon:
        return 3  # Circles touch externally
    elif d > r_diff + epsilon and d < r_sum - epsilon:
        return 2  # Circles intersect
    elif abs(d - r_diff) < epsilon:
        return 1  # Circles touch internally
    elif d < r_diff - epsilon:
        return 0  # One circle is contained within the other
    elif d < epsilon and abs(r1 - r2) < epsilon:
        return -1 # Concentric and identical
    
    return 0

def plot_circles(c1, r1, c2, r2, tangency_point):
    """Plots the two circles, their centers, and the point of tangency."""
    fig, ax = plt.subplots(figsize=(10, 8))

    # Create circle patches
    circle1 = plt.Circle(c1, r1, color='blue', fill=False, linewidth=2, label=f'Circle 1: $r_1={r1}$')
    circle2 = plt.Circle(c2, r2, color='red', fill=False, linewidth=2, label=f'Circle 2: $r_2={r2}$')

    ax.add_patch(circle1)
    ax.add_patch(circle2)

    # Plot centers and label them with coordinates
    ax.plot(c1[0], c1[1], 'bo', markersize=8, label='Center $C_1$')
    ax.text(c1[0] + 0.3, c1[1] + 0.3, f'$C_1$ ({c1[0]:.1f}, {c1[1]:.1f})', fontsize=12, color='blue')
    
    ax.plot(c2[0], c2[1], 'ro', markersize=8, label='Center $C_2$')
    ax.text(c2[0] + 0.3, c2[1] + 0.3, f'$C_2$ ({c2[0]:.1f}, {c2[1]:.1f})', fontsize=12, color='red')

    # Plot tangency point and label it with coordinates
    ax.plot(tangency_point[0], tangency_point[1], 'go', markersize=8, label='Tangency Point T')
    ax.text(tangency_point[0] + 0.3, tangency_point[1] - 0.5, f'T ({tangency_point[0]}, {tangency_point[1]})', fontsize=12, color='green')

    # Set plot properties
    ax.set_aspect('equal', adjustable='box')
    plt.title('Relationship Between Two Circles (Internal Tangency)')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.grid(True)
    # Move the legend to the upper right corner
    plt.legend(loc='upper right')
    plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/10.7.76/figs/figure1.png")
    plt.show()

# --- Main execution ---
if __name__ == "__main__":
    # Parameters for the circles from the problem
    C1 = (0.0, 0.0)
    r1 = 2.0
    C2 = (3.0, 4.0)
    r2 = 7.0

    # Calculate the number of tangents using the native Python function
    num_tangents = find_common_tangents_py(C1, r1, C2, r2)
    print(f"Number of common tangents (native Python): {num_tangents}")
    
    # Calculate the point of tangency for plotting
    v = np.array(C1) - np.array(C2)
    u = v / np.linalg.norm(v)
    T = tuple(np.array(C2) + r2 * u)
    T_rounded = (round(T[0], 2), round(T[1], 2))

    # Plot the result
    plot_circles(C1, r1, C2, r2, T_rounded)
