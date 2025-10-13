import os
import subprocess

# Compile the C program
compile_command = ["gcc", "circle.c", "-o", "circle"]
run_command = ["./circle"]

# Compile
compilation = subprocess.run(compile_command, capture_output=True, text=True)

if compilation.returncode != 0:
    print("Compilation failed:")
    print(compilation.stderr)
else:
    print("Compilation successful. Running program...\n")
    # Run the compiled executable
    run = subprocess.run(run_command, capture_output=True, text=True)
    print(run.stdout)
    print("Program finished. Output written to circle.dat")

