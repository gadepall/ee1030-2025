import numpy as np
import matplotlib.pyplot as plt

# Define the vertices of the triangle
points = np.array([
    [5, -2],   # A
    [6, 4],   # B
    [7, -2], # C

])
M=np.array([6,-2])

# Close the triangle (repeat first point)
points = np.vstack([points, points[0]])

#scatter
plt.text(points[0,0]+0.2, points[0,1]+0.2, "A(5,-2)", fontsize=12, ha='right')
plt.text(points[1,0], points[1,1], "B(6,4)", fontsize=12, ha='right')
plt.text(points[2,0]+0.2, points[2,1]+0.2, "C(7,-2)", fontsize=12, ha='left')
plt.text(M[0]+0.2, M[1]+0.2, "M(6,-2)", fontsize=12, ha='center')

# Plot
plt.plot([M[0],points[1,0]],[M[1],points[1,1]],"go-",linewidth=2)
plt.plot(points[:,0], points[:,1], "bo-", linewidth=2)
plt.xlim([2,9])
plt.ylim([-4,6])
plt.title("isosceles triangle")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect("equal")
plt.grid(True)
plt.savefig('figs/triangle2.png')
plt.show()
