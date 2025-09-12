import matplotlib.pyplot as plt
import math

# Given points
points = [(7, -4), (9, 0), (5, 0)]

# Function to calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distances between (7, -4) to (9, 0) and (7, -4) to (5, 0)
d1 = distance(points[0], points[1])
d2 = distance(points[0], points[2])

# Extract x and y coordinates for plotting
x_coords, y_coords = zip(*points)

# Plot the points
plt.figure(figsize=(6, 6))
plt.scatter(x_coords, y_coords, color='blue')

# Annotate the points
for (x, y) in points:
    plt.text(x + 0.1, y + 0.1, f"({x}, {y})", fontsize=9)

# Draw dashed lines for the distances
plt.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], 'r--', 
         label=f'Distance A-B: {d1:.2f}')
plt.plot([points[0][0], points[2][0]], [points[0][1], points[2][1]], 'g--', 
         label=f'Distance A-C: {d2:.2f}')

# Add labels, legend, and grid
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Distance Comparison between Points')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Show the plot
plt.show()

# Print distances
print("Distance from (7, -4) to (9, 0):", d1)
print("Distance from (7, -4) to (5, 0):", d2)
