import numpy as np

def reflect_point(x, y, z):
    # Normal vector of the plane
    n = np.array([1.0, 1.0, 1.0])
    d = 1.0  # plane constant
    norm_sq = np.dot(n, n)  # = 3

    q = np.array([x, y, z])
    dot = np.dot(n, q)

    # Reflection formula
    s = q - 2 * (dot - d) / norm_sq * n
    return s

# --- Main ---
if __name__ == "__main__":
    # Input point Q
    x, y, z = map(float, input("Enter coordinates of Q (x y z): ").split())

    # Compute reflection
    alpha, beta, gamma = reflect_point(x, y, z)

    # Output result
    print(f"Reflected point S = ({alpha:.6f}, {beta:.6f}, {gamma:.6f})")

