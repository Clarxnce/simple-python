

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return str(self.__dict__)

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.root = new_node
            self.length += 1
        else:
            # keep comparing until new_node.value is less than current_node.value and current_node.left = None
            # or keep comparing until new_node.value is greater than current_node.value and current_node.right = None
            #need to set new_node to left or right of current node
            #split into less than and greater than
            current_node = self.root
            while True:
                if new_node.value < current_node.value:
                    #left
                    if not current_node.left:
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
                else:
                    #right
                    if not current_node.right:
                        current_node.right = new_node
                        return self
                    current_node = current_node.right



    def lookup(self, value):
        if self.length == 0:
            return 'Binary Search Tree is empty'
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif value == current_node.value:
                return current_node
        return False

    def remove(self, value):
        if not self.root:
            return False
        current_node = self.root
        parent_node = None
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif value == current_node.value:
                #Option 1: No right child
                if current_node.right is None:
                    if parent_node is None:
                        self.root = current_node.left
                    else:
                        #if parent > current value, make current left child a child of parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left
                        #if parent < current value, make left child a right child of parent
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.left
                #Option 2: Right child which doesn't have a left child
                elif current_node.right.left is None:
                    if parent_node is None:
                        self.root = current_node.left
                    else:
                        current_node.right.left = current_node.left
                    #if parent > current, make right child a left of the parent
                    if current_node.value < parent_node.value:
                        parent_node.left = current_node.right
                    #if parent < current, make right child a right child of the parent
                    elif current_node.value > parent_node.value:
                        parent_node.right = current_node.left
                #Option 3: Right child that has a left child
                else:
                    #find the Right child's left most child
                    leftmost = current_node.right.left
                    leftmost_parent = current_node.right
                    while leftmost.left is not None:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left
                    #Parent's left subtree is now leftmost's right subtree
                    leftmost_parent.left = leftmost.right
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right
                    if parent_node is None:
                        self.root = leftmost
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = leftmost
                        elif current_node.value > parent_node.value:
                            parent_node.right = leftmost
        return True

    def breadth_first_search(self):
        current_node = self.root
        result = []
        queue = [current_node]

        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result

    def bfs_recursive(self, queue, result):
        if not queue:
            return result
        current_node = queue.pop(0)
        result.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return self.bfs_recursive(queue, result)





bstree = BinarySearchTree()
bstree.insert(9)
bstree.insert(4)
bstree.insert(6)
bstree.insert(20)
bstree.insert(170)
bstree.insert(15)
bstree.insert(1)

print(bstree.breadth_first_search())
print(bstree.bfs_recursive([bstree.root], []))