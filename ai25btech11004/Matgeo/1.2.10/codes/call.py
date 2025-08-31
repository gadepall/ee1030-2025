import subprocess
import os

# Compile the C code
compile_process = subprocess.run(["gcc", "code.c", "-o", "code.out"])

# Check if compilation was successful
if compile_process.returncode == 0:
    print("Compilation successful. Running the program...\n")
    
    # Run the compiled program
    run_process = subprocess.run(["./code.out"])
else:
    print("Compilation failed.")

