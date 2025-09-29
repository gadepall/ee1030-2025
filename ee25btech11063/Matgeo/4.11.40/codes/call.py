import subprocess

# Compile the C code with math library
compile_result = subprocess.run(["gcc", "area.c", "-o", "area.out", "-lm"])

if compile_result.returncode != 0:
    print("Compilation failed!")
else:
    # Run the compiled program
    subprocess.run(["./area.out"])

    # Display contents of area.dat
    with open("area.dat", "r") as f:
        print("Contents of area.dat:")
        print(f.read())

