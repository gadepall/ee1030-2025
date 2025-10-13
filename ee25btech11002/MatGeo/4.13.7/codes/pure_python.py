import numpy as np
import matplotlib.pyplot as plt

# Fixed point
fixed_point = (1, -2)

# Create figure
plt.figure(figsize=(7,7))

# Define the (a, d) pairs
lines = [(1, -1), (2, -1), (1, 0)]
colors = ['blue', 'green', 'purple']

x = np.linspace(-5, 5, 400)

for i, (a, d) in enumerate(lines):
    b = a + d
    c = a + 2*d
    
    if b != 0:
        y = (-a*x - c)/b
        plt.plot(x, y, color=colors[i], linewidth=1.5)
        # Proper label placement inside plot
        # Choose different locations for each line
        if i == 0:
            # This block is not used for the given line data, but is kept for completeness
            plt.text(-4, 4, f'x = 1', fontsize=10, color=colors[i])
            plt.plot(x, y, color=colors[i], linewidth=1.5, 
            label=f"(a={a}, d={d})")   # <-- add label
        elif i == 1:
            # Corrected coordinates for the green line's label
            plt.text(-1, 4, f'2x + y = 0', fontsize=10, color=colors[i])
            plt.plot(x, y, color=colors[i], linewidth=1.5, 
            label=f"(a={a}, d={d})")   # <-- add label
        else:
            # Corrected coordinates for the purple line's label
            plt.text(-4, 4, f'x + y =  -{c}', fontsize=10, color=colors[i])
            plt.plot(x, y, color=colors[i], linewidth=1.5, 
            label=f"(a={a}, d={d})")   # <-- add label
    else:
        # This block handles the vertical blue line where b=0
        x_vert = -c / a
        plt.plot([x_vert]*len(x), x, color=colors[i], linewidth=1.5)
        # Place label next to the vertical line
        plt.text(x_vert + 0.2, 4.5, f'x = 1', fontsize=10, color=colors[i])
        plt.plot([x_vert]*len(x), x, color=colors[i], linewidth=1.5, 
         label=f"(a={a}, d={d})")

# Plot fixed point and label it
plt.plot(fixed_point[0], fixed_point[1], 'ro', markersize=6)
plt.text(fixed_point[0]+0.5, fixed_point[1]-0.3, '(1, -2)', fontsize=10, color='red')

# Axes settings
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Lines passing through fixed point (1, -2) for different values of a and common difference d", fontsize=12)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc="upper right")
plt.grid(True)
plt.legend()
plt.show()