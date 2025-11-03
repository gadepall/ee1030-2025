import matplotlib.pyplot as plt

from call import solve_and_prepare_data

plot_data = solve_and_prepare_data()

line1_x = plot_data["line1_x"]
line1_y = plot_data["line1_y"]
line2_x = plot_data["line2_x"]
line2_y = plot_data["line2_y"]
x_sol, y_sol = plot_data["solution_point"]
a, b = plot_data["a"], plot_data["b"]

fig, ax = plt.subplots(figsize=(8, 8))

# Use the unpacked lists directly
ax.plot(line1_x, line1_y, 'r-', label=f'$\\frac{{x}}{{{a:.0f}}} - \\frac{{y}}{{{b:.0f}}} = 0$')
ax.plot(line2_x, line2_y, 'b-', label=f'${a:.0f}x + {b:.0f}y = {a**2 + b**2:.0f}$')

# Plot the intersection point
ax.scatter(x_sol, y_sol, color='black', s=100, zorder=5, label='Intersection Point')
ax.text(x_sol + 0.2, y_sol + 0.2, f'({x_sol:.0f}, {y_sol:.0f})')

ax.set_title('An Example Solution of given system of Equations')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

ax.grid(True)
ax.axis('equal')
ax.legend()
plt.show()
plt.savefig('fig1.png')
