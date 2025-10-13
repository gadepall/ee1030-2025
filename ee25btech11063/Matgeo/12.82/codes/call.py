import subprocess
import os

# Step 1: Compile the C code
compile_cmd = ["gcc", "eigen.c", "-o", "eigen", "-lm"]
print("Compiling eigen.c ...")
compilation = subprocess.run(compile_cmd, capture_output=True, text=True)

# Check for compilation errors
if compilation.returncode != 0:
    print("Compilation failed:")
    print(compilation.stderr)
    exit(1)

print("Compilation successful.")

# Step 2: Run the compiled executable
print("Running the program ...")
run_cmd = ["./eigen"]
execution = subprocess.run(run_cmd, capture_output=True, text=True)

# Show program output (if any)
print(execution.stdout)
if execution.stderr:
    print("Errors:\n", execution.stderr)

# Step 3: Display contents of eigen.dat
if os.path.exists("eigen.dat"):
    print("\n--- Contents of eigen.dat ---")
    with open("eigen.dat", "r") as f:
        print(f.read())
else:
    print("Output file eigen.dat not found.")

