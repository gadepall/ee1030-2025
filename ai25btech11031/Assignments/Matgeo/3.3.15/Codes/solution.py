import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def circle_intersections(c1, r1, c2, r2):
    dx = c2.x - c1.x
    dy = c2.y - c1.y
    d = math.hypot(dx, dy)

    if d > r1 + r2 or d < abs(r1 - r2) or d == 0:
        return []  # no intersection

    a = (r1*r1 - r2*r2 + d*d) / (2*d)
    h = math.sqrt(max(r1*r1 - a*a, 0))
    xm = c1.x + a*dx/d
    ym = c1.y + a*dy/d
    rx = -dy * (h/d)
    ry = dx * (h/d)

    p1 = Point(xm + rx, ym + ry)
    p2 = Point(xm - rx, ym - ry)

    return [p1, p2]

def main():
    # Input
    BC = float(input("Enter length BC: "))
    AD = float(input("Enter length of median AD: "))
    angleA = float(input("Enter angle A (in degrees): "))

    # Points B, C, D
    B = Point(0, 0)
    C = Point(BC, 0)
    D = Point((B.x + C.x) / 2, (B.y + C.y) / 2)

    # Circle 1: center D, radius AD
    r1 = AD

    # Angle condition: circumcircle with radius BC/(2*sinA)
    A_rad = math.radians(angleA)
    R = BC / (2.0 * math.sin(A_rad))

    # Two possible centers of angle-locus circle
    O1 = Point(D.x, D.y + R)
    O2 = Point(D.x, D.y - R)

    print("\nPossible coordinates of A:")

    # Intersections with O1 circle
    sol1 = circle_intersections(D, r1, O1, R)
    for i, p in enumerate(sol1, start=1):
        print(f"A{i} = ({p.x:.3f}, {p.y:.3f})")

    # Intersections with O2 circle
    sol2 = circle_intersections(D, r1, O2, R)
    for i, p in enumerate(sol2, start=len(sol1)+1):
        print(f"A{i} = ({p.x:.3f}, {p.y:.3f})")

if __name__ == "__main__":
    main()

