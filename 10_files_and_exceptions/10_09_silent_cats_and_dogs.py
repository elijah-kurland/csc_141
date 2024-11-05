#6/10 This exercise became easier as I eventually understood that I needed to import os and the child directory. 
import os
os.chdir ("C:/Users/capta/OneDrive/Desktop/CSC_141/10_files_and_exceptions")

# List of filenames to read.
filenames = ['cats.txt', 'dogs.txt']

# Loop through each filename in the list.
for filename in filenames:
    
    try:
        # Attempt to open and read the file.
        with open(filename) as f:
            contents = f.read()

    # Handle the case where the file is not found by doing nothing.
    except FileNotFoundError:
        pass

    # If the file is found, print its name and contents.
    else:
        print(f"\nReading file: {filename}")
        print(contents)