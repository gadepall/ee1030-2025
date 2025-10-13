import math

# Given points
A = (-6, 0)
C = (3, -8)
P = (-4, 6)

# Function to check collinearity using area of triangle
def are_collinear(A, C, P):
    (x1, y1), (x2, y2), (x3, y3) = A, C, P
    # Area of triangle formula: 0 if collinear
    area = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
    return area == 0

# Function to compute ratio if collinear
def division_ratio(A, C, P):
    (x1, y1), (x2, y2), (x3, y3) = A, C, P
    # Internal/external division formula
    # P divides AC in ratio m:n if (x3,y3) = (m*x2+n*x1)/(m+n), (m*y2+n*y1)/(m+n)
    # We solve for m:n
    if x1 == x2:  # vertical line
        return (y3-y1, y2-y3)
    else:
        return (x3-x1, x2-x3)

     
# Check
if are_collinear(A, C, P):
    m, n = division_ratio(A, C, P)
    if m*n > 0:
        print(f"P divides AC internally in ratio {abs(m)}:{abs(n)}")
    else:
        print(f"P divides AC externally in ratio {abs(m)}:{abs(n)}")
else:
    print("P does not divide AC (points are not collinear

