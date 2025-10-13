import ctypes

# Define a structure equivalent to C struct Point
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

def find_circumcenter(p1: Point, p2: Point, ratio: float) -> Point:
    center = Point()
    k = ratio
    k_squared = k * k

    # Apply the same formula as in the C code
    center.x = (p1.x - k_squared * p2.x) / (1 - k_squared)
    center.y = (p1.y - k_squared * p2.y) / (1 - k_squared)

    return center

if __name__ == "__main__":
    # Define the two points
    p1 = Point(1.0, 0.0)
    p2 = Point(-1.0, 0.0)

    # Define the ratio
    ratio = 1.0 / 3.0

    # Compute the circumcenter
    circumcenter = find_circumcenter(p1, p2, ratio)

    # Print the result
    print(f"The circumcenter of the triangle ABC is at the point: ({circumcenter.x:.2f}, {circumcenter.y:.2f})")
    print("In fraction form, this is (5/4, 0).")
