import os
import shutil

# Function to recursively rename files to lowercase
def rename_to_lowercase(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            # Get the full file path
            file_path = os.path.join(root, file)
            # Check if the file name is already in lowercase
            if file.islower():
                continue
            # Create the new lowercase file name
            new_file_name = file.lower()
            # Create the new file path
            new_file_path = os.path.join(root, new_file_name)
            # Rename the file
            shutil.move(file_path, new_file_path)
            print(f'Renamed: {file_path} -> {new_file_path}')

directory_path = '/home/erodgers/Desktop/Scripts/'
rename_to_lowercase(directory_path)