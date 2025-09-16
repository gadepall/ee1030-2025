import subprocess

# 1. Compile the C program
subprocess.run(["gcc", "code.c", "-o", "code"])

# 2. Run the compiled C program
result = subprocess.run(["./code"], capture_output=True, text=True)

# 3. Print the output from the C program
print(result.stdout)