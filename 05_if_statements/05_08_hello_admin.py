#Creates a tuple of usernames.
usernames = ('admin', 'jack', 'ryan', 'avery', 'catherine')

for username in usernames:
    #Prints the special message for the admin.
    if username == "admin":
        print ("Hello admin, would you like to see a status report?")
    
    #Prints message for everyone who isn't the admin.
    else:
        print (f"Hello {username.title()}, thank you for logging in again.")