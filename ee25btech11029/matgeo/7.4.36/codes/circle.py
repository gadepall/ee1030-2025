import sympy

def solve_circle_problem():
    x, y, a, b, p, q = sympy.symbols('x y a b p q')
    x1, x2, y1, y2 = sympy.symbols('x1 x2 y1 y2')

    print("--- Problem Setup ---")
    print("Equation for x-coordinates: x**2 + 2*a*x - b**2 = 0")
    print("Equation for y-coordinates: y**2 + 2*p*y - q**2 = 0\n")

    sum_x = -2 * a
    prod_x = -b**2

    sum_y = -2 * p
    prod_y = -q**2

    print("--- Applying Vieta's Formulas ---")
    print(f"Sum of x-roots (x1 + x2): {sum_x}")
    print(f"Sum of y-roots (y1 + y2): {sum_y}\n")

    center_h = sympy.simplify(sum_x / 2)
    center_k = sympy.simplify(sum_y / 2)
    print(f"--- Circle Center (h, k) ---")
    print(f"h = (x1 + x2) / 2 = {center_h}")
    print(f"k = (y1 + y2) / 2 = {center_k}\n")
    
    x_diff_sq = sum_x**2 - 4 * prod_x
    y_diff_sq = sum_y**2 - 4 * prod_y
    
    diameter_sq = x_diff_sq + y_diff_sq
    radius_sq = sympy.simplify(diameter_sq / 4)
    radius = sympy.sqrt(radius_sq)

    print("--- Circle Radius (r) ---")
    print(f"Squared diameter d^2 = (x1-x2)^2 + (y1-y2)^2 = {diameter_sq}")
    print(f"Squared radius r^2 = d^2 / 4 = {radius_sq}")
    print(f"Radius r = {radius}\n")

    circle_eq_standard = (x - center_h)**2 + (y - center_k)**2 - radius_sq
    
    circle_eq_general = sympy.expand(circle_eq_standard)

    print("--- Final Equation of the Circle ---")
    print(f"General Form: {circle_eq_general} = 0")


if __name__ == "__main__":
    solve_circle_problem()

