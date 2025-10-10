import matplotlib.pyplot as plt
import numpy as np

# --- Main execution part ---
if __name__ == "__main__":
    # Coordinates for the points as per the question
    A = (7, -2)
    B = (1, -5)
    P = (5, -3)   # Given trisection point
    Q = (3, -4)   # Other trisection point

    # Print the points
    print("Plotting the following points:")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"P = {P}")
    print(f"Q = {Q}\n")
    print("Displaying the graph...")

    # --- Plotting the graph ---
    # Generate a series of points on the line AB for plotting
    x_coords_line = np.linspace(A[0], B[0], 100)
    y_coords_line = np.linspace(A[1], B[1], 100)

    # Create the plot
    plt.figure(figsize=(10, 8))

    # Plot line AB
    plt.plot(x_coords_line, y_coords_line, label='Line Segment AB', color='cyan', linestyle='--')

    # Plot the points
    plt.scatter([A[0]], [A[1]], color='blue', s=150, zorder=5, label=f'Point A {A}')
    plt.scatter([B[0]], [B[1]], color='red', s=150, zorder=5, label=f'Point B {B}')
    plt.scatter([P[0]], [P[1]], color='green', s=150, zorder=5, label=f'Point P {P}')
    plt.scatter([Q[0]], [Q[1]], color='purple', s=150, zorder=5, label=f'Point Q {Q}')

    # Labels near points
    plt.text(A[0], A[1] + 0.3, 'A', fontsize=12, ha='center', color='blue')
    plt.text(B[0], B[1] + 0.3, 'B', fontsize=12, ha='center', color='red')
    plt.text(P[0], P[1] + 0.3, 'P', fontsize=12, ha='center', color='green')
    plt.text(Q[0], Q[1] + 0.3, 'Q', fontsize=12, ha='center', color='purple')

    # Titles, labels, grid
    plt.title('Trisection Points of Line Segment AB', fontsize=16)
    plt.xlabel('X-axis', fontsize=12)
    plt.ylabel('Y-axis', fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.axhline(0, color='black', linewidth=0.75)
    plt.axvline(0, color='black', linewidth=0.75)
    plt.axis('equal')
    plt.legend()

    # Save and show
    plt.savefig('trisection.png')
    plt.show()
