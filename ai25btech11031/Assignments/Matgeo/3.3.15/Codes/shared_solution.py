import ctypes
import math

# Load the shared library
lib = ctypes.CDLL("./solution.so")

# Define Point struct for Python
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

# Set argument and return types
lib.circle_intersections.argtypes = [Point, ctypes.c_double, Point, ctypes.c_double,
                                     ctypes.POINTER(Point), ctypes.POINTER(Point)]
lib.circle_intersections.restype = ctypes.c_int

def circle_intersections(c1, r1, c2, r2):
    p1, p2 = Point(), Point()
    count = lib.circle_intersections(c1, r1, c2, r2,
                                     ctypes.byref(p1), ctypes.byref(p2))
    if count == 2:
        return [p1, p2]
    return []

def main():
    BC = float(input("Enter length BC: "))
    AD = float(input("Enter length of median AD: "))
    angleA = float(input("Enter angle A (in degrees): "))

    # B, C, D
    B = Point(0, 0)
    C = Point(BC, 0)
    D = Point((B.x + C.x) / 2, (B.y + C.y) / 2)

    r1 = AD
    A_rad = math.radians(angleA)
    R = BC / (2.0 * math.sin(A_rad))

    O1 = Point(D.x, D.y + R)
    O2 = Point(D.x, D.y - R)

    print("\nPossible coordinates of A:")

    sol1 = circle_intersections(D, r1, O1, R)
    for i, p in enumerate(sol1, start=1):
        print(f"A{i} = ({p.x:.3f}, {p.y:.3f})")

    sol2 = circle_intersections(D, r1, O2, R)
    for i, p in enumerate(sol2, start=len(sol1)+1):
        print(f"A{i} = ({p.x:.3f}, {p.y:.3f})")

if __name__ == "__main__":
    main()

