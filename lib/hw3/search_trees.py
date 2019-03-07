
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

    def insert(self, data):
        if self.val == data:
            return False
        elif self.val < data:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = BST_Node(data)
                return True
        else:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = BST_Node(data)
                return True

    def find(self, data):
        if self.val == data:
            return True
        elif self.val > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.left.find(data)
            else:
                return False




class BST:
    def __init__(self):
        self.root = None

    def init_bst(self, val):
        self.root = BST_Node(val)

    def insert(self, val):
        if self.root is None:
            self.init_bst(val)
        else:
            self.insert(self.root.val)

    def insertNode(self, current, val):
        if current.val > val:
            if current.left is None:
                current.left = BST_Node(val)
            else:
                self.insertNode(current.left, val)
        if val > current.val:
            if current.right is None:
                current.right = BST_Node(val)
            else:
                self.insertNode(current.right,val)
        return False

    def bsearch(self, val):
        if self.root is not None:
            return self.searchNode(self.root, val)
        else:
            return False

    def searchNode(self, current, val):
        if val == current.val:
            return True

        return False

    def delete(self, val):
        if self.root is None:
            return self.root
        if val < self.root.val:
            self.root.left = self.delete(val)
        elif val > self.root.val:
            self.root.right = self.delete(val)
        else:
            if self.root.left is None:
                temp = self.root.right
                self.root = None
                return temp
            elif self.root.right is None:
                temp = self.root.left
                self.root = None
                return temp

        return self.root


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



        return False

    def rotate_left(self, current):



        return False

    def rotate_right(self, current):

        return False

    def flip_colors(self, current):

        return False

    def insert(self, val):
        if (self.root is None):
            self.init_rbbst(val, RED)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):




        return False

    def bsearch(self, val):

        return False

    def searchNode(self, current, val):

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