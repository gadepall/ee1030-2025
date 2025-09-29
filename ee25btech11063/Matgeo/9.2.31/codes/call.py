import subprocess

# Step 1: Compile the C code
compile = subprocess.run(["gcc", "area.c", "-o", "area", "-lm"], capture_output=True, text=True)

if compile.returncode != 0:
    print("Compilation failed:")
    print(compile.stderr)
else:
    # Step 2: Run the compiled program
    run = subprocess.run(["./area"], capture_output=True, text=True)

    if run.returncode != 0:
        print("Execution failed:")
        print(run.stderr)
    else:
        # Step 3: Read the output from area.dat
        with open("area.dat", "r") as file:
            output = file.read()
            print(output)

