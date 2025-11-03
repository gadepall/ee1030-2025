import subprocess

# Step 1: Compile the C code
compile_result = subprocess.run(["gcc", "solution.c", "-o", "solution.out"])

# Step 2: Check if compilation was successful
if compile_result.returncode == 0:
    # Step 3: Run the compiled executable
    subprocess.run(["./solution.out"])
    print("Executed successfully. Check 'solution.dat' for output.")
else:
    print("Compilation failed.")

