# From: 
# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# Python program to demonstrate insert operation in binary search tree  
  
# A utility class that represents an individual node in a BST 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
# A utility function to insert a new node with the given key 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 