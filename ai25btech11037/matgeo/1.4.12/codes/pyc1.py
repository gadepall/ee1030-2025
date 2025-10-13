
import math

# Given points
A = (-6, 0)
C = (3, -8)
P = (-4, 6)

# Step 1: Compute vectors
AP = (A[0] - P[0], A[1] - P[1])
PC = (P[0] - C[0], P[1] - C[1])

# Step 2: Dot product and norm squared
dot = AP[0] * PC[0] + AP[1] * PC[1]
norm_sq = PC[0]**2 + PC[1]**2

    
k = dot / norm_sq

print(f"Computed k = {k:.3f}")

# Step 3: Collinearity check (area of triangle)
area = A[0]*(C[1]-P[1]) + C[0]*(P[1]-A[1]) + P[0]*(A[1]-C[1])

if area == 0:
    if k < 0:
        print(f"P divides AC externally in ratio {abs(int(k*7))}:{7}")
    else:
        print(f"P divides AC internally in ratio {abs(int(k*7))}:{7}")
else:
    print("P is not collinear with A and C, so it does not divide AC.")"
