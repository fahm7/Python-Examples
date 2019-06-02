
print('________________________STRINGS_________________________')

s = "I am a string"
print(s)

mys = 'abcdefghijklmnopqrstuvwxyz'
print(mys)

print(type(mys))

name = 'Dave'
print ('Hello ' + name + '!' + '!' + '!')


mys = 'abcdefghijklmnopqrstuvwxyz'
print(mys[0] )

print(mys[1+2])

name = 'Fahm'
print (name[-1])

# REPEAT
word = 'assume'
print (word * 3)
print( word[2:4])




print('________________________STRINGS FUNCTIONS_________________________')

print ('{} {} {}'.format('a', 'b', 'c'))

# Numbered fields refer to the position of the arguments
print('{2} {1} {0}'.format('a', 'b', 'c') )

pythagoras = 'There is geometry in the humming of the strings,' \
             ' there is music in the spacing of the spheres. '

print (pythagoras.find('string'))
#40
print (pythagoras.find('algebra'))
#-1

danton = "De l'audace, encore de l'audace, toujours de l'audace."

print(danton.find('audace'))

print(danton.find('audace', 6))

# more on string functions
#https://docs.python.org/3/library/stdtypes.html#string-methods



print('________________________STRINGS FUNCTIONS USES_________________________')

user_ip='208.94.117.90'
url= 'accessed /bears/koala'
now='16:20'
log_message = "IP address {} accessed {} at {}".format(user_ip, url, now)
print (log_message)

