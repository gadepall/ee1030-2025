import subprocess

# Compile the C code
subprocess.run(["gcc", "inverse.c", "-o", "inverse"])

# Run the compiled program
subprocess.run(["./inverse"])

# Display the output written in inverse.dat
with open("inverse.dat", "r") as file:
    print(file.read())

