import numpy as np
from libs.funcs import line_isect, line_dir_pt, param_norm
import matplotlib.pyplot as plt

# The first equation is 5x + 2y = 4
# The normal vector n1 is the coefficients of x and y
n1 = np.array([[5], [2]])
# The constant c1 is 4
c1 = 4

# The second equation is 7x + 3y = 5
# The normal vector n2 is the coefficients of x and y
n2 = np.array([[7], [3]])
# The constant c2 is 5
c2 = 5

# The line_isect function from funcs.py solves the system of equations.
# It takes the two normal vectors and two constants as input.
# The system can be represented as:
# [5 2] [x] = [4]
# [7 3] [y]   [5]
solution = line_isect(n1, c1, n2, c2)

print(f"The solution to the system of equations is:")
print(f"x = {solution[0][0]}")
print(f"y = {solution[1][0]}")

# Verification
# Let's plug the values back into the equations to check
x = solution[0][0]
y = solution[1][0]

print("\nVerification:")
print(f"5*({x}) + 2*({y}) = {5*x + 2*y}")
print(f"7*({x}) + 3*({y}) = {7*x + 3*y}")

# Plotting the lines and the intersection point
# Generate points for the first line
m1, A1 = param_norm(n1, c1)
line1_pts = line_dir_pt(m1, A1, -10, 10)

# Generate points for the second line
m2, A2 = param_norm(n2, c2)
line2_pts = line_dir_pt(m2, A2, -10, 10)

# Plot the lines
plt.plot(line1_pts[0,:], line1_pts[1,:], label='5x + 2y = 4')
plt.plot(line2_pts[0,:], line2_pts[1,:], label='7x + 3y = 5')

# Plot the intersection point
plt.plot(solution[0], solution[1], 'o', markersize=8, label=f'Intersection ({x:.2f}, {y:.2f})')

# Draw x and y axes
plt.axhline(0, color='black', linewidth=0.9)
plt.axvline(0, color='black', linewidth=0.9)

# Add labels and title for clarity
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Intersection of Two Lines")
plt.grid(True)
plt.legend()
plt.axis('equal') # Ensures the axes are scaled equally
plt.show()


