class Stack:

    def __init__(self):
        self.stack = []

    def push(self, val):
        # Use list append method to add element
        return self.stack.append(val)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0



mystack = Stack()
mystack.push("Mon")
mystack.push("Tue")

print (mystack.size())
print (mystack.pop())
print (mystack.size())

print (mystack.peak())
