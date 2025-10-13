import numpy as np

print("=" * 70)
print("PARABOLA PROBLEM VERIFICATION")
print("Parabola: y² = 4x")
print("Point h = (3, 0) from which three normals are drawn")
print("=" * 70)

# Given point
h = np.array([3.0, 0.0])
print(f"\nGiven point h: ({h[0]}, {h[1]})")

# For parabola y² = 4x, we have a = 1 (since 4a = 4)
a = 1.0

# Finding slopes of normals from h(3,0)
# For parabola y² = 4ax, normal at point (am², -2am) has slope m
# Equation of normal: y + 2am = m(x - am²)
# For this to pass through h(3,0): 0 + 2am = m(3 - am²)
# 2am = 3m - am³
# am³ - m + 2am = 0
# m(am² + 2a - 1) = 0  [This is wrong, let me recalculate]
# Actually: 2am = 3m - am³
# am³ - 3m + 2am = 0
# m(am² - 3 + 2a) = 0

# For a = 1: m(m² - 3 + 2) = 0 → m(m² - 1) = 0
# So m = 0, m² = 1 → m = 0, 1, -1

slopes = [0, 1, -1]
print(f"\nSlopes of normals from h to parabola: {slopes}")

# Calculate points P, Q, R on parabola
# For normal with slope m, point of contact is (am², -2am)
points = {}
points['R'] = np.array([a * slopes[0]**2, -2 * a * slopes[0]])  # (0, 0)
points['P'] = np.array([a * slopes[1]**2, -2 * a * slopes[1]])  # (1, -2)
points['Q'] = np.array([a * slopes[2]**2, -2 * a * slopes[2]])  # (1, 2)

P = points['P']
Q = points['Q']
R = points['R']

print(f"\nPoints on parabola:")
print(f"  P = ({P[0]}, {P[1]})")
print(f"  Q = ({Q[0]}, {Q[1]})")
print(f"  R = ({R[0]}, {R[1]})")

# Verify points lie on parabola y² = 4x
print("\n" + "=" * 70)
print("VERIFICATION 1: Points lie on parabola y² = 4x")
print("=" * 70)

def verify_parabola(x, y):
    lhs = y**2
    rhs = 4*x
    return lhs, rhs, abs(lhs - rhs) < 1e-10

for name, point in [('P', P), ('Q', Q), ('R', R)]:
    lhs, rhs, valid = verify_parabola(point[0], point[1])
    print(f"{name}({point[0]}, {point[1]}): y² = {lhs:.4f}, 4x = {rhs:.4f} → Valid: {valid}")

# Verify normals pass through h(3,0)
print("\n" + "=" * 70)
print("VERIFICATION 2: Normals pass through h(3,0)")
print("=" * 70)

for i, (name, point) in enumerate([('R', R), ('P', P), ('Q', Q)]):
    m = slopes[i]
    # Normal equation: y - y0 = m(x - x0)
    # At x = 3: y = m(3 - x0) + y0
    y_at_h = m * (h[0] - point[0]) + point[1]
    valid = abs(y_at_h - h[1]) < 1e-10
    print(f"Normal at {name} (slope={m}): y = {m}(x - {point[0]}) + {point[1]}")
    print(f"  At x=3: y = {y_at_h:.6f}, Expected: {h[1]} → Valid: {valid}")

# Calculate area of triangle PQR
print("\n" + "=" * 70)
print("VERIFICATION 3: Area of triangle PQR")
print("=" * 70)

# Using determinant formula
area = 0.5 * abs(P[0]*(Q[1]-R[1]) + Q[0]*(R[1]-P[1]) + R[0]*(P[1]-Q[1]))
print(f"Area = 0.5 * |det| = {area:.4f}")
print(f"Expected: 2.0")
print(f"Valid: {abs(area - 2.0) < 1e-10}")
print(f"\nAnswer: Column II-a ✓")

# Calculate side lengths
print("\n" + "=" * 70)
print("VERIFICATION 4: Side lengths")
print("=" * 70)

PQ = np.linalg.norm(P - Q)
QR = np.linalg.norm(Q - R)
RP = np.linalg.norm(R - P)

print(f"|PQ| = ||P - Q|| = ||({P[0]-Q[0]}, {P[1]-Q[1]})|| = {PQ:.4f}")
print(f"|QR| = ||Q - R|| = ||({Q[0]-R[0]}, {Q[1]-R[1]})|| = {QR:.4f} (√5 = {np.sqrt(5):.4f})")
print(f"|RP| = ||R - P|| = ||({R[0]-P[0]}, {R[1]-P[1]})|| = {RP:.4f} (√5 = {np.sqrt(5):.4f})")
print(f"\nTriangle is isosceles: |QR| = |RP| = √5")

# Calculate circumradius
print("\n" + "=" * 70)
print("VERIFICATION 5: Circumradius")
print("=" * 70)

circumradius = (PQ * QR * RP) / (4 * area)
print(f"R = (|PQ| × |QR| × |RP|) / (4 × Area)")
print(f"R = ({PQ:.4f} × {QR:.4f} × {RP:.4f}) / (4 × {area:.4f})")
print(f"R = {circumradius:.4f}")
print(f"Expected: 2.5 (5/2)")
print(f"Valid: {abs(circumradius - 2.5) < 1e-10}")
print(f"\nAnswer: Column II-b ✓")

# Calculate centroid
print("\n" + "=" * 70)
print("VERIFICATION 6: Centroid of triangle PQR")
print("=" * 70)

centroid = (P + Q + R) / 3
print(f"G = (P + Q + R) / 3")
print(f"G = (({P[0]}, {P[1]}) + ({Q[0]}, {Q[1]}) + ({R[0]}, {R[1]})) / 3")
print(f"G = ({centroid[0]:.4f}, {centroid[1]:.4f})")
print(f"Expected: (0.6667, 0) or (2/3, 0)")
print(f"Valid: {np.allclose(centroid, [2/3, 0])}")
print(f"\nAnswer: Column II-d ✓")

# Calculate circumcenter
print("\n" + "=" * 70)
print("VERIFICATION 7: Circumcenter of triangle PQR")
print("=" * 70)

# Since triangle is isosceles with P and Q having same x-coordinate
# and opposite y-coordinates, circumcenter lies on x-axis by symmetry
# Let circumcenter O = (xc, 0)
# Distance from O to all vertices must be equal

# |OP|² = |OR|²
# (xc - 1)² + 4 = xc²
# xc² - 2xc + 1 + 4 = xc²
# -2xc + 5 = 0
# xc = 5/2

xc = 5/2
circumcenter = np.array([xc, 0])

dist_OP = np.linalg.norm(circumcenter - P)
dist_OQ = np.linalg.norm(circumcenter - Q)
dist_OR = np.linalg.norm(circumcenter - R)

print(f"Circumcenter O = ({circumcenter[0]}, {circumcenter[1]})")
print(f"\nVerifying equidistance:")
print(f"  |OP| = {dist_OP:.4f}")
print(f"  |OQ| = {dist_OQ:.4f}")
print(f"  |OR| = {dist_OR:.4f}")
print(f"  All equal: {np.allclose([dist_OP, dist_OQ, dist_OR], circumradius)}")
print(f"  Equal to circumradius: {np.allclose(dist_OP, circumradius)}")
print(f"\nExpected: (2.5, 0) or (5/2, 0)")
print(f"Valid: {np.allclose(circumcenter, [5/2, 0])}")
print(f"\nAnswer: Column II-c ✓")

