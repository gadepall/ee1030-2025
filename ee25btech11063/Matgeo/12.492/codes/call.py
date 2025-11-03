import subprocess

# Compile the C program with -lm
subprocess.run(["gcc", "dc.c", "-o", "dc.out", "-lm"])

# Run the compiled C program
subprocess.run(["./dc.out"])

# Read and print the output file
with open("dc.dat", "r") as f:
    print(f.read())

