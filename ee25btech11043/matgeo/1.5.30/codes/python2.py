import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt


def line_gen_num(A, B, num_points):
    
    A = A.flatten()
    B = B.flatten()
    t = np.linspace(0, 1, num_points)
    points = np.outer(A, (1-t)) + np.outer(B, t)
    return points


def circ_gen(center, radius, num_points=100):
   
    center = center.flatten()
    theta = np.linspace(0, 2*np.pi, num_points)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    return np.array([x, y])

# Given coordinates
B = np.array([2, 3]).reshape(-1, 1)  # One end of the diameter (let's call it B)
P = np.array([-2, 5]).reshape(-1, 1) # Center of the circle (let's call it P)

# Function to calculate the other end of the diameter
def func_other_end(center, one_end):
    return 2 * center - one_end

# Function to calculate the radius
def func_radius(center, point_on_circumference):
    return LA.norm(center - point_on_circumference)

# Calculate the other end of the diameter (A)
A = func_other_end(P, B).reshape(-1, 1)

# Calculate the radius of the circle
radius = func_radius(P, B)

print(f"The coordinates of the other end of the diameter are ({A[0,0]}, {A[1,0]})")

# Generate points for the diameter line
x_AB = line_gen_num(A, B, 20)

# Generate points for the circle
x_circ = circ_gen(P, radius)

# Plotting
plt.plot(x_circ[0,:], x_circ[1,:], "red", label="Circle")
plt.plot(x_AB[0,:], x_AB[1,:], "g--", label="Diameter")

# Plot the points
tri_coords = np.block([[A, B, P]])
plt.scatter(tri_coords[0,:], tri_coords[1,:], s=50, zorder=5)

# Add labels to the points
vert_labels = [f'A({A[0,0]:.0f},{A[1,0]:.0f})', f'B({B[0,0]:.0f},{B[1,0]:.0f})', f'P({P[0,0]:.0f},{P[1,0]:.0f}) (Center)']
for i , txt in enumerate(vert_labels):
    plt.annotate(txt, (tri_coords[0,i], tri_coords[1,i]), textcoords="offset points", xytext=(5,5), ha='left')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.title("Diameter of a Circle")
plt.axis('equal') # Important to make the circle appear circular
plt.savefig("fig1.png")
plt.show()

print("Figure saved as fig1.png")
