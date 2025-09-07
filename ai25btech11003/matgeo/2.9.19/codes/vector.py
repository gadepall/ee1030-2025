#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ctypes
import os
import sys

def load_vectors_from_file(filename):
    """Load vectors from the data file created by C program"""
    vectors = {}
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            parts = line.split()
            if len(parts) >= 4:
                name = parts[0]
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                vectors[name] = np.array([x, y, z])
        return vectors
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please run the C program first.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def load_shared_library():
    """Load the shared library created by C program"""
    try:
        lib_path = "./vectors.so"
        if not os.path.exists(lib_path):
            print("Error: vectors.so not found. Please compile the C program first.")
            print("Run: gcc -fPIC -shared -o vectors.so vector_solution.c -lm")
            return None
        lib = ctypes.CDLL(lib_path)
        lib.compute_vector_magnitude.argtypes = [
            ctypes.POINTER(ctypes.c_double),
            ctypes.POINTER(ctypes.c_double),
            ctypes.POINTER(ctypes.c_double)
        ]
        lib.compute_vector_magnitude.restype = ctypes.c_double
        return lib
    except Exception as e:
        print(f"Error loading shared library: {e}")
        return None

def create_vector_visualization(vectors):
    """Create 3D visualization of the vectors"""
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')

    # Colors for different vectors
    colors = {'a': 'red', 'b': 'blue', 'c': 'green', 'result': 'purple'}
    labels = {'a': 'Vector a', 'b': 'Vector b', 'c': 'Vector c', 'result': '3a - 2b + 2c'}
    origin = np.array([0, 0, 0])

    # Plot vectors
    for name, vector in vectors.items():
        if name in colors:
            ax.quiver(origin[0], origin[1], origin[2],
                      vector[0], vector[1], vector[2],
                      color=colors[name], arrow_length_ratio=0.1,
                      linewidth=3, label=labels[name])
            ax.text(vector[0], vector[1], vector[2],
                    f'{name}({vector[0]:.2f}, {vector[1]:.2f}, {vector[2]:.2f})',
                    fontsize=9)

    # Set equal aspect ratio and labels
    max_range = max([np.linalg.norm(v) for v in vectors.values()]) * 1.2
    ax.set_xlim([-max_range/2, max_range/2])
    ax.set_ylim([-max_range/2, max_range/2])
    ax.set_zlim([0, max_range])
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    # Remove legend
    # ax.legend()

    ax.grid(True)

    # Add title as requested
    plt.title('Vectors a, b and c', fontsize=16, fontweight='bold')

    # Save with requested filename, without bottom-left info box
    plt.tight_layout()
    plt.savefig('fig1.png', dpi=300, bbox_inches='tight')
    plt.show()

def verify_calculations_with_library(vectors, lib):
    """Verify calculations using the C shared library"""
    if lib is None:
        print("Shared library not available, skipping verification.")
        return
    try:
        a_array = (ctypes.c_double * 3)(*vectors['a'])
        b_array = (ctypes.c_double * 3)(*vectors['b'])
        c_array = (ctypes.c_double * 3)(*vectors['c'])
        magnitude_from_c = lib.compute_vector_magnitude(a_array, b_array, c_array)
        print(f"Magnitude from C library: {magnitude_from_c:.6f}")
        print(f"Magnitude from Python: {np.linalg.norm(vectors['result']):.6f}")
        print(f"Theoretical value (√61): {np.sqrt(61):.6f}")
    except Exception as e:
        print(f"Error calling C function: {e}")

def main():
    print("Loading vectors from vectors.dat...")
    vectors = load_vectors_from_file("vectors.dat")
    if vectors is None:
        print("Please ensure you have run the C program first to generate vectors.dat")
        return

    lib = load_shared_library()
    verify_calculations_with_library(vectors, lib)
    create_vector_visualization(vectors)

if __name__ == "__main__":
    main()

