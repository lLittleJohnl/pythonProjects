import os
import re

# Set the directory containing the music files
directory = r"C:\Users\joaov\Music\Louvores"

# Get a list of all the files in the directory
files = os.listdir(directory)

# Define a regular expression to match unwanted characters in the title and artists information
cleanup_regex = re.compile(r'[^a-zA-Z0-9]+')

# Loop through each file
for filename in files:
    # Skip files that are not music files
    if not filename.endswith(".mp3"):
        continue

    # Split the filename into the title and artists information
    title, artists = filename.split(" - ")

    # Clean up the title and artists information using the regular expression
    cleaned_title = re.sub(cleanup_regex, "", title)
    cleaned_artists = re.sub(cleanup_regex, "", artists)

    # Construct the new filename
    new_filename = "{} - {}.mp3".format(cleaned_title, cleaned_artists)
    new_file_path = os.path.join(directory, new_filename)

    # Rename the file
    file_path = os.path.join(directory, filename)
    os.rename(file_path, new_file_path)