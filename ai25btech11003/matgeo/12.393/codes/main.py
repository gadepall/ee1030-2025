
import numpy as np
import struct
import math
import numpy as np


A = np.array([[15, 4, 3],[10, 12,6],[20,4,2]])


y = np.array([0.731, 1, 0.849]).reshape(-1,1)

print(np.linalg.norm(np.matmul(A,y)/np.linalg.norm(y)))
from math import sqrt

def read_binary_data():
    """Read solution data from main.so binary file"""
    try:
        with open('main.so', 'rb') as f:
            # Read 6 double values (2 solutions × 3 values each)
            binary_data = f.read()
            solutions = struct.unpack('6d', binary_data)

        sol1 = (solutions[0], solutions[1], solutions[2])  # a1, b1, c1
        sol2 = (solutions[3], solutions[4], solutions[5])  # a2, b2, c2

        print("Data read from main.so (binary file):")
        print(f"Solution 1: a = {sol1[0]:.6f}, b = {sol1[1]:.6f}, c = {sol1[2]:.6f}")
        print(f"Solution 2: a = {sol2[0]:.6f}, b = {sol2[1]:.6f}, c = {sol2[2]:.6f}")

        return sol1, sol2
    except FileNotFoundError:
        print("Error: main.so file not found. Run the C program first.")
        return None, None
    except Exception as e:
        print(f"Error reading main.so: {e}")
        return None, None

def read_text_data():
    """Read solution data from main.dat text file"""
    try:
        solutions = []
        with open('main.dat', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if not line.startswith('#') and line.strip():
                    values = [float(x) for x in line.strip().split()]
                    if len(values) == 3:
                        solutions.append(tuple(values))

        print("\nData read from main.dat (text file):")
        for i, sol in enumerate(solutions, 1):
            print(f"Solution {i}: a = {sol[0]:.6f}, b = {sol[1]:.6f}, c = {sol[2]:.6f}")

        return solutions
    except FileNotFoundError:
        print("Error: main.dat file not found. Run the C program first.")
        return []
    except Exception as e:
        print(f"Error reading main.dat: {e}")
        return []

def construct_matrices(solutions):
    """Construct the Q matrices from solutions"""
    sqrt_3 = sqrt(3)
    sqrt_2 = sqrt(2)

    matrices = []
    for i, (a, b, c) in enumerate(solutions):
        Q = np.array([
            [1/sqrt_3, 1/sqrt_2, a],
            [1/sqrt_3, 0, b],
            [1/sqrt_3, -1/sqrt_2, c]
        ])
        matrices.append(Q)

        print(f"\nMatrix Q{i+1}:")
        print(Q)

        # Verify orthonormality
        QTQ = np.dot(Q.T, Q)
        I = np.eye(3)
        is_orthonormal = np.allclose(QTQ, I, atol=1e-10)

        print(f"Q{i+1}^T * Q{i+1} =")
        print(QTQ)
        print(f"Is orthonormal: {is_orthonormal}")

    return matrices

def analyze_solutions(solutions):
    """Analyze which multiple choice options match our solutions"""
    sqrt_2 = sqrt(2)
    sqrt_3 = sqrt(3)
    sqrt_6 = sqrt(6)

    # Original multiple choice options
    options = {
        'A': (1/sqrt_2, 1/sqrt_2, 0),
        'B': (1/sqrt_6, -2/sqrt_6, 1/sqrt_6),
        'C': (1/sqrt_3, 1/sqrt_3, 1/sqrt_3),
        'D': (-1/sqrt_6, 2/sqrt_6, -1/sqrt_6)
    }

    print("\nAnalysis of solutions against multiple choice options:")
    print("====================================================")

    for i, sol in enumerate(solutions, 1):
        print(f"\nSolution {i}: ({sol[0]:.6f}, {sol[1]:.6f}, {sol[2]:.6f})")
        matched = False
        for option, values in options.items():
            if np.allclose(sol, values, atol=1e-10):
                print(f"  → Matches Option {option}")
                matched = True
        if not matched:
            print("  → No exact match with given options")



def main():
    """Main function to analyze orthonormal matrix data from C program"""
    print("Orthonormal Matrix Data Analyzer")
    print("===============================")

    # Read data from both files
    binary_sol1, binary_sol2 = read_binary_data()
    text_solutions = read_text_data()

    if binary_sol1 and binary_sol2:
        binary_solutions = [binary_sol1, binary_sol2]

        # Verify data consistency between files
        if text_solutions:
            print("\nVerifying data consistency between files:")
            for i, (bin_sol, txt_sol) in enumerate(zip(binary_solutions, text_solutions)):
                consistent = np.allclose(bin_sol, txt_sol, atol=1e-10)
                print(f"Solution {i+1} consistency: {'✓ Consistent' if consistent else '✗ Inconsistent'}")

        # Construct and analyze matrices
        matrices = construct_matrices(binary_solutions)
        analyze_solutions(binary_solutions)
       

        print("\n" + "="*50)
        print("CONCLUSION:")
        print("The correct answers from the original multiple choice are:")
        print("Option B: (1/√6, -2/√6, 1/√6)")
        print("Option D: (-1/√6, 2/√6, -1/√6)")
        print("="*50)

    else:
        print("\nCould not read solution data. Make sure to run the C program first:")
        
if __name__ == "__main__":
    main()
