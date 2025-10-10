import subprocess

# Compile the C code
subprocess.run(["gcc", "matrix.c", "-o", "matrix.out"])

# Run the compiled program
subprocess.run(["./matrix.out"])

