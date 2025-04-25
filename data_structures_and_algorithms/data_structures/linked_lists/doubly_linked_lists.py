
class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.length = None
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            current_tail = self.tail
            current_tail.next = new_node
            self.tail.previous = current_tail
            self.tail = new_node
            self.length += 1

    def prepend(self,data):
        new_node = Node(data)
        current_head = self.head
        new_node.next = current_head
        current_head.previous = new_node
        self.head = new_node
        self.length += 1


    def print_list(self):
        my_list = []
        current_node = self.head
        while current_node != None:
            my_list.append(current_node.data)
            current_node = current_node.next
        return my_list

    def traverse_to_index(self, index):
        i = 0
        current_node = self.head
        while i != index:
            current_node = current_node.next
            i += 1
        return current_node

    # create new node. new_node.next = node at current index. previous node.next now equals new_node
    def insert(self, index, data):
        if index >= self.length:
            return self.append(data)

        new_node = Node(data)
        leader = self.traverse_to_index(index-1)
        follower = leader.next
        leader.next = new_node
        new_node.previous = leader
        new_node.next = follower
        follower.previous = new_node
        self.length += 1

    def remove(self, index):
        if index > self.length-1:
            return 'invalid index'
        leader = self.traverse_to_index(index-1)
        follower = self.traverse_to_index(index+1)
        leader.next = follower
        follower.previous = leader
        self.length -= 1





#[10, 1, 5, 17, 18, 19, 20, 21, 22]
myLinkedList = DoublyLinkedList()
myLinkedList.append(1)
myLinkedList.append(5)
myLinkedList.prepend(10)
myLinkedList.append(17)
myLinkedList.append(18)
myLinkedList.append(19)
myLinkedList.append(20)
# myLinkedList.append(21)
# myLinkedList.append(22)
myLinkedList.insert(3,999)
# myLinkedList.remove(6)
# myLinkedList.remove(8)
print(myLinkedList.print_list())
