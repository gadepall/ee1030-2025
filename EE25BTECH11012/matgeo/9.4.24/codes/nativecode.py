import numpy as np
import matplotlib.pyplot as plt

# --- 1. Solve the Quadratic Equation ---

# The equation is x^2 - 55x + 750 = 0
# Coefficients for ax^2 + bx + c = 0
a = 1
b = -55
c = 750

# Calculate the roots (solutions) of the equation
solutions = np.roots([a, b, c])
solution1, solution2 = solutions[0], solutions[1]

print(f"--- Problem Solution ---")
print(f"The quadratic equation is: {a}x^2 + ({b})x + {c} = 0")
print(f"The possible number of toys produced are: {int(solution1)} and {int(solution2)}")


# --- 2. Generate Data for the Graph ---

# Create a range of x-values (number of toys) to plot
# We'll plot from 0 to 60 to get a good view of the parabola
x_values = np.linspace(0, 60, 400)

# Calculate the corresponding y-values using the quadratic function
y_values = a * x_values**2 + b * x_values + c


# --- 3. Plot the Graph ---

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the quadratic function (parabola)
ax.plot(x_values, y_values, label='Cost Function: $y = x^2 - 55x + 750$', color='dodgerblue')

# Draw a horizontal line at y=0 (x-axis) to highlight where the roots are
ax.axhline(0, color='gray', linestyle='--')

# Plot the solutions (roots) on the graph as distinct points
ax.scatter(solutions, [0, 0], color='red', zorder=5, s=100, label=f'Solutions: x={int(solution1)}, x={int(solution2)}')

# --- 4. Customize and Show the Plot ---

# Adding titles and labels
ax.set_title('Graph of the Toy Production Cost Function', fontsize=16)
ax.set_xlabel('Number of Toys Produced (x)', fontsize=12)
ax.set_ylabel('Total Cost Equation (y)', fontsize=12)

# Set plot limits to focus on the relevant area
ax.set_xlim(0, 60)
ax.set_ylim(-100, 800)

# Add annotations for the solution points
ax.annotate(f'({int(solution1)}, 0)', xy=(solution1, 0), xytext=(solution1 - 8, -70),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate(f'({int(solution2)}, 0)', xy=(solution2, 0), xytext=(solution2 + 2, -70),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Add legend and display the graph
ax.legend()
plt.show()