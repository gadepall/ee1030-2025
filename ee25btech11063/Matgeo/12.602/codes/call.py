import subprocess

# Compile the C code (assuming it's saved as program.c)
subprocess.run(["gcc", "program.c", "-o", "program"], check=True)

# Run the compiled program
subprocess.run(["./program"], check=True)

# Read and print the result from answer.dat
with open("answer.dat", "r") as f:
    output = f.read()

print("Output from answer.dat:\n")
print(output)

