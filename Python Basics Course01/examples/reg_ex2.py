import re

print('---------- Matching Multiple Numbers ----------')
# You can match multiple digits by following the \d with {numOfValues}
 
# Match 5 numbers only
if re.search("\d{5}", "12345"):
    print("It is a zip code")
 
# You can also match within a range
# Match values that are between 5 and 7 digits
numStr = "123 12345 123456 1234567"
 
print("Matches :", len(re.findall("\d{5,7}", numStr)))
 
print('---------- Matching Any Single Letter or Number ----------')
# \w is the same as [a-zA-Z0-9_]
# \W is the same as [^a-zA-Z0-9_]
 
phNum = "412-555-1212"
 
# Check if it is a phone number
if re.search("\w{3}-\w{3}-\w{4}", phNum):
    print("It is a phone number")
 
# Check for valid first name between 2 and 20 characters
if re.search("\w{2,20}", "Ultraman"):
    print("It is a valid name")
 
print('---------- Matching WhiteSpace ----------')
# \s is the same as [\f\n\r\t\v]
# \S is the same as [^\f\n\r\t\v]
 
# Check for valid first and last name with a space
if re.search("\w{2,20}\s\w{2,20}", "Toshio Muramatsu"):
    print("It is a valid full name")
 
# ---------- Matching One or More ----------
# + matches 1 or more characters
 
# Match a followed by 1 or more characters
print("Matches :", len(re.findall("a+", "a as ape bug")))

print('---------- Problem ----------')

# Create a Regex that matches email addresses from a list
# 1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters
 
emailList = "db@aol.com m@.com @apple.com db@.com"
 
print("Email Matches :", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",
                                        emailList)))