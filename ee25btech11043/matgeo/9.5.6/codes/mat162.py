import numpy as np
import matplotlib.pyplot as plt

def solve_quadratic_and_plot(a, b, c):
    """
    Calculates the sum and product of roots for a quadratic equation (ax^2 + bx + c = 0),
    and generates a plot of the parabola marking its real roots.

    Args:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.
    """

    # --- Part 1: Calculate sum and product of roots ---
    # Sum of roots = -b/a
    sum_of_roots = -b / a
    # Product of roots = c/a
    product_of_roots = c / a

    print(f"For the quadratic equation {a}x^2 + {b}x + {c} = 0:")
    print(f"The sum of the roots is: {sum_of_roots:.2f}")
    print(f"The product of the roots is: {product_of_roots:.2f}")

    # --- Part 2: Plotting the parabola and its roots ---

    # Calculate the discriminant
    delta = b**2 - 4 * a * c

    # Find the roots (if real)
    roots = []
    if delta >= 0:
        root1 = (-b + np.sqrt(delta)) / (2 * a)
        root2 = (-b - np.sqrt(delta)) / (2 * a)
        roots.append(root1)
        if root1 != root2: # Add distinct root2 if it exists
            roots.append(root2)
        roots.sort() # Sort for consistent labeling
    else:
        print("\nNo real roots for this equation (discriminant is negative).")


    # Determine plotting range based on roots or a default
    if roots:
        min_root = min(roots)
        max_root = max(roots)
        # Expand the range a bit around the roots
        padding = abs(max_root - min_root) * 0.5 + 1
        if padding == 1: # Case where there's only one root or roots are identical
             padding = 2 # Ensure some sensible padding
        plot_min_x = min_root - padding
        plot_max_x = max_root + padding
    else: # If no real roots, use a reasonable default range
        plot_min_x = -5
        plot_max_x = 5

    x_vals = np.linspace(plot_min_x, plot_max_x, 400)
    y_vals = a * x_vals**2 + b * x_vals + c

    plt.figure(figsize=(10, 6))

    # Plot the parabola
    plt.plot(x_vals, y_vals, label=f'${a}x^2 {b:+}x {c:+} = 0$', color='blue')

    # Mark the roots
    for i, root in enumerate(roots):
        plt.scatter(root, 0, color='red', s=100, zorder=5, label=f'Root {i+1}: {root:.2f}')
        plt.annotate(f'({root:.2f}, 0)', (root, 0), textcoords="offset points", xytext=(5,5), ha='left', color='red')

    # Add x and y axes for reference
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadratic Parabola and its Real Roots')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend()

    # Dynamic y-axis limits for better visualization
    # Avoid errors if all y_vals are the same (e.g., a=0, b=0)
    if len(y_vals) > 1 and np.std(y_vals) > 1e-6:
        y_min_plot = np.min(y_vals)
        y_max_plot = np.max(y_vals)
        y_padding = abs(y_max_plot - y_min_plot) * 0.1
        if y_padding == 0: y_padding = 1
        plt.ylim(y_min_plot - y_padding, y_max_plot + y_padding)
    else: # Fallback for cases with very flat or constant functions
        plt.ylim(min(y_vals)-2, max(y_vals)+2)

    plt.xlim(plot_min_x, plot_max_x) # Ensure x-limits are set
    plt.show()

# --- Main execution ---
# Given quadratic equation: 2x^2 - 9x + 4 = 0
a_given = 2.0
b_given = -9.0
c_given = 4.0

solve_quadratic_and_plot(a_given, b_given, c_given)

# Example with no real roots:
# solve_quadratic_and_plot(1, 1, 1)

# Example with one real root (perfect square):
# solve_quadratic_and_plot(1, -4, 4)

# Example of a linear equation (a=0):
# solve_quadratic_and_plot(0, 2, 4)