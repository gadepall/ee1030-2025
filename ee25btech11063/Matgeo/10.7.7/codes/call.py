import subprocess

# Compile the C code (slope.c)
subprocess.run(["gcc", "slope.c", "-o", "slope.out"])

# Execute the compiled program
subprocess.run(["./slope.out"])

