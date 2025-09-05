import matplotlib.pyplot as plt
import numpy as np

# This script plots the specified 2D points and the line segment connecting A and B.

# --- Main execution part ---
if __name__ == "__main__":
    # Coordinates for the points to be plotted as per the request
    A = (2, -2)
    B = (-7, 4)
    Q = (-4, 2)
    P = (-1, 0)

    # Print the points that will be plotted
    print("Plotting the following points:")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"Q = {Q}")
    print(f"P = {P}\n")
    print("Displaying the graph...")

    # --- Plotting the graph ---

    # Generate a series of points on the line from A to B for plotting the line segment
    x_coords_line = np.linspace(A[0], B[0], 100)
    y_coords_line = np.linspace(A[1], B[1], 100)

    # Create the plot
    plt.figure(figsize=(10, 8))

    # Plot the line segment connecting A and B
    plt.plot(x_coords_line, y_coords_line, label='Line Segment AB', color='cyan', linestyle='--')

    # Plot the individual points
    plt.scatter([A[0]], [A[1]], color='blue', s=150, zorder=5, label=f'Point A {A}')
    plt.scatter([B[0]], [B[1]], color='red', s=150, zorder=5, label=f'Point B {B}')
    plt.scatter([Q[0]], [Q[1]], color='purple', s=150, zorder=5, label=f'Point Q {Q}')
    plt.scatter([P[0]], [P[1]], color='green', s=150, zorder=5, label=f'Point P {P}')
    
    # Add text labels for each point for clarity
    plt.text(A[0], A[1] + 0.3, 'A', fontsize=12, ha='center', color='blue')
    plt.text(B[0], B[1] + 0.3, 'B', fontsize=12, ha='center', color='red')
    plt.text(Q[0], Q[1] + 0.3, 'Q', fontsize=12, ha='center', color='purple')
    plt.text(P[0], P[1] + 0.3, 'P', fontsize=12, ha='center', color='green')

    # Add graph titles and labels
    plt.title('Plot of Points in 2D Space', fontsize=16)
    plt.xlabel('X-axis', fontsize=12)
    plt.ylabel('Y-axis', fontsize=12)

    # Add grid and make axes equal for a true representation
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.axhline(0, color='black', linewidth=0.75)
    plt.axvline(0, color='black', linewidth=0.75)
    plt.axis('equal')
    plt.legend()

    # Show the plot
    plt.savefig('2.png')
    plt.show()
