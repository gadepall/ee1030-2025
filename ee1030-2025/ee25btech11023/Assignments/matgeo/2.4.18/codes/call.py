import subprocess

try:
    subprocess.run(["gcc", "direction_vector.c", "-o", "direction_vector","-lm"], check=True)

    result = subprocess.run(["./direction_vector"], capture_output=True, text=True, check=True)
    
    print(result.stdout)

except (subprocess.CalledProcessError, FileNotFoundError) as e:
    # If anything goes wrong, print a simple error message.
    print(f"An error occurred: {e}")