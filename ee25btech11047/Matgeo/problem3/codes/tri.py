import numpy as np
import matplotlib.pyplot as plt

# local imports
from libs.line.funcs import line_gen
from libs.triangle.funcs import *

# Coordinates of the points
A = np.array(([7, 10])).reshape(-1, 1)
B = np.array(([-2, 5])).reshape(-1, 1)
C = np.array(([3, 4])).reshape(-1, 1)

# Squared lengths of sides
AB2 = np.sum((A - B) ** 2)
AC2 = np.sum((A - C) ** 2)
BC2 = np.sum((B - C) ** 2)

# Dot products
dot_AB_AC = np.dot((A - B).T, (A - C))[0, 0]
dot_AB_BC = np.dot((A - B).T, (B - C))[0, 0]
dot_AC_BC = np.dot((A - C).T, (B - C))[0, 0]

print("Squared side lengths:")
print(f"AB^2 = {AB2}")
print(f"AC^2 = {AC2}")
print(f"BC^2 = {BC2}")

print("\nDot products:")
print(f"(A-B)·(A-C) = {dot_AB_AC}")
print(f"(A-B)·(B-C) = {dot_AB_BC}")
print(f"(A-C)·(B-C) = {dot_AC_BC}")

# Check isosceles right triangle
if ((AB2 == AC2 and dot_AB_AC == 0) or
    (AB2 == BC2 and dot_AB_BC == 0) or
    (AC2 == BC2 and dot_AC_BC == 0)):
    result = "ISOSCELES RIGHT triangle"
else:
    result = "NOT an isosceles right triangle"

print(f"\nThe points form {result}.")

# ---- Plotting ----
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

plt.plot(x_AB[0, :], x_AB[1, :], 'b')
plt.plot(x_BC[0, :], x_BC[1, :], 'b')
plt.plot(x_CA[0, :], x_CA[1, :], 'b')

# Mark points
tri_coords(A, B, C, ['A(7,10)', 'B(-2,5)', 'C(3,4)'])

# Title
plt.title(f"Triangle ABC: {result}")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
