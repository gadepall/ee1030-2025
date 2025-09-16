import matplotlib.pyplot as plt

# Coordinates of the points
points = {'A': (1, -1), 'B': (2, 1), 'C': (4, 5)}

# Extract x and y coordinates separately
x = [coord[0] for coord in points.values()]
y = [coord[1] for coord in points.values()]

# Plot the points
plt.scatter(x, y, color='deepskyblue', label='Points')

# Annotate each point with its label
for label, (x_coord, y_coord) in points.items():
    plt.annotate(label, (x_coord, y_coord), textcoords="offset points", xytext=(5,-10), ha='center')

# Plot the line through the points
plt.plot(x, y, color='red', label='Line')

# Label axes
plt.xlabel('x')
plt.ylabel('y')
plt.title('Collinear Points with Labels')

# Display legend
plt.legend()

# Show grid
plt.grid(True)

# Show plot
plt.show()
