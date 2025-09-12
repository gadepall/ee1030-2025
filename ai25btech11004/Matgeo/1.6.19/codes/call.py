import subprocess

# Compile the C code
subprocess.run(["gcc", "vector.c", "-o", "vector_exec"])

# Run the compiled program
subprocess.run(["./vector_exec"])

# Display contents of the output file
with open("vector.dat", "r") as f:
    print(f.read())
