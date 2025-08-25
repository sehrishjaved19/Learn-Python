import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Contents of Directory: {current_directory}\n")

# List all files and directories in current directory
items = os.listdir(current_directory)

# Print each item
for item in items:
    print(item)
