import numpy as np
import matplotlib.pyplot as plt

def generate_locus_image():
    # Define the length of the line segment
    c = 5  # Let's choose a value for c, e.g., 5

    # Create a range of angles for the line segment AB
    # These angles will determine the positions of A and B
    theta = np.linspace(0.01, np.pi/2 - 0.01, 100) # Avoid 0 and pi/2 to prevent division by zero for some calculations

    # Initialize lists to store the coordinates of the foot of the perpendicular
    locus_x = []
    locus_y = []

    for t in theta:
        # Coordinates of A and B
        # A lies on OY (x=0), B lies on OX (y=0)
        # Length AB = c
        A_y = c * np.sin(t)
        B_x = c * np.cos(t)

        A = np.array([0, A_y])
        B = np.array([B_x, 0])
        O = np.array([0, 0])

        # Complete the rectangle OAPB
        # P will have coordinates (B_x, A_y)
        P = np.array([B_x, A_y])

        # Equation of the line AB:
        # (x / B_x) + (y / A_y) = 1
        # A_y * x + B_x * y - A_y * B_x = 0

        # Vector normal to AB is (A_y, B_x)
        # Line passing through P(B_x, A_y) and perpendicular to AB
        # This line passes through the origin O(0,0) and the foot of the perpendicular, F.
        # However, the question asks for the foot of the perpendicular from P to AB.

        # Let F(x_f, y_f) be the foot of the perpendicular from P to AB.
        # The vector PF is perpendicular to AB.
        # The slope of AB is (0 - A_y) / (B_x - 0) = -A_y / B_x
        # The slope of PF is B_x / A_y (if A_y != 0)

        # Equation of line AB: y - 0 = (-A_y/B_x) * (x - B_x) => y = (-A_y/B_x)*x + A_y
        # A_y * x + B_x * y - A_y * B_x = 0

        # Equation of line PF: y - A_y = (B_x/A_y) * (x - B_x)
        # A_y * (y - A_y) = B_x * (x - B_x)
        # A_y * y - A_y^2 = B_x * x - B_x^2
        # B_x * x - A_y * y - B_x^2 + A_y^2 = 0

        # Solving the system of two linear equations for x_f and y_f:
        # Eq 1: A_y * x + B_x * y = A_y * B_x
        # Eq 2: B_x * x - A_y * y = B_x^2 - A_y^2

        # Using Cramer's rule or substitution:
        det = -A_y**2 - B_x**2
        det_x = -A_y**3 * B_x - B_x**3 * A_y
        det_y = A_y**2 * B_x**2 - B_x * (B_x**2 - A_y**2) * A_y

        # Simplified equations:
        # x_f = (A_y^2 * B_x^2 + B_x^2 * (B_x^2 - A_y^2)) / (A_y^2 + B_x^2)
        # y_f = (A_y * B_x * (B_x^2 - A_y^2) - A_y * B_x * A_y^2) / (-(A_y^2 + B_x^2))

        # A simpler way to find the foot of the perpendicular:
        # Project vector OP onto the line AB.
        # This is incorrect, as P is a vertex of the rectangle.

        # Let F be the foot of the perpendicular.
        # Vector AF is proportional to AB.
        # Vector PF is perpendicular to AB.

        # A more direct approach using parameterization of line AB:
        # r(lambda) = A + lambda * (B - A)
        # Vector PF = F - P = (A + lambda * (B - A)) - P
        # PF . (B - A) = 0
        # ((A - P) + lambda * (B - A)) . (B - A) = 0
        # (A - P) . (B - A) + lambda * (B - A) . (B - A) = 0
        # lambda = -((A - P) . (B - A)) / (LA.norm(B - A)**2)

        # Vector B-A
        BA = B - A # (B_x, -A_y)

        # Vector A-P
        AP = A - P # (-B_x, 0)

        # Calculate lambda
        lambda_val = -np.dot(AP, BA) / np.dot(BA, BA)
        
        # Coordinates of F
        F = A + lambda_val * BA
        locus_x.append(F[0])
        locus_y.append(F[1])

    # Plotting
    plt.figure(figsize=(8, 8))
    plt.plot(locus_x, locus_y, color='blue', label='Locus of the foot of perpendicular')

    # For illustrative purposes, let's plot one instance of the rectangle and the foot of the perpendicular
    # Choose a specific angle for demonstration
    demo_t = np.pi/4
    A_y_demo = c * np.sin(demo_t)
    B_x_demo = c * np.cos(demo_t)
    A_demo = np.array([0, A_y_demo])
    B_demo = np.array([B_x_demo, 0])
    P_demo = np.array([B_x_demo, A_y_demo])

    BA_demo = B_demo - A_demo
    AP_demo = A_demo - P_demo
    lambda_val_demo = -np.dot(AP_demo, BA_demo) / np.dot(BA_demo, BA_demo)
    F_demo = A_demo + lambda_val_demo * BA_demo

    # Plot the axes
    plt.axhline(0, color='gray', linewidth=0.8)
    plt.axvline(0, color='gray', linewidth=0.8)

    # Plot the demo rectangle and points
    plt.plot([0, B_x_demo], [0, 0], 'k--', linewidth=0.7) # OX
    plt.plot([0, 0], [0, A_y_demo], 'k--', linewidth=0.7) # OY
    plt.plot([0, B_x_demo], [A_y_demo, A_y_demo], 'k--', linewidth=0.7) # PA parallel to OX
    plt.plot([B_x_demo, B_x_demo], [0, A_y_demo], 'k--', linewidth=0.7) # PB parallel to OY
    plt.plot([A_demo[0], B_demo[0]], [A_demo[1], B_demo[1]], 'k-', label='Line segment AB (demo)')
    plt.plot([P_demo[0], F_demo[0]], [P_demo[1], F_demo[1]], 'r--', label='Perpendicular PF (demo)')


    plt.scatter([0, B_x_demo, 0, B_x_demo, F_demo[0]], [0, 0, A_y_demo, A_y_demo, F_demo[1]],
                s=50, color='black', zorder=5)
    plt.text(0.1, 0.1, 'O', fontsize=12)
    plt.text(B_x_demo + 0.1, 0.1, 'B', fontsize=12)
    plt.text(0.1, A_y_demo + 0.1, 'A', fontsize=12)
    plt.text(B_x_demo + 0.1, A_y_demo + 0.1, 'P', fontsize=12)
    plt.text(F_demo[0] + 0.1, F_demo[1] + 0.1, 'F', fontsize=12)


    # Plot the analytical solution for comparison (x^(2/3) + y^(2/3) = c^(2/3))
    # This equation is a hypocycloid (astroid)
    t_astroid = np.linspace(0, 2 * np.pi, 200)
    astroid_x = (c**(2/3) * np.cos(t_astroid)**2)**(3/2) # x = c^(2/3) * cos^3(t)
    astroid_y = (c**(2/3) * np.sin(t_astroid)**2)**(3/2) # y = c^(2/3) * sin^3(t)

    # The astroid is typically x = a cos^3(theta), y = a sin^3(theta)
    # So if x^(2/3) + y^(2/3) = c^(2/3), then
    # (c^(2/3) cos^3(theta))^(2/3) + (c^(2/3) sin^3(theta))^(2/3) = c^(2/3)
    # c^(4/9) cos^2(theta) + c^(4/9) sin^2(theta) = c^(2/3)
    # This doesn't quite match.
    # Let's re-evaluate the equation's common form: x^(2/3) + y^(2/3) = a^(2/3)
    # This is a general astroid where x = a cos^3(phi) and y = a sin^3(phi).
    # So, here 'a' is 'c'.
    # x_astroid = c * np.cos(t_astroid)**3
    # y_astroid = c * np.sin(t_astroid)**3

    # However, the problem states x^(2/3) + y^(2/3) = c^(2/3) directly.
    # So if x is positive, x = (c^(2/3) - y^(2/3))^(3/2)
    # Or parametrically:
    x_analytic = (c * np.cos(theta)**3)
    y_analytic = (c * np.sin(theta)**3)

    plt.plot(x_analytic, y_analytic, 'g--', label=f'Analytical Locus: $x^{{2/3}} + y^{{2/3}} = c^{{2/3}}$ (c={c})')


    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Locus of the foot of perpendicular from P to AB')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.xlim(-0.1, c + 1)
    plt.ylim(-0.1, c + 1)
    plt.savefig("fig2.png")
    plt.show()

# Call the function to generate the plot
generate_locus_image()
