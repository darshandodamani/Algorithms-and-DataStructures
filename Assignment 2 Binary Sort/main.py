# Main function, which allows the user to interact with the BinarySearchTree
# In this main function we are interacting eith the methods defined in the BinarySearchTree
# THe user has a feasibility to select the different opeartion which he want to work on 
# The methods will be called from the BinarySearchTree and execute the results and printed in the console.
# After every operations like Insert, Delete requested to Print the tree to see the results in the tree.
# Requested Note: Save the file as {name}.dot in which please do mention end as .dot in the file you if you are printing the graph

from BinarySearchTree import BinarySearchTree

def main():
    bst = BinarySearchTree()
    values = [8, 3, 1, 10, 6, 4, 7, 14, 13]                         # Intial values for creating the tree Referred example from the lecture class PPT
    for value in values:
        bst.insert(value)                                           # insert operation will call the method from BinarySearchTree and create a tree

    bst.print_bst("tree.dot")

                # User feasibility to select the operatio he want to perform

    while True:
        print("****** Choose an option: ******")
        print("1. Insert Operation")
        print("2. Search Operation")
        print("3. Delete Operation")
        print("4. Find the minimum value Operation")
        print("5. Find the maximum value Operation")
        print("6. Successor Operation")
        print("7. Predecessor Operation")
        print("8. Print Tree")
        print("9. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            value = int(input("Vlaue you want to insert: "))
            bst.insert(value)                                           # insert method from BinarySearchTree
            print(f"Inserted {value} into the tree.")
            print(" \n ")
            print("**************************")
        elif choice == "2":
            value = int(input("Value you want to search in tree: "))
            if bst.search(value):                                       # delete method from BinarySearchTree
                print(f"{value} is in the tree.")
                print(" \n ")
            else:
                print(f"{value} is not in the tree.")
                print(" \n ")
                print("**************************")
        elif choice == "3":
            value = int(input("Value you want to delete: "))
            bst.delete(value)                                           # delete method from the BinarySearchTree is called
            print(f"Deleted {value} from the tree.")    
            print(" \n ")
            print("**************************")
        elif choice == "4":
            min_node = bst.min()                                        # min method from the BinarySearchTree is called
            if min_node:
                print(f"The minimum value in the tree is: {min_node.value}")
                print(" \n ")
                print("**************************")
            else:
                print("The tree is empty.")
                print(" \n ")
                print("**************************")
        elif choice == "5":
            max_node = bst.max()                                        # max method from the BinarySearchTree is called
            if max_node:
                print(f"The maximum value in the tree is: {max_node.value}")
                print(" \n ")
                print("**************************")
            else:
                print("The tree is empty.")
                print(" \n ")
                print("**************************")
        elif choice == "6":
            value = int(input("Enter a value to find its successor: "))
            successor_node = bst.successor(value)                       # successor method from the BinarySearchTree is called
            if successor_node:
                print(f"The successor of {value} is: {successor_node.value}")
                print(" \n ")
                print("**************************")
            else:
                print(f"No successor found for {value}.")
                print(" \n ")
                print("**************************")
        elif choice == "7":
            value = int(input("Enter a value to find its predecessor: "))
            predecessor_node = bst.predecessor(value)                   # predecessor method from the BinarySearchTree is called
            if predecessor_node:
                print(f"The predecessor of {value} is: {predecessor_node.value}")
                print(" \n ")
                print("**************************")
            else:
                print(f"No predecessor found for {value}.")
        elif choice == "8":
            filename = input("Enter a filename to save the tree as a graph: ")
            print(" \n ")
            print("**************************")
            bst.print_bst(filename)                                     # print_bst method from BinarySearchTree
            print(f"Saved the tree as {filename}.")
            print(" \n ")
            print("**************************")
        elif choice == "9":
            print("Exiting...")
            print(" \n ")
            print("**************************")
            break
        else:
            print("Invalid choice. Please try again.")
            print(" \n ")
            print("**************************")

if __name__ == "__main__":
    main()