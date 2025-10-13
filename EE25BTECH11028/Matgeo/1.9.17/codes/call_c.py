# Compile the C program
subprocess.run(["gcc", "equidiistance.c", "-o", "equidistance"])

# Run the compiled C program
result = subprocess.run(["./equidistance"], capture_output=True, text=True)

# Print the output from the C program 
print(result.stdout)