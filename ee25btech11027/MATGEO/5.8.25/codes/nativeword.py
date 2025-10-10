import numpy as np
import matplotlib.pyplot as plt

# --- 1. Define the system of equations in matrix form (Aa = B) ---
# 1a - 2b = -300
# 6a - 1b = 70

# Matrix of coefficients
A = np.array([
    [1, -2],
    [6, -1]
])

# Vector of constants
B = np.array([-300, 70])


# --- 2. Solve the system using NumPy ---
try:
    solution = np.linalg.solve(A, B)
    a_sol, b_sol = solution
    print(f"Solution from Python (NumPy): a = {a_sol:.2f}, b = {b_sol:.2f}")

    # --- 3. Plot the Graph ---
    # Create a range of 'a' values for plotting
    a_vals = np.linspace(a_sol - 50, a_sol + 50, 400)

    # Rearrange equations to solve for 'b' (the y-axis)
    # b = (-300 - 1a) / -2
    # b = (70 - 6a) / -1
    b1_vals = (-300 - 1 * a_vals) / -2
    b2_vals = (70 - 6 * a_vals) / -1

    # Create the plot
    plt.figure(figsize=(10, 8))
    plt.plot(a_vals, b1_vals, label='1a - 2b = -300')
    plt.plot(a_vals, b2_vals, label='6a - 1b = 70')

    # Mark the intersection point (same style as your script)
    plt.scatter(a_sol, b_sol, color="red", s=200, marker="*", edgecolors="black",
                zorder=5, label=f'Intersection ({a_sol:.0f}, {b_sol:.0f})')

    # Annotate the point with an arrow
    plt.annotate(f"({a_sol:.0f}, {b_sol:.0f})",
                 (a_sol, b_sol),
                 textcoords="offset points",
                 xytext=(10, 10),
                 fontsize=12,
                 color="red",
                 arrowprops=dict(arrowstyle="->", color="red"))

    # Add titles, labels, and grid
    plt.title("Graphical Solution of Linear Equations", fontsize=16)
    plt.xlabel("a-axis", fontsize=12)
    plt.ylabel("b-axis", fontsize=12)
    plt.grid(True)
    plt.legend()

    # Display the plot
    plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/5.8.25/figs/figure1.png")
    plt.show()

except np.linalg.LinAlgError:
    print("The system of equations has no unique solution.")
