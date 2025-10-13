import subprocess

# Step 1: Compile the C code with -lm
compile_cmd = ["gcc", "eigen.c", "-lm", "-o", "eigen"]
subprocess.run(compile_cmd, check=True)

# Step 2: Run the executable
run_cmd = ["./eigen"]
subprocess.run(run_cmd, check=True)

print("C code executed successfully. Check 'eigen.dat' for results.")

