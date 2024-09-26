#Creates a tuple of numbers 1-9
numbers = ('1','2','3','4','5','6','7','8','9')

#Checks for number 1 and prints the correct ordinal form.
for number in numbers:
    if number == '1':
        print ("1st")

#Checks for number 2 and prints the correct ordinal form.
    elif number == '2':
        print ("2nd")

#Checks for number 3 and prints the correct ordinal form.
    elif number == '3':
        print ("3rd")

#Prints the "th" for all other numbers in the tuple.
    else:
        print(f"{number}th")