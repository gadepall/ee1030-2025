import subprocess

# Compile the C program
subprocess.run(["gcc", "inverse.c", "-o", "inverse"])

# Run the compiled program
subprocess.run(["./inverse"])

