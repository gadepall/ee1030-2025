import numpy as np
import matplotlib.pyplot as plt

def plot_vectors(ax, points, title):
    """
    Helper function to plot the points, vectors, and calculate the cross product sum.
    """
    # Define colors for points A, B, C
    colors = ['r', 'g', 'b']
    
    # Position vectors are the same as the point coordinates
    a, b, c = points[0], points[1], points[2]
    
    # --- Calculations ---
    # Calculate the three cross products
    axb = np.cross(a, b)
    bxc = np.cross(b, c)
    cxa = np.cross(c, a)
    
    # Sum the resulting vectors
    sum_of_cross_products = axb + bxc + cxa
    
    # --- Plotting ---
    # Plot the origin
    ax.scatter(0, 0, 0, color='black', s=50, label='Origin')
    
    # Plot the points A, B, and C
    for i, (point, label) in enumerate(zip(points, ['A', 'B', 'C'])):
        ax.scatter(point[0], point[1], point[2], color=colors[i], s=50, label=f'Point {label}')
        # Draw the position vector from the origin to the point
        ax.quiver(0, 0, 0, point[0], point[1], point[2], color=colors[i], arrow_length_ratio=0.1, linewidth=1.5)

    # Connect the points with a line or triangle
    all_points = np.array(points + [points[0]]) # Add first point to the end to close the shape
    ax.plot(all_points[:,0], all_points[:,1], all_points[:,2], color='grey', linestyle='--')

    # Configure plot appearance
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.legend()
    
    # Set the title with the result of the calculation
    # Format the vector sum to be easy to read
    result_str = np.array2string(sum_of_cross_products, formatter={'float_kind':lambda x: "%.1f" % x})
    ax.set_title(f'{title}\nResult of (a×b)+(b×c)+(c×a) = {result_str}', fontsize=10)

# --- Define the two scenarios ---

# Case 1: Three points that lie on the same line
collinear_points = [
    np.array([2, 3, 4]),
    np.array([4, 6, 8]),   # This is 2 * the first point
    np.array([6, 9, 12])  # This is 3 * the first point
]

# Case 2: Three points that form a triangle
non_collinear_points = [
    np.array([4, 1, 5]),
    np.array([1, 5, 2]),
    np.array([-2, 2, 7])
]

# --- Create the plots ---
fig = plt.figure(figsize=(14, 7))

# First subplot for the collinear case
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
plot_vectors(ax1, collinear_points, 'Case 1: Collinear Points')
ax1.view_init(elev=20, azim=30) # Adjust viewing angle

# Second subplot for the non-collinear case
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
plot_vectors(ax2, non_collinear_points, 'Case 2: Non-Collinear Points')
ax2.view_init(elev=20, azim=30) # Adjust viewing angle

# Show the plots
plt.tight_layout()
plt.show()

