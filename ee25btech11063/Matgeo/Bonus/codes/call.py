import subprocess

# Compile the C program
subprocess.run(["gcc", "coplanar.c", "-o", "coplanar.out"])

# Run the compiled program
subprocess.run(["./coplanar.out"])

