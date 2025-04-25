class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def print_list(self):
        my_list = []
        current_node = self.top
        while current_node != None:
            my_list.append(current_node.data)
            current_node = current_node.next
        return my_list

    def peek(self):
        if self.length == 0:
            return 'Stack is empty'
        return self.top.data

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = self.top
            self.length += 1
        else:
            holding_node = self.top
            self.top = new_node
            self.top.next = holding_node
            self.length += 1


    def pop(self):
        if self.length == 0:
            return 'Stack is empty'

        popped_data = self.top.data
        self.top = self.top.next
        self.length -= 1

        if self.length == 0:
            self.bottom = None

        return popped_data



new_stack = Stack()
print(new_stack.push('Google'))
print(new_stack.push('Udemy'))
print(new_stack.push('Discord'))
print(new_stack.top)
print(new_stack.print_list())
print(new_stack.pop())
print(new_stack.print_list())
print(new_stack.pop())
print(new_stack.print_list())
print(new_stack.pop())
print(new_stack.print_list())