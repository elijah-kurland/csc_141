#Creates an empty tuple of usernames.
usernames = []

for username in usernames:
    #Checks for admin and prints the special message.
    if username == "admin":
        print ("Hello admin, would you like to see a status report?")
    
    #All other names recieve this message.
    else:
        print (f"Hello {username.title()}, thank you for logging in again.")

#If list is empty, this message prints (in this case it does).
else:
    print("We need to find some users!")