import matplotlib.pyplot as plt
import math

def plot_triangle(c):
    a = 5       # fixed side 1
    b = 1.5     # fixed side 2

    # Triangle inequality check
    if not (a + b > c and a + c > b and b + c > a):
        print(False)
        return False

    # Place side 'a' on x-axis (0,0) to (a,0)
    A = (0, 0)
    B = (a, 0)

    # Use law of cosines to find angle at A
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    if cos_C < -1 or cos_C > 1:  # numerical stability check
        print(False)
        return False

    # Place C using coordinates
    # Using law of cosines again for coordinates
    x = (b**2 + a**2 - c**2) / (2 * a)
    y = math.sqrt(max(b**2 - x**2, 0))
    C = (x, y)

    # Plot triangle
    plt.figure(figsize=(5,5))
    x_coords = [A[0], B[0], C[0], A[0]]
    y_coords = [A[1], B[1], C[1], A[1]]
    plt.plot(x_coords, y_coords, 'b-')
    plt.fill(x_coords, y_coords, 'skyblue', alpha=0.4)
    
    # Label vertices
    plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
    plt.text(B[0], B[1], 'B', fontsize=12, ha='left')
    plt.text(C[0], C[1], 'C', fontsize=12, va='bottom')

    plt.axis("equal")
    plt.title(f"Triangle with sides: {a}, {b}, {c}")
    plt.savefig("triangle.png")
    plt.close()
    print("Triangle plotted and saved as triangle.png")
    return True


if __name__ == "__main__":
    c = float(input("Enter third side length: "))
    plot_triangle(c)
