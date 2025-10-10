import numpy as np
import matplotlib.pyplot as plt

# Solve intersection of two lines ax + by + c = 0
def intersection(a1,b1,c1, a2,b2,c2):
    A = np.array([[a1,b1],[a2,b2]])
    B = np.array([-c1,-c2])
    x, y = np.linalg.solve(A,B)
    return x, y

# Line equations
# 1) 3x - 2y + 1 = 0
# 2) 2x + 3y - 21 = 0
# 3) x - 5y + 9 = 0

# Find vertices
A = intersection(3,-2,1, 2,3,-21)
B = intersection(2,3,-21, 1,-5,9)
C = intersection(3,-2,1, 1,-5,9)

x1,y1 = A
x2,y2 = B
x3,y3 = C

# Triangle vertices for plotting
triangle_x = [x1, x2, x3, x1]
triangle_y = [y1, y2, y3, y1]

# Plotting range
x_vals = np.linspace(-5, 15, 400)

# Line 1: 3x - 2y + 1 = 0 -> y = (3x+1)/2
y1_line = (3*x_vals + 1)/2
plt.plot(x_vals, y1_line, color="blue")
plt.text(15, (3*15+1)/2, "3x-2y+1=0", fontsize=9, color="blue")  # moved right

# Line 2: 2x + 3y - 21 = 0 -> y = (21-2x)/3
y2_line = (21 - 2*x_vals)/3
plt.plot(x_vals, y2_line, color="green")
plt.text(13, (21-2*13)/3, "2x+3y-21=0", fontsize=9, color="green")

# Line 3: x - 5y + 9 = 0 -> y = (x+9)/5
y3_line = (x_vals + 9)/5
plt.plot(x_vals, y3_line, color="red")
plt.text(-2, ((-2+9)/5) - 1.0, "x-5y+9=0", fontsize=9, color="red")  # moved down

# Plot triangle
plt.fill(triangle_x, triangle_y, color="lightblue", alpha=0.5)

# Mark vertices
plt.scatter([x1,x2,x3],[y1,y2,y3], color="black", zorder=5)
plt.text(x1,y1,f"A({int(round(x1))},{int(round(y1))})", fontsize=9, ha="right")
plt.text(x2,y2,f"B({int(round(x2))},{int(round(y2))})", fontsize=9, ha="right")
plt.text(x3,y3,f"C({int(round(x3))},{int(round(y3))})", fontsize=9, ha="right")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Triangle formed by 3 lines")
plt.grid(True)
plt.axis("equal")
plt.savefig("../figs/fig8.png")
plt.show()

