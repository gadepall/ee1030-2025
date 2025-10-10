import subprocess

# compile the C code
subprocess.run(["gcc", "triangle.c", "-o", "triangle"])

# run the compiled program
subprocess.run(["./triangle"])

