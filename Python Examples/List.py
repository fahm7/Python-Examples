mylist= ['one','two','three','four']
print(mylist)
print mylist[3]

# append  -----
mylist.append('tree')
print(mylist)

# insert  -----
mylist.insert(2,"nest")
print(mylist)

# remove  -----
mylist.remove("nest")
print(mylist)

# del  -----
del mylist[0]
print(mylist)
del  mylist[0]
print(mylist)

# del  -----
del mylist[0:2]
print(mylist)


# extend -----
mylist1= ['blue','green','yellow','red']
mylist.extend(mylist1[1:3])
print(mylist)

#pop
print("PO0000P")
mylist.pop(0)
print(mylist)

mylist= ['one','two','three','four']
mylist.pop()

print(mylist)

#index
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print fruits.index('banana')
# Find next banana starting a position 4
print fruits.index('banana', 4)

#count
print(fruits.count('apple'))

print (fruits.count('tangerine'))
#0
#PLUS
mylist= ['one','two','three','four']
mylist1= ['blue','green','yellow','red']

newlist=mylist+ mylist1
print newlist

print [0,1] + [1,2]
print ("LENGTHS")
print len(mylist)
print len(mylist1)
print len(newlist)