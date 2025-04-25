

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

    def dfs_in_order(self):
        return traverse_in_order(self.root, [])

    def dfs_post_order(self):
        return traverse_post_order(self.root, [])

    def dfs_pre_order(self):
        return traverse_pre_order(self.root, [])


def traverse_in_order(node, arr):
    if node.left:
        traverse_in_order(node.left, arr)
    arr.append(node.value)
    if node.right:
        traverse_in_order(node.right, arr)
    return arr

def traverse_pre_order(node, arr):
    arr.append(node.value)
    if node.left:
        traverse_pre_order(node.left, arr)
    if node.right:
        traverse_pre_order(node.right, arr)
    return arr

def traverse_post_order(node, arr):
    if node.left:
        traverse_post_order(node.left, arr)
    if node.right:
        traverse_post_order(node.right, arr)
    arr.append(node.value)
    return arr



bstree = BinarySearchTree()
bstree.insert(9)
bstree.insert(4)
bstree.insert(6)
bstree.insert(20)
bstree.insert(170)
bstree.insert(15)
bstree.insert(1)

print(bstree.dfs_in_order())
print(bstree.dfs_pre_order())
print(bstree.dfs_post_order())

