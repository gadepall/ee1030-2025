import subprocess

# 1. Compile the C program
subprocess.run(["gcc", "direction cosines.c", "-o", "direction cosines"])

# 2. Run the compiled C program
result = subprocess.run(["./direction cosines"], capture_output=True, text=True)

# 3. Print the output from the C program
print(result.stdout)
