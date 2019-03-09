
import time
import random


class Array_Search:
    def __init__(self, array):
        self.array = array

    def init_array_search(self, val_array):
        self.array = Array_Search(val_array)

    def squential_search(self, key):
        idx = 0
        for num in self.array:
            if num == key:
                return idx
            idx = idx+1
        return False

    def bsearch(self, val):
        list.sort(self.array)
        low = 0
        high = len(self.array) - 1
        while low <= high:
            mid = low + ((high - low)//2)
            if self.array[mid] > val:
                high = mid - 1
            elif self.array[mid] < val:
                low = mid + 1
            else:
                return mid      #found
        return False            #not found


class BST_Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None



class BST:
    def __init__(self):
        self.root = None

    def init_bst(self, val):
        self.root = BST_Node(val)

    def insert(self, val):
        if self.root is None:
            self.init_bst(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):
        if current.val > val:
            if current.left is None:
                current.left = BST_Node(val)
                current.left.parent = current
            else:
                self.insertNode(current.left, val)
        if val > current.val:
            if current.right is None:
                current.right = BST_Node(val)
                current.right.parent = current
            else:
                self.insertNode(current.right, val)
        return False

    def bsearch(self, val):
        if self.root is not None:
            return self.searchNode(self.root, val)
        else:
            return False

    def searchNode(self, current, val):
        if val == current.val:
            return True
        elif val < current.val and current.left is not None:
            return self.searchNode(current.left, val)
        elif val > current.val and current.right is not None:
            return self.searchNode(current.right, val)
        return False

    def find(self, val):
        if self.root is not None:
            return self.findNode(self.root, val)
        else:
            return None

    def findNode(self, current, val):
        if val == current.val:
            return current
        elif val < current.val and current.left is not None:
            return self.findNode(current.left, val)
        elif val > current.val and current.right is not None:
            return self.findNode(current.right, val)

    def delete(self, val):
        return self.deleteNode(self.find(val))

    def deleteNode(self, node):

        # returns the node with the min value in the tree rooted at input node
        def min_val_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current
        # returns the num of children for a node
        def num_children(n):
            num_children = 0
            if n.left is not None:
                num_children += 1
            if n.right is not None:
                num_children += 1
            return num_children

        node_parent = node.parent
        node_children = num_children(node)

        # First case where the node does not have any children
        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None

        # Second case where the node has one child
        if node_children == 1:

            # finds the child node
            if node.left is not None:
                child = node.left
            else:
                child = node.right

            # replaces the node being deleted with its child
            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child

            # corrects the parent pointer
            child.parent = node_parent

        # Third case where the node has two children
        if node_children == 2:

            # the successor(in order) to the node being deleted
            next = min_val_node(node.right)

            # replaces value of the node being deleted with the successor's val
            node.val = next.val

            # deletes the successor node now that the value was copied
            self.deleteNode(next)


class RBBST_Node:
    def __init__(self, val, color):
        self.val = val
        self.left = None
        self.right = None
        self.color = color


RED = True
BLACK = False


class RBBST:
    def __init__(self):
        self.root = None

    def init_rbbst(self, val, color):
        self.root = RBBST_Node(val, color)

    def is_red(self, current):
        if current is not None:
            return current.color
        else:
            return False

    def rotate_left(self, current):
        if self.root is not None:
            self.is_red(current.right)
            temp = current.right
            current.right = temp.left
            temp.left = current
            temp.color = current.color
            current.color = RED
            return temp
        else:
            return False

    def rotate_right(self, current):
        if self.root is not None:
            self.is_red(current.left)
            temp = current.left
            current.left = temp.right
            temp.right = current
            temp.color = current.color
            current.color = RED
            return temp
        else:
            return False

    def flip_colors(self, current):
        if self.is_red(current) is False and self.is_red(current.left) is True and self.is_red(current) is True:
            current.color = RED
            current.left.color = BLACK
            current.right.color = BLACK
        else:
            return False

    def insert(self, val):
        if self.root is None:
            self.init_rbbst(val, RED)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):
        if current is None:
            return RBBST_Node(val, RED)
        diff = current.val - current.key
        if diff < 0:
            current.left = self.insertNode(current.left, )




        return False

    def bsearch(self, val):
        if self.root is not None:
            return self.searchNode(self.root, val)
        else:
            return False

    def searchNode(self, current, val):
        while current is not None:
            return RBBST_Node(val, RED)
        return False

if __name__ == "__main__":


    set_sz = 10
    tut = BST()

    vals = random.sample(range(1, 100), set_sz)

    for idx in range(set_sz - 1):

        tut.insert(vals[idx])

    print (tut.bsearch(vals[1]))
    print(tut.bsearch(11))

    tut_rb = RBBST()

    for idx in range(set_sz - 1):

        tut_rb.insert(vals[idx])

    print (tut.bsearch(vals[1]))
    print(tut.bsearch(11))