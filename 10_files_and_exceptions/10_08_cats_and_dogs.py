#6/10 This exercise became easier as I eventually understood that I needed to import os and the child directory. 
import os
os.chdir ("C:/Users/capta/OneDrive/Desktop/CSC_141/10_files_and_exceptions")

# List of filenames to read.
filenames = ['cats.txt', 'dogs.txt']

# Loop through each filename in the list.
for filename in filenames:
    print(f"\nReading file: {filename}")
    
    try:
        # Attempt to open and read the file.
        with open(filename) as f:
            contents = f.read()
            print(contents)
    
    # Handle the case where the file is not found.
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")