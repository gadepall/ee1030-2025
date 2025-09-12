import subprocess

# Compile the C program
subprocess.run(["gcc", "axis.c", "-o", "axis"], check=True)

# Run the compiled program
subprocess.run(["./axis"], check=True)

