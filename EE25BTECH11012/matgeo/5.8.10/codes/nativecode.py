import matplotlib.pyplot as plt
import numpy as np

# Create a range of x-values (Narayan's age) to plot over
# np.linspace creates an array of evenly spaced numbers over a specified interval
x = np.linspace(0, 60, 400)

# --- Define the Equations ---
# We rearrange the original equations to solve for y, the standard y = f(x) format for plotting.

# Equation 1 from "Seven years ago...": x - 7y = -42  =>  y = (x + 42) / 7
y1 = (x + 42) / 7

# Equation 2 from "Three years from now...": x - 3y = 6   =>  y = (x - 6) / 3
y2 = (x - 6) / 3

# --- Plotting the Graph ---

# Set up the plot size for better visibility
plt.figure(figsize=(10, 8))

# Plot the two lines representing the equations
plt.plot(x, y1, label='x - 7y = -42 (Seven years ago)')
plt.plot(x, y2, label='x - 3y = 6 (Three years from now)')

# --- Mark the Solution ---
# The solution to the problem is the single point where the two lines intersect.
# We can calculate this point algebraically and plot it.
intersection_x = 42
intersection_y = 12
plt.plot(intersection_x, intersection_y, 'ro', label=f'Intersection ({intersection_x}, {intersection_y})') # 'ro' means red circle

# --- Formatting the Graph for Clarity ---

# Add a title and labels for the x and y axes
plt.title("Graphical Solution to the Age Problem", fontsize=16)
plt.xlabel("Narayan's Current Age (x)", fontsize=12)
plt.ylabel("Daughter's Current Age (y)", fontsize=12)

# Display the legend to identify each line
plt.legend()

# Add a grid to make the coordinates easier to read
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Set the visible range for the axes to focus on the solution area
plt.xlim(0, 50)
plt.ylim(0, 20)

# Add an annotation with an arrow to clearly point out the solution
plt.annotate(
    f'Solution: ({intersection_x}, {intersection_y})', # The text to display
    xy=(intersection_x, intersection_y),              # The point to annotate
    xytext=(intersection_x - 15, intersection_y + 3), # Where to place the text
    arrowprops=dict(facecolor='black', shrink=0.05),  # Arrow style
    fontsize=12
)

# Save the finished plot to a PNG image file
plt.savefig('age_problem_solution_graph.png')

print("Graph has been successfully generated and saved as age_problem_solution_graph.png")