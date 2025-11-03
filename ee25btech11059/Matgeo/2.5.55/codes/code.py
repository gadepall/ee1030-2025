import math

MAX_POINTS = 10000
STEP = 1.0
TOL = 0.5
SIDE_LENGTH = 12.0

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def dist2(a, b):
    return (a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2

def generate_points(P, Q):
    S = []
    T = []

    x = -10
    while x <= 10:
        y = -10
        while y <= 10:
            z = -10
            while z <= 10:
                A = Point(x, y, z)
                lhs = dist2(A, P)
                rhs = dist2(A, Q)
                d = lhs - rhs

                if abs(d - 50.0) < TOL and len(S) < MAX_POINTS:
                    S.append(A)
                elif abs(-d - 50.0) < TOL and len(T) < MAX_POINTS:
                    T.append(A)
                z += STEP
            y += STEP
        x += STEP
    return S, T

def check_squares(S, T):
    print(f"Found {len(S)} points on Set S and {len(T)} points on Set T.")

    for s_point in S:
        for t_point in T:
            d = math.sqrt(dist2(s_point, t_point))
            if abs(d - SIDE_LENGTH) < TOL:
                print(f"\n✔ Found a square side of length {d:.2f}:")
                print(f"  S-point: ({s_point.x:.2f}, {s_point.y:.2f}, {s_point.z:.2f})")
                print(f"  T-point: ({t_point.x:.2f}, {t_point.y:.2f}, {t_point.z:.2f})")
                return True
    print("\n✘ No such square found with side length", SIDE_LENGTH)
    return False

def main():
    P = Point(1, 2, 3)
    Q = Point(4, 2, 7)

    S, T = generate_points(P, Q)
    check_squares(S, T)

if __name__ == "__main__":
    main()
