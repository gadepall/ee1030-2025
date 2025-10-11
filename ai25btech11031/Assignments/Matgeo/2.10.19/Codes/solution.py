def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def cross(a, b):
    return [
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]
    ]

# Input vectors
u = list(map(int, input("Enter vector u (x y z): ").split()))
v = list(map(int, input("Enter vector v (x y z): ").split()))
w = list(map(int, input("Enter vector w (x y z): ").split()))

# A = u · (v × w)
A = dot(u, cross(v, w))

# B = v · (u × w)
B = dot(v, cross(u, w))

# C = (v × w) · u
C = dot(cross(v, w), u)

# D = (u × v) · w
D = dot(cross(u, v), w)

# Print results
print("\nResults:")
print(f"A = u · (v × w) = {A}")
print(f"B = v · (u × w) = {B}")
print(f"C = (v × w) · u = {C}")
print(f"D = (u × v) · w = {D}")

# Check which is different
if A == C == D and B != A:
    print("\n=> Expression B is different.")
elif B == C == D and A != B:
    print("\n=> Expression A is different.")
elif A == B == D and C != A:
    print("\n=> Expression C is different.")
elif A == B == C and D != A:
    print("\n=> Expression D is different.")
else:
    print("\n=> No unique difference found (all may be equal or zero).")
