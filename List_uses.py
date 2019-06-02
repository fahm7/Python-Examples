list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5, 6]
list2.append([5, 6])

# to check, you can print them out using the print statements below.

print ("showing list1 and list2:")
print (list1)
print (list2)

print ("A list is symmetric if the first row is the same as the first column and so on")
# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(p):
    rows= len(p)
    i=0
    while i<rows:
        #print ("ROWS= ",rows)
        l1= p[i]
        cols= len(l1)
        l2=[]
        j=0
        #print ("COLS = ",cols)

        #print("l1 \n" , l1)

        while j< rows:
            l2.append(p[j][i])
            j=j+1
        i=i+1
        if l1!=l2:
            print("UNEQUAL")
            return False
    return True
        #print("l2 \n",l2)


print (symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]]))
#>>> True

print (symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]]))
#>>> True

print (symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]]))
#>>> False

print (symmetric([[1, 2],
                [2, 1]]))
#>>> True

print (symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]]))
#>>> False

print (symmetric([[1,2,3],
                 [2,3,1]]))
#>>> False