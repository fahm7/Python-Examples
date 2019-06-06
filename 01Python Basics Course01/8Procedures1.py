# Factorial
def factorial(n):
    if n > 0:
        factorial(n - 1)
    else:
        return 1

    return n * factorial(n - 1)


print(factorial(0))

print(factorial(1))
print(factorial(5))
print(factorial(10))


#palindrome
def is_palindrome(s):
    print(s)
    if s == '' :
        print("empty")
        return True
    else:
        if s[0] == s[-1]:
            #print(s[0])
            is_palindrome(s[1:-1])
        else:
            return False



print(is_palindrome('madam'))
print(is_palindrome('school'))

