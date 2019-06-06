print('________________________FUNCTION INBUILD________________________')

i = 56
print(type(i))
print('________________________FUNCTION INBUILD  Simple Function________________________')


# funtion with no return type

def display_greatings():
    print("Welcome all to the journey of Python")


print(display_greatings());

# Example to return for funtion
print('________________________FUNCTION INBUILD FUNCTION WITH RETURN TYPE________________________')


def vol(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2


print(vol(10, 3))

result = vol(10, 3)

print("Volume fo the cylinder H= 10, r= 3 is {}".format(result))


#############STRING#######################

print(str(b'Zoot!'))
print('01\t012\t0123\t01234'.expandtabs())

mystring = 'abcdefghijklmnopqrstuvwxyz'
print(mystring)
print(mystring.capitalize())
print(mystring.casefold())

print(mystring.find('fgh', 0, 16))

print('fgh' in mystring)
