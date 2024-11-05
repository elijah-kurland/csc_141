#4/10 This exercise was easier after understanding 10-1.
import os
os.chdir("C:/Users/capta/OneDrive/Desktop/CSC_141/10_files_and_exceptions")

filename = 'learning_python.txt'

# Open the file and read all lines into a list.
with open(filename) as f:
    lines = f.readlines()

# Process each line
for line in lines:
    # Remove newline and replace 'Python' with 'C'.
    line = line.rstrip()
    print(line.replace('Python', 'C'))
