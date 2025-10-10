import subprocess

# Compile the C code
subprocess.run(["gcc", "ellipse.c", "-o", "ellipse"])

# Run the compiled program
subprocess.run(["./ellipse"])

