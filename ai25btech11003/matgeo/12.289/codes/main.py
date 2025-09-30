#!/usr/bin/env python3
"""
Simple Python program to read main.dat and main.so files for Power Method analysis.
"""

import ctypes
import numpy as np
import os
import sys

def read_dat_file():
    """Read the main.dat file and extract numerical data."""
    if not os.path.exists('main.dat'):
        print("main.dat not found! Creating solution with default values...")
        return create_solution()
    
    print("Reading main.dat file...")
    with open('main.dat', 'r') as f:
        content = f.read()
    
    print("Content of main.dat:")
    print(content)
    print("-" * 40)
    
    # Try to extract eigenvalue from the file
    lines = content.split('\\n')
    eigenvalue = None
    
    for i, line in enumerate(lines):
        if 'eigenvalue' in line.lower() or 'Approximate eigenvalue' in line:
            # Look for the eigenvalue in the next line
            try:
                if i + 1 < len(lines):
                    eigenvalue = float(lines[i + 1].strip())
                    break
            except:
                continue
    
    return eigenvalue

def create_solution():
    """Create the Power Method solution manually."""
    print("\\n=== Power Method Implementation ===")
    
    # Define the matrix A
    A = np.array([[15.0, 4.0, 3.0],
                  [10.0, 12.0, 6.0],
                  [20.0, 4.0, 2.0]])
    
    # Initial vector x0
    x0 = np.array([1.0, 1.0, 1.0])
    
    print("Matrix A:")
    print(A)
    print(f"\\nInitial vector x0: {x0}")
    
    # Iteration 1
    x1 = A @ x0
    max_x1 = np.max(np.abs(x1))
    y1 = x1 / max_x1
    
    print(f"\\nIteration 1:")
    print(f"x1 = A * x0 = {x1}")
    print(f"max(|x1|) = {max_x1}")
    print(f"y1 = x1/{max_x1} = {y1}")
    
    # Iteration 2
    x2 = A @ y1
    max_x2 = np.max(np.abs(x2))
    y2 = x2 / max_x2
    
    print(f"\\nIteration 2:")
    print(f"x2 = A * y1 = {x2}")
    print(f"max(|x2|) = {max_x2}")
    print(f"y2 = x2/{max_x2} = {y2}")
    
    # Calculate eigenvalue using Rayleigh quotient
    eigenvalue = (y2.T @ A @ y2) / (y2.T @ y2)
    
    print(f"\\nApproximate eigenvalue (Rayleigh quotient): {eigenvalue:.8f}")
    
    return eigenvalue

def load_shared_library():
    """Try to load main.so shared library."""
    if not os.path.exists('main.so'):
        print("main.so not found!")
        return None
    
    try:
        lib = ctypes.CDLL('./main.so')
        print("Successfully loaded main.so shared library")
        return lib
    except Exception as e:
        print(f"Error loading main.so: {e}")
        return None

def compare_with_options(eigenvalue):
    """Compare calculated eigenvalue with given options."""
    print("\\n=== Multiple Choice Analysis ===")
    
    options = {
        'a': 7.768,
        'b': 9.468,
        'c': 10.548,
        'd': 19.468
    }
    
    print(f"Calculated eigenvalue: {eigenvalue:.3f}")
    print("\\nGiven options:")
    
    min_diff = float('inf')
    closest_option = None
    
    for option, value in options.items():
        diff = abs(eigenvalue - value)
        print(f"  ({option}) {value:6.3f} - Difference: {diff:6.3f}")
        if diff < min_diff:
            min_diff = diff
            closest_option = option
    
    print(f"\\nClosest option: ({closest_option}) {options[closest_option]}")
    print("Note: The calculated value differs significantly from all given options.")

def verify_with_numpy():
    """Verify using NumPy's eigenvalue calculation."""
    print("\\n=== NumPy Verification ===")
    
    A = np.array([[15.0, 4.0, 3.0],
                  [10.0, 12.0, 6.0],
                  [20.0, 4.0, 2.0]])
    
    eigenvals, eigenvecs = np.linalg.eig(A)
    dominant_eigenval = max(eigenvals.real)
    
    print(f"All eigenvalues: {eigenvals.real}")
    print(f"Dominant eigenvalue: {dominant_eigenval:.8f}")

def main():
    """Main function."""
    print("Power Method Analysis")
    print("=" * 40)
    
    # Try to read from main.dat first
    eigenvalue_from_dat = read_dat_file()
    
    if eigenvalue_from_dat is not None:
        print(f"\\nEigenvalue from main.dat: {eigenvalue_from_dat:.8f}")
        eigenvalue = eigenvalue_from_dat
    else:
        # Calculate it manually
        eigenvalue = create_solution()
    
    # Try to load shared library
    lib = load_shared_library()
    
    # Compare with multiple choice options
    compare_with_options(eigenvalue)
    
    # Verify with NumPy
    verify_with_numpy()
    
    print("\\n" + "=" * 40)
    print("Analysis complete!")

if __name__ == "__main__":
    main()