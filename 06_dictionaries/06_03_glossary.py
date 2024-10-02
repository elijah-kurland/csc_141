#Create a dictionary that stores key words and definitions.
glossary = {
    'Boolean':'Represent true and false values.',
    'String':'A series of characters.',
    'Loop':'Works through a collection of items one at a time.',
    'Comment':'A note that describes what the program is doing. It is ignored by the interpreter.',
    'List':'A colloection of items in a certain order.',
    }

#Print each key word and it's corresponding definition.
term = 'Boolean'
print(f"\n{term.title()}: {glossary[term]}")

term = 'String'
print(f"\n{term.title()}: {glossary[term]}")

term = 'Loop'
print(f"\n{term.title()}: {glossary[term]}")

term = 'Comment'
print(f"\n{term.title()}: {glossary[term]}")

term = 'List'
print(f"\n{term.title()}: {glossary[term]}")