
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
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
        holding_point = leader.next
        leader.next = new_node
        new_node.next = holding_point
        self.length += 1

    def remove(self, index):
        if index > self.length-1:
            return 'invalid index'
        leader = self.traverse_to_index(index-1)
        after = self.traverse_to_index(index+1)
        leader.next = after
        self.length -= 1

    # reverse the order of the singly linked list
    # If the list is empty or consists of 1 item only we return the list as it is.
    # Otherwise, we create two nodes first and second which point to the first and second nodes of the list respectively
    # Then we update the tail of the list to point to the head as after reversing the present head will become the last node
    # Then we run a loop until second becmes None
    # Inside the loop we create a temporary node which points to the 'next' of the second node
    # Then we update the 'next' of the second node to point to the first node so that the link is now reversed (2nd node points to 1st node instead of 3rd).
    # And then we will update the first and second nodes to be equal to the second and temporary nodes respectively.
    # What this does is, in the next iteration, 'second' will point to the 3rd node and 'first' to the 2nd
    # And the 'second.next = first' statement will make the 3rd node point to the 2nd node instead of the 4th.
    # And this will go on till 'second' becomes None and by then all the links will be reversed.
    # Finally, we will update the 'next' of the head(which is still the original head) point to None as it is effectively the last node
    # And then we will update the head to be equal to 'first', which by now points to the last node of the original list, and return the now reversed linked list
    # Time complexity pretty clearly will be O(n)
    def reverse(self):
        if self.length == 1:
            return self.print_list()
        first = self.head
        second = first.next
        self.tail = self.head
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first
        return self.print_list()


#[10, 1, 5, 17, 18, 19, 20, 21, 22]
myLinkedList = LinkedList()
myLinkedList.append(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(5)
myLinkedList.append(6)
myLinkedList.append(7)
print(myLinkedList.print_list())
print(myLinkedList.reverse())