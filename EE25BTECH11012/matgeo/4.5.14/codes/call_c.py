import subprocess
import os

# Determine the executable name based on the operating system
executable_name = 'line_program'
if os.name == 'nt':  # 'nt' is the name for Windows
    executable_name += '.exe'

# Prepend './' to specify the current directory
executable_path = os.path.join('.', executable_name)

    # Run the C program as a subprocess
    # capture_output=True saves its output
    # text=True decodes the output as text
    # check=True raises an error if the C program fails
    result = subprocess.run(
        [executable_path],
        capture_output=True,
        text=True,
        check=True
    )

    # Print the output that was captured from the C program
    print(result.stdout)