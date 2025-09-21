import subprocess

# Compile the C program (only once)
subprocess.run(["gcc", "equidistant.c", "-o", "equidistant", "-lm"])

# Run the compiled program and capture output
result = subprocess.run(["./equidistant"], capture_output=True, text=True)

print("Output from C program:")
print(result.stdout)