

class Stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        if self.data == 0:
            return 'Stack is empty'
        return self.data[-1]

    def push(self, value):
        self.data.append(value)
        return self


    def pop(self):
        if len(self.data) == 0:
            return 'Stack is empty'
        return self.data.pop()



new_stack = Stack()
print(new_stack.push('Google'))
print(new_stack.peek())
print(new_stack.push('Udemy'))
print(new_stack.peek())
print(new_stack.push('Discord'))
print(new_stack.peek())
print(new_stack.pop())
print(new_stack.pop())
print(new_stack.pop())
