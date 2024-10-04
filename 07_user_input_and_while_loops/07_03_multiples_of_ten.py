#Prompt the user to enter a number.
number = input("Enter a number and I'll tell you if it's a multiple of ten:")

#Convert the input string to an integer.
number = int(number)

#Check if the number is a multiple of ten.
if number % 10 == 0:
    #Inform the user that the number is a multiple of ten.
    print(f"The number {number} is a multiple of ten.")
else:
    #Inform the user that the number is not a multiple of ten.
    print(f"The number {number} is not a multiple of ten.")