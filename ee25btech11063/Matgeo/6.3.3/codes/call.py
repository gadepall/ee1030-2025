import subprocess

import subprocess
import sys
import os

# compile command: note the "-lm" at the end to link the math library
compile_cmd = ["gcc", "line.c", "-o", "line.out", "-lm"]

print("Compiling:", " ".join(compile_cmd))
proc = subprocess.run(compile_cmd, capture_output=True, text=True)

if proc.returncode != 0:
    print("Compilation failed.\n--- stdout ---")
    print(proc.stdout)
    print("--- stderr ---")
    print(proc.stderr)
    sys.exit(proc.returncode)

print("Compilation succeeded.\nRunning ./line.out ...")
proc = subprocess.run(["./line.out"], capture_output=True, text=True)

if proc.returncode != 0:
    print("Program exited with an error.\n--- stdout ---")
    print(proc.stdout)
    print("--- stderr ---")
    print(proc.stderr)
    sys.exit(proc.returncode)

# If the program runs, read and print line.dat
dat_file = "line.dat"
if os.path.exists(dat_file):
    print(f"\nContents of {dat_file}:")
    with open(dat_file, "r") as f:
        print(f.read())
else:
    print(f"{dat_file} was not created.")

