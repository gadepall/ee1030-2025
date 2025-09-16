import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Define C int type
c_int = ctypes.c_int

def main():
    # Coordinates of the points (numpy arrays)
    A = np.array([c_int(7).value, c_int(10).value])
    B = np.array([c_int(-2).value, c_int(5).value])
    C = np.array([c_int(3).value, c_int(4).value])

    # Squared lengths of sides
    AB2 = c_int(np.sum((A - B) ** 2))
    AC2 = c_int(np.sum((A - C) ** 2))
    BC2 = c_int(np.sum((B - C) ** 2))

    # Dot products (for right angle check)
    dot_AB_AC = c_int(np.dot(A - B, A - C))
    dot_AB_BC = c_int(np.dot(A - B, B - C))
    dot_AC_BC = c_int(np.dot(A - C, B - C))

    print("Squared side lengths:")
    print(f"AB^2 = {AB2.value}")
    print(f"AC^2 = {AC2.value}")
    print(f"BC^2 = {BC2.value}")

    print("\nDot products:")
    print(f"(A-B)·(A-C) = {dot_AB_AC.value}")
    print(f"(A-B)·(B-C) = {dot_AB_BC.value}")
    print(f"(A-C)·(B-C) = {dot_AC_BC.value}")

    # Check isosceles right triangle
    if ((AB2.value == AC2.value and dot_AB_AC.value == 0) or
        (AB2.value == BC2.value and dot_AB_BC.value == 0) or
        (AC2.value == BC2.value and dot_AC_BC.value == 0)):
        result = "ISOSCELES RIGHT triangle"
    else:
        result = "NOT an isosceles right triangle"
    print(f"\nThe points form {result}.")

    # ---- Plotting ----
    fig, ax = plt.subplots()
    # Draw triangle edges
    triangle = np.array([A, B, C, A])  # closed loop
    ax.plot(triangle[:, 0], triangle[:, 1], 'b-o', linewidth=2)

    # Annotate points
    ax.text(A[0]+0.2, A[1]+0.2, "A(7,10)", color="red")
    ax.text(B[0]+0.2, B[1]+0.2, "B(-2,5)", color="red")
    ax.text(C[0]+0.2, C[1]+0.2, "C(3,4)", color="red")

    # Title
    ax.set_title(f"Triangle ABC: {result}")
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)

    plt.show()

if __name__ == "__main__":
    main()s
