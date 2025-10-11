import os
import ctypes
import platform
import matplotlib.pyplot as plt

def compile_c_code():
    """Compiles the main.c file into a shared library."""
    c_file = "main.c"
    if not os.path.exists(c_file):
        print(f"Error: {c_file} not found.")
        return None

    # Define library name based on OS
    system = platform.system()
    if system == "Windows":
        lib_name = "main.dll"
        compile_command = f"gcc -shared -o {lib_name} -fPIC {c_file}"
    else: # Linux, macOS
        lib_name = "main.so"
        compile_command = f"gcc -shared -o {lib_name} -fPIC {c_file}"
        
    print(f"Compiling C code with: {compile_command}")
    
    # Check if compilation is successful
    if os.system(compile_command) != 0:
        print("C code compilation failed.")
        return None
        
    print("Compilation successful.")
    return lib_name

def main():
    """
    Main function to run the verification and plot the results.
    """
    lib_name = compile_c_code()
    if not lib_name:
        return

    # Load the shared library
    try:
        c_lib = ctypes.CDLL(os.path.join(os.getcwd(), lib_name))
    except Exception as e:
        print(f"Failed to load library: {e}")
        return

    # Define the function signatures (argtypes and restype) for type safety
    c_lib.solve_part_a.argtypes = [ctypes.c_int]
    c_lib.solve_part_a.restype = ctypes.c_int
    c_lib.solve_part_b.argtypes = [ctypes.c_int]
    c_lib.solve_part_b.restype = ctypes.c_int
    c_lib.solve_part_c.argtypes = [ctypes.c_int]
    c_lib.solve_part_c.restype = ctypes.c_int

    # --- Verification ---
    test_primes = [3, 5, 7, 11] # Keep the list small as C code is a full brute-force search
    
    results = {'p': test_primes, 'a': [], 'b': [], 'c': []}
    theoretical = {'p': test_primes, 'a': [], 'b': [], 'c': []}

    print("\n--- Verification Report (C Implementation vs Theory) ---")
    for p in test_primes:
        print(f"\n--- Verifying for p = {p} ---")
        
        # Part A
        num_a = c_lib.solve_part_a(p)
        the_a = 2 * p - 1
        results['a'].append(num_a)
        theoretical['a'].append(the_a)
        print(f"  Part (a): Numerical = {num_a:<5} | Theoretical (2p-1) = {the_a:<5} -> {'Match' if num_a == the_a else 'Mismatch'}")

        # Part B
        num_b = c_lib.solve_part_b(p)
        the_b = (p - 1)**2
        results['b'].append(num_b)
        theoretical['b'].append(the_b)
        print(f"  Part (b): Numerical = {num_b:<5} | Theoretical ((p-1)^2) = {the_b:<5} -> {'Match' if num_b == the_b else 'Mismatch'}")
        
        # Part C
        num_c = c_lib.solve_part_c(p)
        the_c = p**3 - p**2
        results['c'].append(num_c)
        theoretical['c'].append(the_c)
        print(f"  Part (c): Numerical = {num_c:<5} | Theoretical (p^3-p^2) = {the_c:<5} -> {'Match' if num_c == the_c else 'Mismatch'}")

    # --- Plotting ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, axes = plt.subplots(3, 1, figsize=(10, 15), sharex=True)
    fig.suptitle('C Numerical Verification vs. Theoretical Formulas (Assuming d=a)', fontsize=16)
    
    colors = {'a': 'red', 'b': 'green', 'c': 'blue'}
    titles = {'a': 'Part (a): Symmetric/Skew-Symmetric, det(A)=0', 'b': 'Part (b): tr(A)!=0, det(A)=0', 'c': 'Part (c): det(A)!=0'}
    formulas = {'a': '2p - 1', 'b': '(p - 1)^2', 'c': 'p^3 - p^2'}
    
    for i, part in enumerate(['a', 'b', 'c']):
        ax = axes[i]
        color = colors[part]
        ax.plot(results['p'], results[part], 'o', markersize=8, color=color, label='Numerical Count (from C code)')
        ax.plot(theoretical['p'], theoretical[part], '--', color=color, label=f'Theoretical Formula: {formulas[part]}')
        ax.set_title(titles[part])
        ax.set_ylabel('Number of Matrices')
        ax.legend()
        ax.grid(True)
    
    axes[-1].set_xlabel('Prime number (p)')
    plt.xticks(test_primes)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    
    # Save the figure
    plt.savefig('figure_all_parts.png')
    print("\nPlot saved as figure_all_parts.png")
    
    plt.show()

if __name__ == "__main__":
    main()


