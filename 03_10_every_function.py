#List
classes = ['computer programming', 'English', 'Game History', 'Math']

#Delete
del classes[-1]
print (classes)

#Append
classes.append('Math')
print (classes)

#Pop
work=classes.pop(2)
print(classes)
print(work)

#Insert
classes.insert(1,work)
print (classes)

#Sorted
print(sorted(classes))
print(classes)

#Sorted Reverse
print(sorted(classes,reverse=True))
print(classes)

#Reverse
classes.reverse()
print(classes)
classes.reverse()
print (classes)

#Sort)
classes.sort()
print (classes)

#Sort Reverse
classes.sort(reverse=True)
print (classes)