import re
print('---------- Matching Zero or One ----------')
 
randStr = "cat cats"
 
regex = re.compile("[cat]+s?")
 
matches = re.findall(regex, randStr)
 
# Match cat or cats
print("Matches :", len(matches))
 
for i in matches:
    print(i)
print('---------- Matching Zero or More ----------')
# * matches zero or more of what proceeds it
 
randStr = "doctor doctors doctor's"
 
# Match doctor doctors or doctor's
regex = re.compile("[doctor]+['s]*")
 
matches = re.findall(regex, randStr)
 
print("Matches :", len(matches))
 
# You can do the same by setting an interval match
regex = re.compile("[doctor]+['s]{0,2}")
 
matches = re.findall(regex, randStr)
 
print("Matches :", len(matches))
 
for i in matches:
    print(i)

 