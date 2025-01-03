import subprocess

# Define the bash commands you want to run in order
command = "sudo hcitool lescan" 

# Run the command in a subprocess
process = subprocess.run(command, shell=True, text=True)

# Print the output
print("Output:")
print(process.stdout)

# Print any errors
if process.stderr:
    print("Error:")
    print(process.stderr)
