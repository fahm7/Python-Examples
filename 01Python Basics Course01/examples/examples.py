s1 ="<apc>"
print s1[1]
print s1[0++1]
print s1+s1[0]
print (s1+s1)[0]

f= "Faheem"
print(f[3])
print(f[3:4])
print(f[3:6])
print(f[:2])

s='number'
t='number'
i=1

print(s.find(t,i))

# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url', 
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
temp = page[start_link:]
no_end=temp.find("com")
no_st=temp.find("http")

url=temp[no_st:no_end+3]
print(url)


# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.
def print_numbers(num):
	count = 1;
	while(count<=num):
	  print(count)
	  count=count+1
print_numbers(10)	

print("______________FACTORIAL_____________________")
# factorial of a given number
def factorial(n):
	 fact = 1
	 while n>0:
	      fact = fact*n
	      n=n-1
	 return fact
	 	
     

print(factorial(4))	


# list in python
print("______________LIST_____________________")

p=[1,2]
q=[3,4]

p.append(q)
print(p)
print('-q=----')
print(q)


