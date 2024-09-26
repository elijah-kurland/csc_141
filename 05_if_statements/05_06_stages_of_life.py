#Assigns an integer to the age.
age = 18

#Check the age category and print the corresponding message.
if age < 2:
    print("You are a baby.")  #Age is less than 2 years.
elif age < 4:
    print("You are a toddler.")  #Age is between 2 and 4 years.
elif age < 13:
    print("You are a kid.")  #Age is between 4 and 13 years.
elif age < 20:
    print("You are a teenager")  #Age is between 13 and 20 years.
elif age < 65:
    print("You are an adult.")  #Age is between 20 and 65 years.
else:
    print("You are an elder")  #Age is 65 years and older.