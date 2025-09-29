import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# Define a function to generate points for a line segment
def line_gen_num(point1, point2, num_points):
    point1 = np.array(point1).flatten()
    point2 = np.array(point2).flatten()
    t = np.linspace(0, 1, num_points)
    # Using broadcasting to get all points along the line
    # Each column will be a point [x, y]
    points = np.outer(point1, (1 - t)) + np.outer(point2, t)
    return points

# Given vertices
A_coords = np.array([5, -6])
B_coords = np.array([6, 4])
C_coords = np.array([0, 0])

# 1. Find the midpoint D of BC
# D = ( (Bx + Cx) / 2, (By + Cy) / 2 )
D_x = (B_coords[0] + C_coords[0]) / 2
D_y = (B_coords[1] + C_coords[1]) / 2
D_coords = np.array([D_x, D_y])

print(f"Coordinates of D (midpoint of BC): ({D_coords[0]:.2f}, {D_coords[1]:.2f})")

# Find the length of the median AD
# Length = sqrt( (Dx - Ax)^2 + (Dy - Ay)^2 )
length_AD = LA.norm(D_coords - A_coords)

print(f"The length of the median AD is: {length_AD:.2f}")

# Plotting
plt.figure(figsize=(10, 8))

# Plot triangle sides
# Line AB
x_AB = line_gen_num(A_coords, B_coords, 2) # Only 2 points for a straight line
plt.plot(x_AB[0,:], x_AB[1,:], 'k-', label='Side AB')
# Line BC
x_BC = line_gen_num(B_coords, C_coords, 2)
plt.plot(x_BC[0,:], x_BC[1,:], 'k-', label='Side BC')
# Line CA
x_CA = line_gen_num(C_coords, A_coords, 2)
plt.plot(x_CA[0,:], x_CA[1,:], 'k-', label='Side CA')

# Plot median AD
x_AD = line_gen_num(A_coords, D_coords, 2)
plt.plot(x_AD[0,:], x_AD[1,:], 'g--', label=f'Median AD (Length: {length_AD:.2f})')

# Plot vertices
all_coords = np.block([[A_coords.reshape(-1,1), B_coords.reshape(-1,1), C_coords.reshape(-1,1), D_coords.reshape(-1,1)]])
plt.scatter(all_coords[0,:], all_coords[1,:], s=100, zorder=5) # Larger dots for vertices

# Add labels to the points
vert_labels = [
    f'A( {A_coords[0]:.0f},{A_coords[1]:.0f} )',
    f'B( {B_coords[0]:.0f},{B_coords[1]:.0f} )',
    f'C( {C_coords[0]:.0f},{C_coords[1]:.0f} )',
    f'D( {D_coords[0]:.0f},{D_coords[1]:.0f} )(Midpoint of BC)'
]
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, (all_coords[0,i], all_coords[1,i]), textcoords="offset points", xytext=(5,5), ha='left')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid(True)
plt.title("Triangle ABC and Median AD")
plt.axis('equal') # Ensures correct aspect ratio
plt.savefig("fig2.png")
plt.show()

print("Figure saved as fig2.png")
