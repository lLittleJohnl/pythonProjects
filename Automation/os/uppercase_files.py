import os


### MUSIC ###

# Set the directory containing the music files
directory = r""

# Get a list of all the files in the directory
files = os.listdir(directory)

# Loop through each file
for filename in files:
    # Skip files that are not music files
    if not filename.endswith(".mp3"):
        continue

    # Construct the full path to the file
    file_path = os.path.join(directory, filename)

    # Rename the file to uppercase
    new_filename = filename.upper()
    new_file_path = os.path.join(directory, new_filename)
    os.rename(file_path, new_file_path)

### PDF ###

# Set the directory containing the music files
directory = r"path"

# Get a list of all the files in the directory
files = os.listdir(directory)

# Loop through each file
for filename in files:
    # Skip files that are not music files
    if not filename.endswith(".pdf"):
        continue

    # Construct the full path to the file
    file_path = os.path.join(directory, filename)

    # Rename the file to uppercase
    new_filename = filename.upper()
    new_file_path = os.path.join(directory, new_filename)
    os.rename(file_path, new_file_path)