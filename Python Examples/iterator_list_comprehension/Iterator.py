sampStr = iter("Sample")

print("Char :", next(sampStr))
print("Char :", next(sampStr))


class Alphabet:

    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1

    def __iter__(self):
        return self
# python 3.X
    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index += 1
        return self.letters[self.index]


alpha = Alphabet()

for letter in alpha:
    print(letter)

x = [i for i in range(10)]
print (x)

# This will give the output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


