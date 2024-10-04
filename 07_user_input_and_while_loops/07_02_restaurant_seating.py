#Prompt the user to input the number of people in their dinner group.
dinner_group = input("How many people will be part of your group?")

#Convert the input string to an integer for numerical comparison.
dinner_group = int(dinner_group)

#Check if the number of people exceeds the maximum group size.
if dinner_group > 8:
    #Inform the user that they need to wait for a table if the group is too large.
    print("Sorry, you will have to wait for a table.")
else:
    #Confirm that their table is ready if the group size is acceptable.
    print("Your table is now ready.")