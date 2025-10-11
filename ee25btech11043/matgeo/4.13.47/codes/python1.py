import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib_geometry = ctypes.CDLL("./code9.so")

# Define the argument types and return type for the C function
lib_geometry.calculateFootOfPerpendicular.argtypes = [
    ctypes.c_double,  # P_x
    ctypes.c_double,  # P_y
    ctypes.c_double,  # A_x
    ctypes.c_double,  # A_y
    ctypes.c_double,  # B_x
    ctypes.c_double,  # B_y
    ctypes.POINTER(ctypes.c_double), # foot_x
    ctypes.POINTER(ctypes.c_double)  # foot_y
]
lib_geometry.calculateFootOfPerpendicular.restype = None

def generate_locus_image():
    """
    Generates an image showing the locus of the foot of the perpendicular
    from P to AB, using a C function for calculation.
    """
    # Define the length of the line segment
    c = 5.0  # Let's choose a value for c, e.g., 5.0

    # Create a range of angles for the line segment AB
    # These angles will determine the positions of A and B
    # Avoid 0 and pi/2 to prevent division by zero for some calculations or degenerate cases
    theta_vals = np.linspace(0.01, np.pi/2 - 0.01, 100)

    # Initialize lists to store the coordinates of the foot of the perpendicular
    locus_x = []
    locus_y = []

    # Ctypes variables to hold the results from the C function
    foot_x_result = ctypes.c_double()
    foot_y_result = ctypes.c_double()

    for theta in theta_vals:
        # Coordinates of A and B
        # A lies on OY (x=0), B lies on OX (y=0)
        # Length AB = c
        A_x = 0.0
        A_y = c * np.sin(theta)
        B_x = c * np.cos(theta)
        B_y = 0.0

        # Complete the rectangle OAPB
        # P will have coordinates (B_x, A_y)
        P_x = B_x
        P_y = A_y

        # Call the C function to find the foot of the perpendicular
        lib_geometry.calculateFootOfPerpendicular(
            P_x, P_y,
            A_x, A_y,
            B_x, B_y,
            ctypes.byref(foot_x_result),
            ctypes.byref(foot_y_result)
        )

        locus_x.append(foot_x_result.value)
        locus_y.append(foot_y_result.value)

    # --- Plotting ---
    plt.figure(figsize=(8, 8))
    plt.plot(locus_x, locus_y, color='blue', linewidth=2, label='Locus from C calculation')

    # For illustrative purposes, let's plot one instance of the rectangle and the foot of the perpendicular
    # Choose a specific angle for demonstration
    demo_t = np.pi/4
    A_y_demo = c * np.sin(demo_t)
    B_x_demo = c * np.cos(demo_t)
    A_demo = np.array([0, A_y_demo])
    B_demo = np.array([B_x_demo, 0])
    P_demo = np.array([B_x_demo, A_y_demo])

    # Recalculate foot for demo using C function
    lib_geometry.calculateFootOfPerpendicular(
        P_demo[0], P_demo[1],
        A_demo[0], A_demo[1],
        B_demo[0], B_demo[1],
        ctypes.byref(foot_x_result),
        ctypes.byref(foot_y_result)
    )
    F_demo = np.array([foot_x_result.value, foot_y_result.value])

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
    plt.text(P_demo[0] + 0.1, P_demo[1] + 0.1, 'P', fontsize=12)
    plt.text(F_demo[0] + 0.1, F_demo[1] + 0.1, 'F', fontsize=12)

    # Plot the analytical solution for comparison (Astroid: x^(2/3) + y^(2/3) = c^(2/3))
    # Parametric form: x = c * cos^3(t), y = c * sin^3(t)
    t_astroid = np.linspace(0, np.pi/2, 200) # Only first quadrant
    x_analytic = c * np.cos(t_astroid)**3
    y_analytic = c * np.sin(t_astroid)**3

    plt.plot(x_analytic, y_analytic, 'g--', linewidth=1.5,
             label=f'Analytical Locus: $x^{{2/3}} + y^{{2/3}} = c^{{2/3}}$ (c={c})')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Locus of the foot of perpendicular from P to AB')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.xlim(-0.1, c + 1)
    plt.ylim(-0.1, c + 1)
    plt.savefig("fig1.png")
    plt.show()

# Call the function to generate the plot
generate_locus_image()
