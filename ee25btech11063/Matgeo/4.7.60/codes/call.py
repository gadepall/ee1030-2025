import subprocess

# Compile the C program with -lm (link math library)
subprocess.run(["gcc", "norm.c", "-o", "norm", "-lm"], check=True)

# Run the compiled program
subprocess.run(["./norm"], check=True)

