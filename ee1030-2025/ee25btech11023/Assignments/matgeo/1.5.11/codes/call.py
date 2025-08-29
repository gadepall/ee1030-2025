import subprocess

try:
    subprocess.run(["gcc", "section.c", "-o", "section","-lm"], check=True)

    result = subprocess.run(["./section"], capture_output=True, text=True, check=True)
    
    print(result.stdout)

except (subprocess.CalledProcessError, FileNotFoundError) as e:
    # If anything goes wrong, print a simple error message.
    print(f"An error occurred: {e}")