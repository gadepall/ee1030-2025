import subprocess

# Command to compile the C file
compile_cmd = ["gcc", "solve_equation.c", "-o", "solve_equation"]

# Run the compilation
compile_process = subprocess.run(compile_cmd, capture_output=True, text=True)

# Check for errors
if compile_process.returncode != 0:
    print("Compilation failed:")
    print(compile_process.stderr)
else:
    print("Compilation successful.")

