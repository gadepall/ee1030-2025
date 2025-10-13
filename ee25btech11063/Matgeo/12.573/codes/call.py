import subprocess
import os

# Step 1: Compile the C program
compile_process = subprocess.run(["gcc", "vector.c", "-o", "vector"], capture_output=True, text=True)

# Check for compilation errors
if compile_process.returncode != 0:
    print("Compilation failed:\n", compile_process.stderr)
else:
    print("Compilation successful. Running the program...\n")

    # Step 2: Execute the compiled program
    run_process = subprocess.run(["./vector"], capture_output=True, text=True)

    # Print program output (e.g., success message)
    print(run_process.stdout)

    # Step 3: Check if the output file 'vector.dat' exists
    if os.path.exists("vector.dat"):
        print("Contents of vector.dat:\n")
        with open("vector.dat", "r") as f:
            print(f.read())
    else:
        print("Error: vector.dat file not found.")

