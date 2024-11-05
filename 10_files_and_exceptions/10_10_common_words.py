#9/10 This exercise was very challenging to write and import the text file. This was a trial and error code. 
def count_common_words(filename, word):
    """Count how many times the specified word appears in the text."""
    try:
        # Attempt to open the file.
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    # Handle the case where the file is not found.
    except FileNotFoundError:
        pass
    else:
        # Count occurrences of the word.
        word_count = contents.lower().count(word)

        # Prepare and print the message with the count.
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

# Specify the filename and the word to count.
filename = "C:/Users/capta/Downloads/pg36-h/war.txt.html"
count_common_words(filename, 'war')