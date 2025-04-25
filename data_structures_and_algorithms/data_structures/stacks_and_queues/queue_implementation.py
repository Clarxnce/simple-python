class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        return str(self.print_list())

    def print_list(self):
        my_list = []
        current_node = self.first
        while current_node != None:
            my_list.append(current_node.data)
            current_node = current_node.next
        return my_list

    def peek(self):
        if self.length == 0:
            return 'Queue is empty'
        return self.first.data


    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = self.last = new_node
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
        return self


    def dequeue(self):
        if self.length == 0:
            return 'Queue is empty'
        self.first = self.first.next
        self.length -= 1

        if self.length == 0:
            self.last = None
        return self



new_queue = Queue()
print(new_queue.enqueue('Simon'))
print(new_queue.enqueue('Joan'))
print(new_queue.enqueue('Clarence'))
print(new_queue.print_list())
print(new_queue.dequeue())
print(new_queue.print_list())
print(new_queue.dequeue())
print(new_queue.print_list())
print(new_queue.dequeue())
print(new_queue.print_list())