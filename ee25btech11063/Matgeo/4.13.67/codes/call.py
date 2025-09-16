import subprocess

# Step 1: Compile the C code (locus.c -> executable "locus")
compile_cmd = ["gcc", "locus.c", "-o", "locus"]
compilation = subprocess.run(compile_cmd, capture_output=True, text=True)

# Check for compilation errors
if compilation.returncode != 0:
    print("Compilation failed!")
    print(compilation.stderr)
else:
    print("Compilation successful.")

    # Step 2: Run the compiled program
    run_cmd = ["./locus"]
    execution = subprocess.run(run_cmd, capture_output=True, text=True)

    print("Program output:")
    print(execution.stdout)

    if execution.stderr:
        print("Program errors:")
        print(execution.stderr)

