# declare (make) a list
listName = []  # empty list
anotherList = [3, 6, 7, 1, 5, 8, 0, 1, 5]

# print a list
print anotherList

# add another thing to the END of the list
listName.append(14)
listName.append(15)
listName.append(12)
listName.append(1)
print listName

# add another thing to a specific location
listName.insert(0, 7) # (index, value)
listName.insert(3, 100)
print listName

# find where in the list something is
# probably wont need to use
print listName.index(12)

# access individual indexes
# get a value at a particular index
print listName[0]
print listName[3]

# sort the list
listName.sort()
print listName

# remove a value from the list
listName.remove(15)
print listName

# remove a value by index
del listName[0]
print listName

# get the length of the list
print len(listName)

# for loop through the list and change each element
for num in range(0, len(listName)):
    listName[num] += 1
print listName

# for loop through the list, getting each element
for num in listName:
    print num




