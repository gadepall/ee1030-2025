import subprocess
import sys

# Compile code.c -> plgm_out and link math library with -lm
try:
    subprocess.run(["gcc", "code.c", "-o", "plgm_out", "-lm"], check=True)
except subprocess.CalledProcessError as e:
    print("Compilation failed:", e)
    sys.exit(1)

# Run the produced executable (which creates plgm.dat)
try:
    subprocess.run(["./plgm_out"], check=True)
except subprocess.CalledProcessError as e:
    print("Execution failed:", e)
    sys.exit(1)

print(" Done. 'plgm.dat' should be in the current directory.")

