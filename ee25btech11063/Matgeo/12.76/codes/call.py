import subprocess

# Compile with math library (-lm)
subprocess.run(["gcc", "area.c", "-o", "area", "-lm"], check=True)

# Execute the compiled program
subprocess.run(["./area"], check=True)

print("C program executed successfully. Check 'area.adat' for output.")

