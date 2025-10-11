import numpy as np
import matplotlib.pyplot as plt

def solve_and_plot_native():
    """
    Solves for eigenvectors using NumPy and plots the visualization.
    """
    print("--- 1. Native Python Solution ---")
    
    # Define the matrix
    A = np.array([[4, 3], 
                  [9, -2]])

    # Calculate eigenvalues and eigenvectors
    # The function returns eigenvalues and a matrix where columns are the eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)

    print("Matrix A:\n", A)
    print("\nEigenvalues:\n", eigenvalues)
    print("\nEigenvectors (as columns):\n", eigenvectors)

    # --- Plotting ---
    # Extract the eigenvectors for plotting (corresponding to options a and c)
    # Note: np.linalg.eig might return vectors with different signs or normalization,
    # but they will be on the same line. We'll use the ones from the problem for consistency.
    v1 = np.array([1, 1])   # Corresponds to λ=7
    v2 = np.array([2, -6])  # Corresponds to λ=-5
    
    # A non-eigenvector for comparison
    v_other = np.array([3, 4])
    
    # Apply the transformation A to the vectors
    Av1 = A @ v1
    Av2 = A @ v2
    Av_other = A @ v_other

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 10))

    # Eigenvector 1 (λ=7)
    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Eigenvector $\\vec{v_1}$ for $\\lambda=7$')
    ax.quiver(0, 0, Av1[0], Av1[1], angles='xy', scale_units='xy', scale=1, color='cyan', alpha=0.8, label='$A\\vec{v_1}$ (Scaled by 7)')

    # Eigenvector 2 (λ=-5)
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', label='Eigenvector $\\vec{v_2}$ for $\\lambda=-5$')
    ax.quiver(0, 0, Av2[0], Av2[1], angles='xy', scale_units='xy', scale=1, color='magenta', alpha=0.8, label='$A\\vec{v_2}$ (Scaled by -5)')
    
    # Non-eigenvector
    ax.quiver(0, 0, v_other[0], v_other[1], angles='xy', scale_units='xy', scale=1, color='green', label='Non-Eigenvector $\\vec{v_3}$')
    ax.quiver(0, 0, Av_other[0], Av_other[1], angles='xy', scale_units='xy', scale=1, color='lime', alpha=0.8, label='$A\\vec{v_3}$ (Direction Changed)')

    # Set plot limits and labels
    ax.set_xlim([-15, 30])
    ax.set_ylim([-20, 35])
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Visualization of Eigenvector Transformation (Native Python)")
    ax.axhline(0, color='grey', lw=0.5)
    ax.axvline(0, color='grey', lw=0.5)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')
    ax.legend()
    
    plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/12.41/figs/figure1.png")
    plt.show()

if __name__ == '__main__':
    solve_and_plot_native()
