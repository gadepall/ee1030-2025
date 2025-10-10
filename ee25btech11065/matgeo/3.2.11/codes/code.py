import numpy as np
import matplotlib.pyplot as plt

# --- Problem Definition ---
# Draw a line segment of length 7.6 cm and divide it in the ratio 5:8.
# Measure the two parts.

# --- Calculations ---
total_length = 7.6
ratio_a = 5
ratio_b = 8
total_ratio_parts = ratio_a + ratio_b

# Calculate the length of each part
length_part1 = (ratio_a / total_ratio_parts) * total_length
length_part2 = (ratio_b / total_ratio_parts) * total_length

# Print the calculated measurements to the console
print(f"Total length of the line segment: {total_length} cm")
print(f"Ratio of division: {ratio_a}:{ratio_b}")
print("-" * 30)
print(f"Calculated length of the first part (5 parts): {length_part1:.2f} cm")
print(f"Calculated length of the second part (8 parts): {length_part2:.2f} cm")
print(f"Verification (Sum of parts): {length_part1 + length_part2:.2f} cm")


# --- Visualization Setup ---
# Define the coordinates for the line segment and the division point
# Let's place the line segment on the x-axis for simplicity
A = np.array([0, 0])
B = np.array([total_length, 0])
P = np.array([length_part1, 0]) # The point of division

# Create a figure and axis for the plot
plt.figure(figsize=(10, 4))
ax = plt.gca()

# --- Plot the Line and Points ---
# Plot the main line segment from A to B
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', lw=2, label=f'Total Length = {total_length} cm')

# Mark the start, end, and division points with red dots
points = {'A': A, 'P': P, 'B': B}
for label, point in points.items():
    plt.scatter(point[0], point[1], color='red', zorder=5)
    # Add labels below the points
    plt.text(point[0], point[1] - 0.2, f'{label}', ha='center', fontsize=12)

# --- Add Annotations and Labels ---
# Add labels for the two measured parts above the line segments
plt.text((A[0] + P[0]) / 2, 0.2, f'{length_part1:.2f} cm', ha='center', va='bottom', fontsize=10, color='darkgreen')
plt.text((P[0] + B[0]) / 2, 0.2, f'{length_part2:.2f} cm', ha='center', va='bottom', fontsize=10, color='purple')


# --- Set Plot Properties ---
plt.xlabel('Length (cm)')
plt.ylabel('')
plt.title('Line Segment of Length 7.6 cm Divided in the Ratio 5:8')
plt.legend(loc='best')
plt.grid(True, linestyle='--', alpha=0.6)

# Set axis limits for better viewing and remove y-axis ticks
plt.xlim(-0.5, 8.5)
plt.ylim(-1, 1)
ax.yaxis.set_major_locator(plt.NullLocator()) # Hide y-axis ticks as they are not needed

# Ensure the aspect ratio is not distorted
ax.set_aspect('equal', adjustable='box')

# Save the plot to a file
plt.savefig('divided_line_segment.png', bbox_inches='tight')

# Display the plot
plt.show()

