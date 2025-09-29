import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from libs.funcs import * 
from libs.params import * 

# The vector a = (1, 1, 2) is now defined in params.py
# This script calculates its unit vector and creates a 3D plot for visualization.

try:
    # Calculate the unit vector using the function from funcs.py
    a, magnitude_a, unit_a = calculate_unit_vector(a_vector)

    # Print the results
    print(f"Original vector a: {a}")
    print(f"Magnitude of a: {magnitude_a:.4f}")
    print(f"Unit vector â: {unit_a}")
    print(f"Magnitude of the unit vector: {np.linalg.norm(unit_a):.4f}")


    # --- Plotting the Vectors ---

    # Create the 3D plot
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the original vector 'a' in blue
    ax.quiver(0, 0, 0, a[0], a[1], a[2], color='b', arrow_length_ratio=0.1, label=f'Vector a = {a}')

    # Plot the unit vector 'â' in red
    ax.quiver(0, 0, 0, unit_a[0], unit_a[1], unit_a[2], color='r', arrow_length_ratio=0.2, label=f'Unit Vector â ≈ [{unit_a[0]:.2f}, {unit_a[1]:.2f}, {unit_a[2]:.2f}]')

    # Set the plot limits for better visualization
    limit = max(np.max(np.abs(a)), 1.5)
    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit])
    ax.set_zlim([0, limit])

    # Set plot title and labels
    ax.set_title('Unit Vector in 3D', fontsize=16)
    ax.set_xlabel('x-axis', fontsize=12)
    ax.set_ylabel('y-axis', fontsize=12)
    ax.set_zlabel('z-axis', fontsize=12)

    # Add a legend
    ax.legend(fontsize=12)

    # Set the view angle
    ax.view_init(elev=20., azim=30)

    # Display the plot
    plt.show()

except (ValueError, NameError) as e:
    print(f"An error occurred: {e}")
    print("Please ensure that 'params.py' contains 'a_vector' and 'funcs.py' contains 'calculate_unit_vector'.")


