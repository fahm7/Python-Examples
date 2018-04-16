# define a funtion  that takes agument as funtion

def our_decorator(func):
    # write a inner funtion , that modifies the funtion received
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)

    return function_wrapper


def foo(x):
    print("Hi, foo has been called with " + str(x))


print("We call foo before decoration:")
foo("Hi")
print("__"*20)

print("We now call our_decorator - decorte foo")
print("__"*20)
foo = our_decorator(foo)
print("__"*20)

print("We call foo after decoration:")
print("__"*20)
foo("Hi")

print("__"*20)
foo("50")


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))
print("**"*20)
foo("Hi")


print("__"*10+"with random"+"__"*10)
from random import random, randint, choice
def our_decorator(func):
    def function_wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        res = func(*args, **kwargs)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

with_random = our_decorator(random)
with_randint = our_decorator(randint)
with_choice = our_decorator(choice)

with_random()
with_randint(3, 8)
with_choice([4, 5, 6])


#####################################################
print("__"*10+"Use case"+"__"*10)
def argument_test_natural_number(f):

    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper


@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


for i in range(1, 10):
    print(i, factorial(i))

print(factorial(-1))
