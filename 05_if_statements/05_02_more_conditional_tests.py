fruit_1 = "apple"
fruit_2 = "mango"
fruit_3 = "orange"
fruit_4 = "Apple"

#Equality of strings/lower method tests

if (fruit_1.lower() == (fruit_4.lower())):
    print("Equal!")
else:
    print("Unequal!")

# Inequality of strings

if(fruit_1 != fruit_2):
    print("The fruits are unequal")
else:
    print("The fruits are equal")

# Numerical tests

age_1 = 18

age_2 = 23

if (age_1 == 18):
    print("Person is eligible to vote")

if(age_1 != 23):
          print("Person cannot drink")

if(age_1 <= age_2):
    print("Yonger")

if(age_2 >= age_1):
    print("Older")

# and/or keyword test
if (age_1 == 18 or age_2 >= 23):
    print("Person is eligible for voting")

if(age_1 == 18 and age_2 == 23):
    print("Age difference is 5 years")

## Item in list or not test
classes = ['math', 'science', 'history']
if 'math' in classes:
    print("Math appears in classes.")
if 'art' not in classes:
    print("Art does not appear in classes.")