import subprocess

# Compile the C code
subprocess.run(["gcc", "solution.c", "-o", "solution"])

# Run the compiled executable
subprocess.run(["./solution"])

