import subprocess

# Step 1: Compile the C code
compile_cmd = ["gcc", "code.c", "-o", "code.out"]
compilation = subprocess.run(compile_cmd, capture_output=True, text=True)

# Check for compilation errors
if compilation.returncode != 0:
    print(" Compilation failed:")
    print(compilation.stderr)
else:
    print(" Compilation successful. Running the program...\n")

    # Step 2: Run the compiled program
    run_cmd = ["./code.out"]
    subprocess.run(run_cmd)

