import matplotlib.pyplot as plt

# --- Data ---
# Define the x and y coordinates for the points.
points = [(5, 1), (-2, -3), (8, 19/7)]

# Sort the points based on the x-coordinate to ensure the line is drawn correctly.
points.sort()

# Unzip the sorted points into separate lists for x and y coordinates.
x_coords, y_coords = zip(*points)

# --- Plotting ---
# Create a new figure and axes for the plot.
plt.figure(figsize=(8, 6))

# Create a scatter plot of the points.
# 's=100' sets the size of the markers, and 'c='red'' sets their color.
plt.scatter(x_coords, y_coords, s=100, c='red', zorder=5, label='Points')

# Draw a line connecting the points.
# 'zorder=1' ensures the line is drawn behind the points.
plt.plot(x_coords, y_coords, c='blue', zorder=1, label='Line')


# Add labels to each point for clarity.
# We loop through each point and add a text label slightly offset from the point itself.
for x, y in points:
    # The label format is (x, y)
    # The 19/7 is formatted to two decimal places for readability.
    label = f"({x}, {y:.2f})" if y == 19/7 else f"({x}, {y})"
    plt.text(x + 0.3, y + 0.3, label, fontsize=9)

# --- Customization ---
# Set the title of the plot.
plt.title('Plot of Given Coordinates with Connecting Line')

# Set the labels for the x and y axes.
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a grid to the plot for better readability.
plt.grid(True)

# Add a legend to the plot.
plt.legend()

# Ensure the axes are scaled equally and include the origin (0,0).
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')



# --- Display the Plot ---
# Show the final plot.
plt.show()

