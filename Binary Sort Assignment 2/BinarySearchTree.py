from graphviz import Digraph

# Node class, which represents a node in the BinarySearchTree
class Node:
    #Constructor initilizing the attribute of the object
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BinarySearchTree class, which represents the BinarySearchTree
class BinarySearchTree:
    #the constructor of the class 
    def __init__(self):
        self.root = None

# --------------INSERT--------------
# From lecture Notes
# For adding a node x,it is necessary to find it a suitable place in the Tree w.r.t.the property of a BST.
# Thus,it is required to check if the Tree is empty, in that case the new node becomes the Root, otherwise the Tree is searched for finding a place
# for the new node in this way: for every encounteed node y of the Tree , if x.key < y.key then x will be inserted at the left of y ; otherwise it will be added to its right sub-tree.
# The insert method allows you to insert a new value into the binary search tree. It takes a value as input and does not return anything (None).
    def insert(self, value):
             
        if not self.root:                                   # if the tree is empty assign new value to root
            self.root = Node(value)
            return
        
        current = self.root                                 
        while True:
            if value < current.value:                       
                if not current.left:                        # if there is no left child insert here
                    current.left = Node(value)
                    return
                current = current.left                      # Move to the left child and continue the search
            else:                                            
                if not current.right:
                    current.right = Node(value)             # if there is no right child insert here
                    return
                current = current.right


# --------------SEARCH--------------
    # Search a value into the BinarySearchTree
    ##
    # Search, that returns either a pointer to the node that has a given key value or NIL if the Tree doesn’t contain such a node
    # value - The value we need to search for
    ##

    def search(self, value):
        current = self.root                                 # Search from the root node
        while current:
            if value == current.value:                      # if value is equal to current_node value search is done here
                return True 
            elif value < current.value:                     # if it is not the current_node value, then if it smaller
                current = current.left                      
            else:
                current = current.right                     # else moved to right and search is done here
        return False


# --------------DELETE--------------
    ##
    # If x is a leaf, we simply have to substitute it with NIL as its parent child and set x.parent as NIL, as well.
    # If x has only one child, we have to substitute x with it in the tree, clearing then the parent and children attributes of x.
    # If x has two children and its right child y = x.r doesn’t have a left child y.l == NIL, x can be substituted with y, the left sub-tree of x
    # becomes the new left sub-tree of x and everything else remains unchanged. Finally, if the right child of x has both children and x.r also has both children, we have to find the Successor z of x (which cannot have
    # a left child), then we have to make y(= x.r) the right child of z, attaching z.r and its descendants to the sub-tree rooted in y (i.e.
    # deleting z from the Tree), and, finally, substitute x with z in the Tree, which now sees the former parent, left and right child of x be now
    # z.p, z.l, z.r respectively, while the former z.r is now attached to the left sub-tree of y.
    ##

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:                                    
            return node

        if value < node.value:                              
            node.left = self._delete(node.left, value)      
        elif value > node.value:                            
            node.right = self._delete(node.right, value)    
        else:
            if node.left is None:                           
                return node.right                           
            elif node.right is None:                       
                return node.left                            
            else:
                successor = self._find_min(node.right)      
                node.value = successor.value               
                node.right = self._delete(node.right, successor.value)  

        return node
    # Note: All the conditions are met as per the statemnts above
    

    def min(self):
        if self.root:
            return self._find_min(self.root)

    # it will find the minimum value in the tree. The minimum values are always in the left of the tree
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
    
    def max(self):
        if self.root:
            return self._find_max(self.root)
        
    # it will find the maximun value in the tree. The maximum values are always in the right of the tree
    def _find_max(self, node):
        while node.right:
            node = node.right
        return node

    # predecessor will find the maximum smaller key in the Tree
    # Predecessor of a node x returns the node with the maximum smaller key in the Tree (NIL if x is the minimum
    # node). The predecessor of x is defined as the Maximum(x.left) if x.left 6= NIL or as the first ancestor reached from its right sub-tree.
    def predecessor(self, value):
        node = self.search(value)
        if node:
            return self._find_predecessor(node)
        
    def _find_predecessor(self, node):
        if node.left:
            return self._find_max(node.left)
        parent = node.parent
        while parent and node == parent.left:
            node = parent
            parent = parent.parent
        return parent

    # successor will find the minimum bigger key in the Treee ins the  tree
    # Successor (complexity O(h)) of a node x returns the node with the minimum bigger key in the Tree (NIL if x is the maximum node).
    # The successor of x is defined as the Minimum(x.right) if x.right 6= NIL or as the first ancestor reached from its left sub-tree.

    def successor(self, value):
        node = self.search(value)
        if node:
            return self._find_successor(node)

    def _find_successor(self, node):
        if node.right:
            return self._find_min(node.right)
        else:
            current = node
            while current.parent and current == current.parent.right:
                current = current.parent
            return current.parent

    def predecessor(self, node, file):
        if node:
            file.write(f"{node.value};\n")
            if node.left:
                file.write(f"{node.value} -> {node.left.value};\n")
                self.predecessor(node.left, file)
            if node.right:
                file.write(f"{node.value} -> {node.right.value};\n")
                self.predecessor(node.right, file)

    # the print_bst method generates the Graphiz representation of the binary search tree. I have a Graphiz as a extension in the vs code
    # which made me to easy to display the .dot format file saves by the print_bst method. Intially it opens, Here it calls teh predecessor method
    # adding left node, right node to the edge of the node is functioned by the predecessor method. 
    def print_bst(self, filename):
        with open(filename, "w") as file:
            file.write("digraph {\n")
            if not self.root:
                file.write("}\n")
                return
            self.predecessor(self.root, file)
            file.write("}\n")