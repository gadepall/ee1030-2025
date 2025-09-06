import numpy as np
import matplotlib.pyplot as plt

# Define x-range
x = np.linspace(-10, 10, 400)

# Line 1: x + y = 4 => y = 4 - x
y1 = 4 - x

# Line 2: 4x + 3y = 10 => y = (10 - 4x)/3
y2 = (10 - 4*x) / 3

# Points found on L1 (x+y=4)
px = np.array([3, -7])
py = 4 - px

# Normal vector n and constants for line L2
n = np.array([4, 3])
c = 10
norm_n_sq = np.dot(n, n)

# Function to get foot of perpendicular from point to line L2
def foot_of_perpendicular(P):
    lamb = (np.dot(n, P) - c) / norm_n_sq
    Q = P - lamb * n
    return Q

# Calculate foot points Q
foot_points = np.array([foot_of_perpendicular(np.array([px[i], py[i]])) for i in range(len(px))])

plt.figure(figsize=(8,6))
plt.plot(x, y1, label=r'$x+y=4$ (L1)', color='blue')
plt.plot(x, y2, label=r'$4x+3y=10$ (L2)', color='green')
plt.scatter(px, py, color='red', zorder=5)
plt.text(3, 1, '(3,1)', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='red')
plt.text(-7, 11, '(-7,11)', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='red')

# Plot dotted lines for perpendiculars showing distance 1 unit with text, moved a bit
for i in range(len(px)):
    plt.plot([px[i], foot_points[i,0]], [py[i], foot_points[i,1]], linestyle='dotted', color='red')
    mid_x = (px[i] + foot_points[i,0]) / 2
    mid_y = (py[i] + foot_points[i,1]) / 2
    plt.text(mid_x + 0.3, mid_y + 0.3, 'dist = 1', color='red', fontsize=10,
             verticalalignment='bottom', horizontalalignment='left')

plt.xlim(-10, 10)
plt.ylim(-5, 15)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
# Save the plot to a file
plt.savefig('../figs/fig.png')

# Display the plot
plt.show()  


