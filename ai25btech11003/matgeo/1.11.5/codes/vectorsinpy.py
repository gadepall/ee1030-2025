import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_vectors_file(filename):
    """Read vectors from the .dat file created by C program"""
    vectors = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            parts = line.split()
            if len(parts) == 4:
                name = parts[0]
                x, y, z = map(float, parts[1:4])
                vectors[name] = np.array([x, y, z])
    return vectors

def solve_vector_problem():
    """Solve the vector problem mathematically"""
    print("=== Mathematical Solution ===")
    a = np.array([1, 1, 1])
    b = np.array([2, 4, -5])

    # From the analytical solution: lambda = 1
    lambda_val = 1.0
    c = np.array([lambda_val, 2, 3])
    b_plus_c = b + c

    magnitude_b_plus_c = np.linalg.norm(b_plus_c)
    unit_b_plus_c = b_plus_c / magnitude_b_plus_c

    dot_product = np.dot(a, unit_b_plus_c)

    print(f"Found λ = {lambda_val}")
    print(f"Vector a = {a}")
    print(f"Vector b = {b}")
    print(f"Vector c = {c}")
    print(f"Vector b + c = {b_plus_c}")
    print(f"||b + c|| = {magnitude_b_plus_c}")
    print(f"Unit vector (b+c)/|b+c| = {unit_b_plus_c}")
    print(f"Verification: a · u = {dot_product:.6f} (should be 1.0)")

    return {'a': a, 'b': b, 'c': c, 'unit_b_plus_c': unit_b_plus_c}

def plot_vectors(vectors_dict):
    """Create 3D visualization of all vectors (no legend)"""
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    colors = {'a': 'red', 'b': 'blue', 'c': 'green', 'unit_b_plus_c': 'purple'}
    origin = np.array([0, 0, 0])

    for name, vector in vectors_dict.items():
        ax.quiver(origin[0], origin[1], origin[2],
                  vector[0], vector[1], vector[2],
                  color=colors.get(name, 'black'),
                  arrow_length_ratio=0.1,
                  linewidth=2)

        # Endpoint labels, using (b+c)/|b+c| notation
        if name == 'unit_b_plus_c':
            label_text = f'  (b+c)/|b+c|({vector[0]:.2f},{vector[1]:.2f},{vector[2]:.2f})'
        else:
            label_text = f'  {name}({vector[0]:.2f},{vector[1]:.2f},{vector[2]:.2f})'
        ax.text(vector[0], vector[1], vector[2], label_text, fontsize=8)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Updated title
    ax.set_title('Vectors a, b, c and unit vector along b+c')

    # No legend call

    max_range = 6
    ax.set_xlim([-1, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])
    ax.grid(True)

    plt.tight_layout()
    plt.savefig('vectors_3d.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    calculated_vectors = solve_vector_problem()
    print("\n=== Attempting to read vectors.dat file ===")
    try:
        file_vectors = read_vectors_file('vectors.dat')
        print(f"Successfully read {len(file_vectors)} vectors from file:")
        for name, vector in file_vectors.items():
            if name == 'unit_b_plus_c':
                print(f"  (b+c)/|b+c|: {vector}")
            else:
                print(f"  {name}: {vector}")
        vectors_to_plot = file_vectors if file_vectors else calculated_vectors
    except FileNotFoundError:
        print("vectors.dat file not found. Using calculated vectors.")
        vectors_to_plot = calculated_vectors

    print("\n=== Creating 3D visualization ===")
    plot_vectors(vectors_to_plot)
    print("\nVisualization complete! Check the generated vectors_3d.png file.")

if __name__ == "__main__":
    main()

