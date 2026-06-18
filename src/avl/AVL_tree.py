"""
Tests the AVL tree building algorithm
"""

        
#import random, math

outputdebug = True 

def debug(msg):
    if outputdebug:
        print (msg)

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 




class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0) 
    
    def insert(self, key):
        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            
        
        elif key < tree.key: 
            self.node.left.insert(key)
            
        elif key > tree.key: 
            self.node.right.insert(key)
        
        else: 
            debug(" Key [" + str(key) + "] already in tree.")
            
        self.rebalance() 

    
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


            
    def rrotate(self):
        # Rotate left pivoting on self
        
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
        
            
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 


    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 
    
    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        
    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 

    def display(self, level=0):
        '''
        Display the whole tree in a table-like format.
        '''
        self.update_heights()  # Must update heights before balances 
        self.update_balances()
        
        # Create headers for the table
        print(f"{'Level':<6} | {'Node':<6} | {'Height':<6} | {'Balance':<7} | {'Leaf':<5}")
        print("-" * 40)  # Line separator

        # Helper function for recursive display
        def recursive_display(node, level):
            if node is None or node.node is None:
                return

            # Print the current node's details
            print(f"{level:<6} | {node.node.key:<6} | {node.height:<6} | {node.balance:<7} | {'Yes' if node.is_leaf() else 'No':<5}")
            
            # Recursive calls for left and right children
            if node.node.left:
                recursive_display(node.node.left, level + 1)
            if node.node.right:
                recursive_display(node.node.right, level + 1)

        # Start recursive display from the root node
        if self.node:
            recursive_display(self, 0)
        else:
            print("Tree is empty.")




    def delete(self, key):
        """
        Delete a node with the given key from the AVL tree.
        """
        if self.node is None:
            return  # Key not found, nothing to delete
        
        
        if key < self.node.key:
            self.node.left.delete(key)
        elif key > self.node.key:
            self.node.right.delete(key)
        else:
            # Key found, now we need to delete this node
            if self.node.left.node is None and self.node.right.node is None:
                # Case 1: The node is a leaf
                self.node = None
            elif self.node.left.node is None:
                # Case 2: The node has only a right child
                self.node = self.node.right.node
            elif self.node.right.node is None:
                # Case 2: The node has only a left child
                self.node = self.node.left.node
            else:
                # Case 3: The node has two children
                # Find the in-order predecessor or successor
                successor = self.logical_successor(self.node)
                self.node.key = successor.key
                self.node.right.delete(successor.key)

        # Step 2: Update heights and rebalance the tree
        if self.node is not None:
            self.rebalance()

             
    def printTreeNoHB(self):            ##  https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
        def display(root):              ##  AUTHOR: Original: J.V.     Edit: BcK
            #   No child.
            if root.node.right.node is None and root.node.left.node is None:
                line = str(root.node.key) 
                
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            #   Only left child.
            if root.node.right.node is None:
                lines, n, p, x = display(root.node.left)
                nodeOutput = (str(root.node.key) )
                
                keyLength = len(nodeOutput)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + nodeOutput
                second_line = x * ' ' + '/' + (n - x - 1 + keyLength) * ' '
                shifted_lines = [line + keyLength * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + keyLength, p + 2, n + keyLength // 2

            #   Only right child.
            if root.node.left.node is None:
                lines, n, p, x = display(root.node.right)
                nodeOutput = str(root.node.key) 
                keyLength = len(nodeOutput)
                first_line = nodeOutput + x * '_' + (n - x) * ' '
                second_line = (keyLength + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [keyLength * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + keyLength, p + 2, keyLength // 2

            #   Two children.
            left, n, p, x = display(root.node.left)
            right, m, q, y = display(root.node.right)
            nodeOutput = str(root.node.key)
            
            keyLength = len(nodeOutput)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + nodeOutput + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + keyLength + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + keyLength * ' ' + b for a, b in zipped_lines]
            return lines, n + m + keyLength, max(p, q) + 2, n + keyLength // 2

        lines = []
        if self.node != None:
            lines, *_ = display(self)
            print("\t\t== AVL Tree ==")
            print()
        if lines == []:
            print("No tree found, please rebuild a new Tree.\n")
            return -1
        for line in lines:
            print(line)
        print()     




    def preorder_traverse(self):
        """
        Perform a pre-order traversal of the AVL tree.
        Return the nodes' keys in pre-order as a list.
        """
        if self.node is None:
            return []
        
        # Pre-order: root, left, right
        prelist = [self.node.key]
        prelist.extend(self.node.left.preorder_traverse())
        prelist.extend(self.node.right.preorder_traverse())
        
        return prelist
    
    def postorder_traverse(self):
        """
        Perform a post-order traversal of the AVL tree.
        Return the nodes' keys in post-order as a list.
        """
        if self.node is None:
            return []
        
        # Post-order: left, right, root
        postlist = []
        postlist.extend(self.node.left.postorder_traverse())
        postlist.extend(self.node.right.postorder_traverse())
        postlist.append(self.node.key)
        
        return postlist
    

    def avl_search(self, e):
        """
        Search for a node with value `e` in the AVL tree.
        Return True if the node exists, False otherwise.
        """
        current = self.node  # Start from the root node
        
        while current is not None:
            if e < current.key:
                current = current.left.node  # Move to left subtree
            elif e > current.key:
                current = current.right.node  # Move to right subtree
            else:
                return True  # Element is found
        
        return False  # Element is not found
    
    def depth_nodeAVL(self, e):
        """
        Calculate the depth of the node with value `e` in the AVL tree.
        Return the depth if found, or -1 if the node is not in the tree.
        """
        current = self.node  # Start from the root node
        depth = 0  # Depth starts at 0 (root level)
        
        while current is not None:
            if e < current.key:
                current = current.left.node  # Move to left subtree
                depth += 1  # Increase depth
            elif e > current.key:
                current = current.right.node  # Move to right subtree
                depth += 1  # Increase depth
            else:
                return depth  # Element is found, return its depth
        
        return -1  # Element is not in the tree

    def calculate_depth_statistics(self):
        """
        Scans the AVL tree and prints a statistic table of the number of nodes at each depth.
        """
        depth_count = {}  # Dictionary to store the count of nodes at each depth
        
        # Traverse the tree in order and calculate depths
        self._calculate_depths_helper(depth_count)
        
        # Sort depth levels and print the statistics table
        max_depth = max(depth_count.keys()) if depth_count else 0
        print("\nTable 1: The Statistic table (for nodes of different depths)")
        print("Depth of nodes | Number of nodes")
        print("--------------------------------")
        for depth in range(max_depth + 1):
            print(f"{depth:^15} | {depth_count.get(depth, 0):^15}")
    
    def _calculate_depths_helper(self, depth_count, current_depth=0):
        """
        Helper method to recursively calculate the depth of each node and update the count.
        """
        if self.node is None:
            return
        
        # Increase the count for the current depth
        if current_depth in depth_count:
            depth_count[current_depth] += 1
        else:
            depth_count[current_depth] = 1
        
        # Recursively calculate depths for left and right subtrees
        self.node.left._calculate_depths_helper(depth_count, current_depth + 1)
        self.node.right._calculate_depths_helper(depth_count, current_depth + 1)


    def get_leaf_nodes(self):
        """
        Collect and print all leaf nodes (nodes with no children).
        """
        leaves = self._get_leaf_nodes_helper()
        
        return leaves
    
    def _get_leaf_nodes_helper(self):
        """
        Helper method to recursively collect leaf nodes.
        """
        if self.node is None:
            return []
        
        if self.is_leaf():
            return [self.node.key]  # This is a leaf node
        
        leaves = []
        leaves.extend(self.node.left._get_leaf_nodes_helper())
        leaves.extend(self.node.right._get_leaf_nodes_helper())
        return leaves
    
    def get_non_leaf_nodes(self):
        """
        Collect and print all non-leaf nodes (nodes with at least one child).
        """
        non_leaves = self._get_non_leaf_nodes_helper()
        
        return non_leaves
    
    def _get_non_leaf_nodes_helper(self):
        """
        Helper method to recursively collect non-leaf nodes.
        """
        if self.node is None:
            return []
        
        if not self.is_leaf():
            non_leaves = [self.node.key]  # This is a non-leaf node
        else:
            non_leaves = []
        
        non_leaves.extend(self.node.left._get_non_leaf_nodes_helper())
        non_leaves.extend(self.node.right._get_non_leaf_nodes_helper())
        return non_leaves

    #inverse in-order traversal
    def inverse_inorder(self):
        self.inverse_inorderHelper(self.node)
    def inverse_inorderHelper(self, r):
        if r != None:
            
            self.inverse_inorderHelper(r.right.node)
            print(r.key, end = " ")
            self.inverse_inorderHelper(r.left.node)

def print_level2_menu():
    print("\n\nMENU-Level 2")
    print("\n1. Display the AVL tree, showing the height and balance factor for each node.")
    print("\n2. Print the pre-order, in-order, and post-order traversal sequences of the AVL tree.")
    print("\n3. Print all leaf nodes of the AVL tree, and all non-leaf nodes (separately)")
    print("\n4. Insert a new integer key into the AVL tree.")
    print("\n5. Delete an integer key from the AVL tree.")
    print("\n6. Display the statistic table of the AVL tree.")
    print("\n7. Return to the level-1 menu")

def task_handler(choice,myTree):
    if choice == 1:
        myTree.printTreeNoHB()
        print("\n\nThe Heights and the balance factors of each node in the AVL tree")
        print()
        myTree.display()

    elif choice == 2:
        print("\nPreorder traversal:")
        print(myTree.preorder_traverse())
        print("\n\nInorder traversal:")
        print(myTree.inorder_traverse())
        print("\n\nPostorder traversal:")
        print(myTree.postorder_traverse())

    elif choice == 3:
        print("\nLeaf Nodes")
        print(myTree.get_leaf_nodes())
        print("\n\nNon-Leaf Nodes")
        print(myTree.get_non_leaf_nodes())

    elif choice == 4:
        N = int(input("\nEnter an integer: "))
        if not myTree.avl_search(N):
            myTree.insert(N)
            print("\nInverse In-Order Traversal")
            myTree.inverse_inorder()
            print("\n\nInteger",N,"successfully inserted")
        else:
            print(f"ERROR: Node {N} already exists!")

    elif choice == 5:
        N = int(input("\nEnter an integer: "))
        if myTree.avl_search(N):
            myTree.delete(N)
            myTree.printTreeNoHB()
        else:
            print(f"ERROR: Node {N} not found!")

    elif choice == 6:
        myTree.calculate_depth_statistics()
    elif choice==7:
        print("\nLevel-2 Menu Exited")

def main():
    choice = 0

    while choice != 3:
        myTree = AVLTree()
        print("\n\nMENU-Level 1")
        print("\n1. Pre-load a sequence of integers to build AVL tree")
        print("\n2. Manually enter integer keys one by one to build an AVL tree")
        print("\n3. Exit")
        choice = input("\nEnter choice: ")
        if not (choice.lstrip('-').isdigit() or choice.isdigit()):
            print("\nOnly Integers are allowed")
            continue
        choice=int(choice)

        if choice == 1:
            myPreset = [63, 83, -27, 22, 44, 79, 33, 9, 3, 0, 101, 97, 47, 88, 57, 50, 51, 52, 48, 78, 94]
            for num in myPreset:
                myTree.insert(num)

            while choice!=7:    
                print_level2_menu()
                choice = input("\nEnter choice: ")
                if not (choice.lstrip('-').isdigit() or choice.isdigit()):
                    print("\nOnly Integers are allowed")
                    continue
                choice=int(choice)
                task_handler(choice,myTree)
            

        elif choice==2:
            print("\nType 'exit' to stop entering numbers")
            while True:
                num = input("\nEnter num: ")
                
                # Check if the input is "exit" to break the loop
                if num.lower() == "exit":
                    break
                
                # Check if the input is a valid integer
                if not num.lstrip('-').isdigit():
                    print("\nOnly Integers are allowed")
                    continue
                
                num = int(num)  # Convert the input to an integer
                
                # Check if the number is already present in the BST
                isPresent = myTree.avl_search(num)
                if isPresent ==True:
                    print(f"\n{num} is already present in the BST.")
                else:
                    myTree.insert(num)

            while choice!=7:    
                print_level2_menu()
                choice = input("\nEnter choice: ")
                if not (choice.lstrip('-').isdigit() or choice.isdigit()):
                    print("\nOnly Integers are allowed")
                    continue
                choice=int(choice)
                task_handler(choice,myTree)

        elif choice==3:
            print("\nProgram Terminated")

if __name__ == "__main__":
    main() 
