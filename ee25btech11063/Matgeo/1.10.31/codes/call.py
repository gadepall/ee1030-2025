import subprocess

# Step 1: Create vector.dat automatically
with open("vector.dat", "w") as f:
    f.write("14 2 3 -6\n")   # You can change values here if needed

# Step 2: Compile the C code with -lm (math library)
compile_result = subprocess.run(["gcc", "code.c", "-o", "vector", "-lm"], capture_output=True, text=True)

if compile_result.returncode != 0:
    print("Compilation failed:\n", compile_result.stderr)
else:
    print("Compilation successful. Running program...\n")
    # Step 3: Run the compiled program
    run_result = subprocess.run(["./vector"], capture_output=True, text=True)
    
    # Step 4: Print program output (results or error from C code)
    if run_result.stdout.strip():
        print(run_result.stdout.strip())
    if run_result.stderr.strip():
        print("Runtime error:\n", run_result.stderr.strip())

