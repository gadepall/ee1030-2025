import matplotlib as mp
mp.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt

def line_equation_normal(point1, point2):
    """
    Returns line equation in normal form: n^T x = c
    where n is the normal vector and x = [x y]^T.
    """
    x1, y1 = point1
    x2, y2 = point2

    # Direction vector
    dx, dy = x2 - x1, y2 - y1
    
    # Normal vector
    n = np.array([dy, -dx])
    
    # Constant term
    c = n @ np.array([x1, y1])
    
    return n, c

def diagonals_of_square(vertices):
    """
    Given 4 vertices of a square (in order), compute equations of diagonals.
    """
    A, B, C, D = vertices
    
    # Diagonals are AC and BD
    line1 = line_equation_normal(A, C)
    line2 = line_equation_normal(B, D)
    
    return line1, line2

def format_normal_form(n, c):
    """Format equation in normal form."""
    return f"[{n[0]} {n[1]}] · [x y]^T = {c}"

def format_cartesian(n, c):
    """
    Convert n^T x = c into Cartesian form ax + by + d = 0
    where n = [a b].
    """
    a, b = n
    d = -c
    terms = []
    if a != 0:
        terms.append(f"{'' if a == 1 else '-' if a == -1 else a}x")
    if b != 0:
        sign = "+" if b > 0 and terms else ""
        terms.append(f"{sign}{'' if abs(b) == 1 else b}y" if b not in [1, -1] else f"{sign}{'y' if b == 1 else '-y'}")
    if d != 0:
        sign = "+" if d > 0 and terms else ""
        terms.append(f"{sign}{d}")
    return " ".join(terms) + " = 0"

def plot_square_and_diagonals(vertices, line1, line2):
    """Plot square and its diagonals with Cartesian equations on the plot."""
    A, B, C, D = vertices
    square_x = [A[0], B[0], C[0], D[0], A[0]]
    square_y = [A[1], B[1], C[1], D[1], A[1]]
    
    plt.plot(square_x, square_y, 'b-', label='Square')
    
    # Plot diagonals
    plt.plot([A[0], C[0]], [A[1], C[1]], 'r--', label='Diagonal AC')
    plt.plot([B[0], D[0]], [B[1], D[1]], 'g--', label='Diagonal BD')
    
    # Equations in Cartesian form for plot
    eq1 = format_cartesian(*line1)
    eq2 = format_cartesian(*line2)
    
    # Midpoints of diagonals
    mid_AC = ((A[0]+C[0])/2, (A[1]+C[1])/2)
    mid_BD = ((B[0]+D[0])/2, (B[1]+D[1])/2)
    
    # Place texts
    plt.text(mid_AC[0]+0.05, mid_AC[1]+0.05, eq1, color='red', fontsize=10, ha='left')
    plt.text(mid_BD[0]-0.15, mid_BD[1]-0.1, eq2, color='green', fontsize=10, ha='right')
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.savefig("/home/user/Matrix/Matgeo_assignments/4.3.13/figs/Figure_1")
    plt.show()

# Example input
vertices = [(0,0), (1,0), (1,1), (0,1)]

# Compute diagonal equations
line1, line2 = diagonals_of_square(vertices)

# Print normal forms
print("Diagonal AC equation (normal form):", format_normal_form(*line1))
print("Diagonal BD equation (normal form):", format_normal_form(*line2))

# Plot with Cartesian equations
plot_square_and_diagonals(vertices, line1, line2)


