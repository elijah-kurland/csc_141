#Create a dictionary that stores key words and definitions.
glossary = {
    'Boolean':'Represent true and false values.',
    'String':'A series of characters.',
    'Loop':'Works through a collection of items one at a time.',
    'Comment':'A note that describes what the program is doing. It is ignored by the interpreter.',
    'List':'A colloection of items in a certain order.',
    'Float':'A numerical value with a decimal component.',
    'Key':'The first item in a key-value pair in a dictionary.',
    'Dictionary':"A collection of key-value pairs.",
    'Float':'A numerical value with a decimal component.',
    'Conditional test':'A comparison between two values.',
    }

#Prints each term and it's corresponding definition.
for term, definition in glossary.items():
    print(f"\n{term.title()}: {definition}")