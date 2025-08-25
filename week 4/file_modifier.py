import os

filename = "hello.txt"

try:
    with open(filename, 'r') as file:
        content = file.read()

    modified_content = content.upper()
    base_name = os.path.basename(filename)
    new_filename = f"modified_{base_name}"

    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"File successfully modified and saved as '{new_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
