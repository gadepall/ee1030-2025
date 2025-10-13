import math
import numpy as np
import matplotlib.pyplot as plt

def solve_quadratic_native(a, b, c):
    """
    Solves a quadratic equation ax^2 + bx + c = 0.
    Returns a tuple of real roots, or None if no real roots exist.
    """
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2*a)
        root2 = (-b - sqrt_discriminant) / (2*a)
        return (root1, root2)

def plot_solution(a, b, c, roots):
    """
    Plots the quadratic function and its intersection points with the x-axis.
    """
    # 1. Generate a range of 's' values for our x-axis
    s_values = np.linspace(min(roots) - 20, max(roots) + 20, 400)
    # 2. Calculate the corresponding y-values for the parabola
    y_values = a * s_values**2 + b * s_values + c

    plt.figure(figsize=(10, 6))
    
    # 3. This line plots the parabola itself
    plt.plot(s_values, y_values, label=f'Parabola: $y = s^2 + 5s - 1800$')
    
    # 4. This line draws the x-axis (y=0) for reference
    plt.axhline(0, color='black', linestyle='--')
    
    # 5. This line plots the intersection points (the roots) on the x-axis
    plt.plot(roots, [0]*len(roots), 'ro', markersize=8, label=f'Intersection Points: ({roots[0]:.0f}, 0) & ({roots[1]:.0f}, 0)')
    
    # --- Formatting ---
    positive_root = next(r for r in roots if r > 0)
    plt.title(f"Solution to the Train Problem (s = {positive_root:.0f} km/hr)", fontsize=14)
    plt.xlabel("Speed (s)")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/9.4.40/figs/figure1.png")
    plt.show()

# --- Main execution ---
if __name__ == "__main__":
    # Coefficients from the train problem: s^2 + 5s - 1800 = 0
    a, b, c = 1.0, 5.0, -1800.0
    
    roots = solve_quadratic_native(a, b, c)

    if roots:
        # Sort roots for consistent plotting
        sorted_roots = sorted(roots)
        plot_solution(a, b, c, sorted_roots)
    else:
        print("No real roots found.")
