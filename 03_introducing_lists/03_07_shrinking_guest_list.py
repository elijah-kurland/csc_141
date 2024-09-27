#This sends a new message to the currently invited guests.
guests = ['Ryan Reynolds', 'Chris Pratt', 'Ewan McGreggor']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

#Deletes a guest off of the list.
del(guests[1])
guests.insert(1, 'Chris Evans')

#Prints the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

#A new table was found and more guests can show up.
print("\n""We got a bigger table!")
guests.insert(0, 'Mark Hammil')
guests.insert(2, 'Sam Witwer')
guests.append('Oscar Isaac')

name = guests[0].title()
print("\n"f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")

#Updates the list to tell some of the guests that they are no longer invited.
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

#There should be two people left to invite.
name = guests[0].title()
print("\n"f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

#Empties the list.
del(guests[0])
del(guests[0])

#Prints the current two guests left.
print(guests)