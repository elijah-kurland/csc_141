#This code prints the names of the guests invited.
guests = ['Ryan Reynolds', 'Chris Pratt', 'Ewan McGregor']
message = f"Welcome {guests[0].title()}, you have been invited to dinner at 103 road."
print (message)

message = f"Welcome {guests[1].title()}, you have been invited to dinner at 103 road."
print (message)

message = f"Welcome {guests[2].title()}, you have been invited to dinner at 103 road."
print (message)

print (guests[1])
#This will delete and insert a new guest into the list.
del (guests[1])
guests.insert(1, 'Chris Evans')
print (message)
#This updates the messages to the new guests on the list.
message = f"Welcome {guests[1].title()}, you have been invited to dinner at 103 road."
print (message)

message = f"Welcome {guests[2].title()}, you have been invited to dinner at 103 road."
print (message)