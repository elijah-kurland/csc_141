#This code prints the names of the guests invited.
guests = ['Ryan Reynolds', 'Chris Pratt', 'Ewan McGregor']
message = f"Welcome {guests[0].title()}, you have been invited to dinner at 103 road."
print (message)

message = f"Welcome {guests[1].title()}, you have been invited to dinner at 103 road."
print (message)

message = f"Welcome {guests[2].title()}, you have been invited to dinner at 103 road."
print (message)

print ("\n" + guests[1])
#this will delete and insert a new guest into the list.
del (guests[1])
guests.insert(1, 'Chris Evans')

message = f"Welcome {guests[0].title()}, you have been invited to dinner at 103 road."
print ("\n" + message)

message = f"Welcome {guests[1].title()}, you have been invited to dinner at 103 road."
print (message)

message = f"Welcome {guests[2].title()}, you have been invited to dinner at 103 road."
print (message)

#A new table was found and more guests can now show up.
new_message = "We have found a larger table and will be inviting more guests."
print ("\n" + new_message)
#This adds more guests to the list and appends one of them.
guests.insert(0, 'Mark Hamill')
guests.insert(1, 'Same Witwer')
guests.append('Oscar Isaac')
#This updates the list of invited guest messages.
message = f"Welcome {guests[0].title()}, you have been invited to dinner at 103 road."
print ("\n" + message)

message = f"Welcome {guests[1].title()}, you have been invited to dinner at 103 road."
print (message)

message = f"Welcome {guests[2].title()}, you have been invited to dinner at 103 road."
print (message)

message = f"Welcome {guests[3].title()}, you have been invited to dinner at 103 road."
print (message)

message = f"Welcome {guests[4].title()}, you have been invited to dinner at 103 road."
print (message)

message = f"Welcome {guests[5].title()}, you have been invited to dinner at 103 road."
print (message)