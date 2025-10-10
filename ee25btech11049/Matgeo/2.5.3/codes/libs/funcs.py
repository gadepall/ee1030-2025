import numpy as np
import matplotlib.pyplot as plt

# --- Helper Functions ---

def line_gen(A, B, n=10):
    """Generates n points on a line segment between points A and B."""
    return np.array([np.linspace(A[0], B[0], n), np.linspace(A[1], B[1], n)])

def label_pts(points, labels):
    """Adds text labels to a plot for each point."""
    for i, label in enumerate(labels):
        plt.text(points[0, i] + 0.2, points[1, i] + 0.2, label, fontsize=12)

def is_right_angled_python(p1, p2, p3):
    """
    Checks if three points form a right-angled triangle using the Pythagorean theorem
    in pure Python.
    """
    # Calculate the square of the lengths of the three sides
    d1_sq = np.sum((p1 - p2)**2)
    d2_sq = np.sum((p2 - p3)**2)
    d3_sq = np.sum((p3 - p1)**2)

    # Sort the squared lengths to easily identify the potential hypotenuse
    sides_sq = sorted([d1_sq, d2_sq, d3_sq])

    # Check if a^2 + b^2 == c^2 using a tolerance for floating-point comparison
    is_right = np.isclose(sides_sq[0] + sides_sq[1], sides_sq[2])

    # Print the verification result to the console
    print("-" * 50)
    print("--- Pure Python Verification ---")
    if is_right:
        print(f"Conclusion: The points form a right-angled triangle.")
    else:
        print(f"Conclusion: The points DO NOT form a right-angled triangle.")
    print("-" * 50)
    return is_right

