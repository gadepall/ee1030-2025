import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ctypes
import os
import subprocess

# Function to read vectors from vectors.dat file
def read_vectors_from_file(filename):
    vectors = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split()
                    label = parts[0]
                    coords = [float(x) for x in parts[1:]]
                    vectors[label] = np.array(coords)
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please run the C program first to generate it.")
        return None
    return vectors

# Function to compile and load the shared library
def compile_and_load_library():
    print("Compiling C code into shared library...")

    # Compile the C code into a shared library
    compile_result = subprocess.run(
        ["gcc", "-shared", "-fPIC", "-o", "main.so", "main.c", "-lm"],
        capture_output=True, text=True
    )

    if compile_result.returncode != 0:
        print("Compilation failed:")
        print(compile_result.stderr)
        return None

    print("Compilation successful: main.so created")

    # Load the shared library
    try:
        lib = ctypes.CDLL('./main.so')
    except OSError as e:
        print(f"Error loading library: {e}")
        return None

    # Define function signatures
    lib.find_plane_normal.argtypes = [
        ctypes.POINTER(ctypes.c_double),  # A
        ctypes.POINTER(ctypes.c_double),  # B  
        ctypes.POINTER(ctypes.c_double),  # C
        ctypes.POINTER(ctypes.c_double)   # n (output)
    ]
    lib.find_plane_normal.restype = None

    lib.point_to_plane_distance.argtypes = [
        ctypes.POINTER(ctypes.c_double),  # P
        ctypes.POINTER(ctypes.c_double)   # n
    ]
    lib.point_to_plane_distance.restype = ctypes.c_double

    return lib

def solve_distance_problem():
    print("=== Distance Between Point and Plane - Python Solution ===\n")

    # Check if vectors.dat exists, if not, suggest running C program
    if not os.path.exists('vectors.dat'):
        print("vectors.dat not found!")
        print("Please first compile and run the C program:")
        print("1. gcc -o main main.c -lm")
        print("2. ./main")
        print("This will generate the vectors.dat file.\n")
        return None, None, None, None, None, None

    # Read vectors from file
    vectors = read_vectors_from_file('vectors.dat')
    if vectors is None:
        return None, None, None, None, None, None

    A = vectors['A']
    B = vectors['B'] 
    C = vectors['C']
    P = vectors['P']
    n_from_file = vectors['n']  # Normal vector calculated by C program

    print("Points loaded from vectors.dat:")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")
    print(f"P = {P}")
    print(f"Normal vector n = {n_from_file}")

    # Compile and load the shared library
    lib = compile_and_load_library()
    if lib is None:
        return None, None, None, None, None, None

    # Convert numpy arrays to ctypes arrays
    A_c = (ctypes.c_double * 3)(*A)
    B_c = (ctypes.c_double * 3)(*B)
    C_c = (ctypes.c_double * 3)(*C)
    P_c = (ctypes.c_double * 3)(*P)
    n_c = (ctypes.c_double * 3)()

    # Calculate normal vector using C library (for verification)
    lib.find_plane_normal(A_c, B_c, C_c, n_c)
    n_calculated = np.array([n_c[0], n_c[1], n_c[2]])

    # Calculate distance using C library
    n_c_for_distance = (ctypes.c_double * 3)(*n_from_file)
    distance = lib.point_to_plane_distance(P_c, n_c_for_distance)

    print(f"\nResults from C library:")
    print(f"Calculated normal vector: {n_calculated}")
    print(f"Distance from P to plane: {distance:.10f} units")

    # Verification
    expected_distance = 3 * np.sqrt(34) / 17
    print(f"\nVerification:")
    print(f"Expected distance (3√34/17): {expected_distance:.10f} units")
    print(f"Match: {'Yes' if abs(distance - expected_distance) < 1e-10 else 'No'}")

    return A, B, C, P, n_from_file, distance

def create_plane_visualization(A, B, C, P, distance):
    print("\nCreating visualization...")

    # Create 3D plot
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')

    # Plot points A, B, C on the plane
    ax.scatter(*A, color='red', s=120, label='A(3,-1,2)', alpha=0.8)
    ax.scatter(*B, color='green', s=120, label='B(5,2,4)', alpha=0.8)  
    ax.scatter(*C, color='blue', s=120, label='C(-1,-1,6)', alpha=0.8)

    # Plot point P with emphasis to show it's away from the plane
    ax.scatter(*P, color='purple', s=200, label='P(6,5,9)', marker='D', alpha=0.9, edgecolors='black', linewidth=2)

    # Annotate points with better positioning
    ax.text(A[0]+0.2, A[1]+0.2, A[2]+0.2, 'A', fontsize=14, fontweight='bold', color='darkred')
    ax.text(B[0]+0.2, B[1]+0.2, B[2]+0.2, 'B', fontsize=14, fontweight='bold', color='darkgreen')
    ax.text(C[0]+0.2, C[1]+0.2, C[2]+0.2, 'C', fontsize=14, fontweight='bold', color='darkblue')
    ax.text(P[0]+0.2, P[1]+0.2, P[2]+0.2, 'P', fontsize=14, fontweight='bold', color='purple')

    # Create plane surface using the three points A, B, C
    v1 = B - A  # Vector from A to B
    v2 = C - A  # Vector from A to C

    # Create a larger parametric grid for the plane to show it extends beyond the points
    u = np.linspace(-2.0, 2.0, 25)
    v = np.linspace(-2.0, 2.0, 25)
    U, V = np.meshgrid(u, v)

    # Parametric equation of plane: Point = A + u*v1 + v*v2
    X = A[0] + U * v1[0] + V * v2[0]
    Y = A[1] + U * v1[1] + V * v2[1]  
    Z = A[2] + U * v1[2] + V * v2[2]

    # Plot the plane surface with transparency to clearly show P is above it
    ax.plot_surface(X, Y, Z, alpha=0.4, color='lightblue', edgecolor='none')

    # Add a wireframe to make the plane more visible
    ax.plot_wireframe(X, Y, Z, alpha=0.2, color='gray', linewidth=0.5)

    # Set labels and title
    ax.set_xlabel('X', fontsize=14, fontweight='bold')
    ax.set_ylabel('Y', fontsize=14, fontweight='bold')
    ax.set_zlabel('Z', fontsize=14, fontweight='bold')
    ax.set_title('Distance between Point and Plane', fontsize=18, fontweight='bold', pad=20)

    # NO YELLOW BOX - Distance information removed as requested

    # Set legend with better positioning
    ax.legend(loc='upper left', fontsize=12, framealpha=0.9)

    # Adjust the view to better show P is away from the plane
    ax.view_init(elev=25, azim=45)

    # Set axis limits to better show the separation between P and the plane
    all_points = np.vstack([A, B, C, P])
    x_range = all_points[:, 0].max() - all_points[:, 0].min()
    y_range = all_points[:, 1].max() - all_points[:, 1].min()
    z_range = all_points[:, 2].max() - all_points[:, 2].min()

    margin = max(x_range, y_range, z_range) * 0.3

    ax.set_xlim([all_points[:, 0].min() - margin, all_points[:, 0].max() + margin])
    ax.set_ylim([all_points[:, 1].min() - margin, all_points[:, 1].max() + margin])
    ax.set_zlim([all_points[:, 2].min() - margin, all_points[:, 2].max() + margin])

    # Improve grid and background
    ax.grid(True, alpha=0.3)

    # Save the figure as fig1.png with higher quality
    plt.savefig('fig1.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.tight_layout()
    plt.show()

    print("Visualization saved as 'fig1.png'")
    print("- Point P is now clearly shown away from the plane")
    print("- Yellow distance box removed")

def main():
    # Solve the distance problem
    result = solve_distance_problem()

    if result[0] is not None:  # Check if solution was successful
        A, B, C, P, n, distance = result

        # Create visualization
        create_plane_visualization(A, B, C, P, distance)

        print("\n=== Summary ===")
        print("Files used/created:")
        print("- vectors.dat (read from C program output)")
        print("- main.so (compiled shared library)")
        print("- fig1.png (generated visualization)")
        print("\nSolution completed successfully!")
    else:
        print("\nSolution failed. Please check the instructions above.")

if __name__ == "__main__":
    main()
