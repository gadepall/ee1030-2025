import subprocess

# Compile the C program
subprocess.run(["gcc", "code.c", "-o", "code"])

# Run the compiled C program
result = subprocess.run(["./code"], capture_output=True, text=True)

# Print the output from the C program (solution)
print(result.stdout)