import os
import re

def rename_m4a_files(directory):
    # Change to the specified directory
    os.chdir(directory)

    # List all .m4a files in the directory
    files = [f for f in os.listdir(directory) if f.endswith('.m4a')]

    # Sort files based on the numbers in the filenames
    files.sort(key=lambda x: int(re.search(r'\d+', x).group()))

    # Rename files to sound1.m4a, sound2.m4a, etc.
    for index, file in enumerate(files, start=1):
        new_name = f'sound{index}.m4a'
        os.rename(file, new_name)
        print(f'Renamed "{file}" to "{new_name}"')

# Specify the directory containing the .m4a files
directory = '/home/andrew/Desktop/git_volume/andrew0082.github.io/sound'

rename_m4a_files(directory)
