import subprocess

try:
    subprocess.run(["gcc", "mid.c", "-o", "mid","-lm"], check=True)

    result = subprocess.run(["./mid"], capture_output=True, text=True, check=True)
    
    print(result.stdout)

except (subprocess.CalledProcessError, FileNotFoundError) as e:
    # If anything goes wrong, print a simple error message.
    print(f"An error occurred: {e}")