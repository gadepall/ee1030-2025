import subprocess

# Compile C program
subprocess.run(["gcc", "points.c", "-o", "points"], check=True)

# Run the compiled program
subprocess.run(["./points"], check=True)

