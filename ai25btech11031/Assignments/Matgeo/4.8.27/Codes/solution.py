import numpy as np

def cross_product(v1, v2):
    """Return cross product of two vectors"""
    return np.cross(v1, v2)

def dot_product(v1, v2):
    """Return dot product of two vectors"""
    return np.dot(v1, v2)

def plane_equation(normal, point):
    """Given normal vector and point, return plane equation coefficients"""
    d = dot_product(normal, point)
    return (*normal, d)

def main():
    # Input point
    x0, y0, z0 = map(float, input("Enter point (x0 y0 z0): ").split())

    # Input first plane coefficients
    a1, b1, c1, d1 = map(float, input("Enter coefficients of plane1 (a1 b1 c1 d1): ").split())

    # Input second plane coefficients
    a2, b2, c2, d2 = map(float, input("Enter coefficients of plane2 (a2 b2 c2 d2): ").split())

    # Normals of plane1 and plane2
    n1 = np.array([a1, b1, c1])
    n2 = np.array([a2, b2, c2])

    # Required normal vector is cross product
    n_required = cross_product(n1, n2)

    # Given point
    p = np.array([x0, y0, z0])

    # Plane equation: n·x = d
    a, b, c, d = plane_equation(n_required, p)

    print(f"\nRequired plane equation:")
    print(f"{a:.2f}x + {b:.2f}y + {c:.2f}z = {d:.2f}")

if __name__ == "__main__":
    main()

