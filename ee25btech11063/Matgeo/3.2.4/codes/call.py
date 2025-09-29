# run_triangle.py
import subprocess
import sys

# compile (math library linked just in case)
subprocess.run(["gcc", "triangle.c", "-o", "triangle.out", "-lm"], check=True)

# run
subprocess.run(["./triangle.out"], check=True)

# print file content
with open("triangle.dat", "r") as f:
    print(f.read())

