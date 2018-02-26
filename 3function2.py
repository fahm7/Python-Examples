#Write a function named readable_timedelta. 
#The function should take one argument, an integer days, 
#and return a string that says how many weeks and days that is. 
#For example, readable_timedelta(10) should return, 1 week(s) and 3 day(s).

def readable_timedelta(numer_of_days):
	print ("***Printing the number of weeks and days in the given number of days***")

	weeks = numer_of_days//7 # two slashes will round of and give the number
	days = numer_of_days %7

	return " {} weeks and {} days".format(weeks,days)


print(readable_timedelta(20))	

print(readable_timedelta(7))	

print(readable_timedelta(365))