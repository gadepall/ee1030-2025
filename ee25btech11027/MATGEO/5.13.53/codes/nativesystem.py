import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gaussian_elimination(A_in, B_in):
    """
    Performs Gaussian elimination to check consistency.
    """
    # Create the augmented matrix
    M = np.hstack((A_in, B_in.reshape(-1, 1)))
    n = M.shape[0]
    TOLERANCE = 1e-9

    for i in range(n):
        # Pivot (Find row with max value for robust elimination)
        pivot_row = i
        for k in range(i + 1, n):
            if abs(M[k, i]) > abs(M[pivot_row, i]):
                pivot_row = k
        M[[i, pivot_row]] = M[[pivot_row, i]] # Swap rows

        # Check for zero pivot after swapping
        if abs(M[i, i]) < TOLERANCE:
            continue

        # Elimination
        for k in range(i + 1, n):
            factor = M[k, i] / M[i, i]
            M[k, i:] -= factor * M[i, i:]
            
    # Check for inconsistency (Row [0 0 0 | k] where k != 0)
    # The last row should be checked
    if abs(M[n-1, n-1]) < TOLERANCE and abs(M[n-1, n]) > TOLERANCE:
        return M, "NO SOLUTION"
    
    return M, "SOLVABLE"

# Augmented Matrix for the inconsistent system (lambda = 1)
A_matrix = np.array([
    [2.0, -1.0, 2.0],
    [1.0, -2.0, 1.0],
    [1.0, 1.0, 1.0]
])
B_vector = np.array([2.0, -4.0, 4.0])

final_matrix, consistency = gaussian_elimination(A_matrix, B_vector)

print("--- Native Python Result (Gaussian Elimination) ---")
print(f"System tested with lambda = 1.")
print(f"Consistency Check: {consistency}")
print("\nFinal Matrix after Native Python Gaussian Elimination:")
print(final_matrix)

# Equations for the three planes (lambda=1)
# P1: 2x - y + 2z = 2
# P2: x - 2y + z = -4
# P3: x + y + z = 4

def plot_planes():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Define the range for x and y
    x_range = np.linspace(-5, 5, 50)
    y_range = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x_range, y_range)

    # Calculate z for each plane
    # P1: z = (2 - 2x + y) / 2
    Z1 = (2 - 2*X + Y) / 2
    
    # P2: z = -4 - x + 2y
    Z2 = -4 - X + 2*Y

    # P3: z = 4 - x - y
    Z3 = 4 - X - Y

    # Plot the planes
    ax.plot_surface(X, Y, Z1, alpha=0.5, color='cyan', label='Plane 1')
    ax.plot_surface(X, Y, Z2, alpha=0.5, color='red', label='Plane 2')
    ax.plot_surface(X, Y, Z3, alpha=0.5, color='yellow', label='Plane 3')

    # Customize the plot appearance
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Inconsistent System (No Solution) Planes for $\lambda=1$')
    
    # Manually create a legend placeholder since plot_surface doesn't auto-legend well
    # The planes will visually show a triangular tunnel (no single intersection point)

    plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/5.13.53/figs/figure1.png")
    plt.show()

# plot_planes() # Uncomment this line to run the plot command
# When run, this will display the 3D graph showing the three planes 
# forming a triangular prism, which is the geometric representation of "NO SOLUTION."
