import subprocess

try:
    subprocess.run(["gcc", "problem.c", "-o", "problem","-lm"], check=True)

    result = subprocess.run(["./problem"], capture_output=True, text=True, check=True)
    
    print(result.stdout)

except (subprocess.CalledProcessError, FileNotFoundError) as e:
    # If anything goes wrong, print a simple error message.
    print(f"An error occurred: {e}")
