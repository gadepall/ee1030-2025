import subprocess

# Step 1: Compile code.c into an executable
subprocess.run(["gcc", "code.c", "-o", "code"], check=True)

# Step 2: Run the compiled program
subprocess.run(["./code"], check=True)

# Step 3: Read result from answer.dat
with open("answer.dat", "r") as f:
    result = f.read().strip()

print("Value of a+b-c+2d =", result)

