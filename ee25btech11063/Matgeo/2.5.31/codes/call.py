import subprocess

# Compile with math library linked (-lm)
compile_process = subprocess.run(["gcc", "code.c", "-o", "code", "-lm"], capture_output=True, text=True)

if compile_process.returncode != 0:
    print("Compilation failed:\n", compile_process.stderr)
else:
    # Run the compiled executable
    run_process = subprocess.run(["./code"], capture_output=True, text=True)
    print(run_process.stdout)

    # Read and print the contents of triangle.dat
    with open("triangle.dat", "r") as f:
        print(f.read())

