import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

 #binary tree O(log n), always sorted or else tree isn't valid

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #if there is no node at root -> insert this as root

        #compare value to the root

        if value < self.value:
            #if value is smaller, look left and repeat steps
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                #if no node, make new one with this value
                return self.left.insert(value)
            
        #if value is larger or equal to -> look right and repeat 
        elif value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                #if no node, make new one with this value
                return self.right.insert(value)
            
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if no node at root -> return False

        if target == self.value:
            return True
        #compare value to root
        elif target < self.value:
            #if value is smaller, go left
            if self.left == None:
                return False
            #look at node there
            elif self.left.contains(target):
                return True

        #if bigger or ==, go right
        elif target >= self.value:
            if self.right == None:
                return False
            elif self.right.contains(target):
                return True

    # Return the maximum value found in the tree
    def get_max(self):
        #if no right child, return this value
        if self.right == None:
            return self.value
        #otherwise, go right
        else:
            return self.right.get_max()
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #call cb on the value of every node
        cb(self.value)

        #check if both aren't none
        if self.left is not None and self.right is not None:
            self.left.for_each(cb)
            self.right.for_each(cb)
        #check if right isn't none
        elif self.right is not None:
            self.right.for_each(cb)
        #check if left isn't none
        elif self.left is not None:
            self.left.for_each(cb)
        else: 
            return


    # DAY 2 Project -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     pass

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
