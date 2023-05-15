import graphviz

# Define the Node class, which represents a node in the BinarySearchTree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Define the BinarySearchTree class, which represents the BinarySearchTree


class BinarySearchTree:
    def __init__(self):
        self.root = None

# --------------INSERT--------------
# For adding a node x,it is necessary to find it a suitable placeinthe Tree w.r.t.the property of a BST.
# Thus,it is required to check if the Tree is empty, in that case the new
# node becomes the Root, otherwise the Tree is searched for finding a place
# for the new node in this way: for every encounteed node y of the Tree , if
# x.key < y.key then x will be inserted at the left of y ; otherwise it will be added to its right sub-tree.

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = Node(value)
                    return
                current = current.right

    # Search a value into the BinarySearchTree
    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

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

    # Perform a preorder traversal of the BST and print the nodes to a file

    def predecessor(self, node, file):
        if node:
            file.write(f"{node.value};\n")
            if node.left:
                file.write(f"{node.value} -> {node.left.value};\n")
                self.predecessor(node.left, file)
            if node.right:
                file.write(f"{node.value} -> {node.right.value};\n")
                self.predecessor(node.right, file)

    # Print the BST as a graph in DOT format

    def print_bst(self, filename):
        with open(filename, "w") as file:
            file.write("digraph {\n")
            if not self.root:
                file.write("}\n")
                return
            self.predecessor(self.root, file)
            file.write("}\n")

    def display(self):
        dot = Digraph(comment='Binary Search Tree')
        self.__display_helper(dot, self.root)
        dot.render('bst', view=False, format='png')
        dot.render('bst', view=True)


# Define the main function, which allows the user to interact with the BST


def main():
    bst = BinarySearchTree()
    values = [8, 3, 1, 10, 6, 4, 7, 14, 13]
    for value in values:
        bst.insert(value)

    bst.print_bst("tree.dot")

    while True:
        print("Choose an option:")
        print("1. Insert a value")
        print("2. Search for a value")
        print("3. Delete a value")
        print("4. Print the tree")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            value = int(input("Enter a value to insert: "))
            bst.insert(value)
            print(f"Inserted {value} into the tree.")
        elif choice == "2":
            value = int(input("Enter a value to search: "))
            if bst.search(value):
                print(f"{value} is in the tree.")
            else:
                print(f"{value} is not in the tree.")
        elif choice == "3":
            value = int(input("Enter a value to delete: "))
            bst.delete(value)
            print(f"Deleted {value} from the tree.")

        elif choice == "4":
            filename = input("Enter a filename to save the tree as a graph: ")
            bst.print_bst(filename)
            print(f"Saved the tree as {filename}.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
