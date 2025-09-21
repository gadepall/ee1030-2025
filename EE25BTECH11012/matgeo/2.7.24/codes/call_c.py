import subprocess

# 1. Compile the C program
subprocess.run(["gcc", "area.c", "-o", "area"])

# 2. Run the compiled C program
result = subprocess.run(["./area"], capture_output=True, text=True)

# 3. Print the output from the C program
print(result.stdout)