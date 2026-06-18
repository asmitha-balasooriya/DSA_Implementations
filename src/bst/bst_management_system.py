"""code from Pearson Education, Inc p104 """

def printTree(root, element="element", left="left", right="right"):                                 ##  https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display(root, element=element, left=left, right=right):                                     ##  AUTHOR: Original: J.V.     Edit: BcK
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, element)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, element)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, element)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, element)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
    lines = []
    if root != None:
        lines, *_ = display(root, element, left, right)
    print("\t== Binary Tree: shape ==")
    print()
    if lines == []:
        print("\t  No tree found")
    for line in lines:
        print("\t", line)
    print()



class BST:
    def __init__(self):
        self.root = None  # point to the root of a BST (or binary tree)
        self.size = 0

    # Return True if the element is in the tree
    def search(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return current # Element is found

        return False

    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
          self.root = self.createNewNode(e) # Create a new root
        else:
          # Locate the parent node
          parent = None
          current = self.root
          while current != None:
            if e < current.element:
              parent = current
              current = current.left
            elif e > current.element:
              parent = current
              current = current.right
            else:
              return False # Duplicate node not inserted

          # Create the new node and attach it to the parent node
          if e < parent.element:
            parent.left = self.createNewNode(e)
          else:
            parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
        return TreeNode(e)
    """
    # Return the size of the tree
    def getSize(self):
      return self.size"""

    # Inorder traversal from the root
    def inorder(self):
        sortedList=[]
        self.inorderHelper(self.root,sortedList)
        return sortedList
        

    # Inorder traversal from a subtree
    def inorderHelper(self, r,sortedList):
        if r != None:
            self.inorderHelper(r.left,sortedList)
            sortedList.append(r.element)
            self.inorderHelper(r.right,sortedList)
        
        
        
        
    #inverse in-order traversal
    def inverse_inorder(self):
        self.inverse_inorderHelper(self.root)
    def inverse_inorderHelper(self, r):
        if r != None:
            self.inverse_inorderHelper(r.right)
            print(r.element, end = " ")
            self.inverse_inorderHelper(r.left)
        
    #Method to print all the leaf nodes 
    def leaf_BST(self):
        self.leaf_BST_Helper(self.root)

    def leaf_BST_Helper(self,node):
        if node:
            if node.left is None and node.right is None:
                print(node.element, end=" ")  # This is a leaf node
            else:
                self.leaf_BST_Helper(node.left)
                self.leaf_BST_Helper(node.right)

    # Method to print the non-leaf nodes
    def non_leaf_BST(self):
        self.non_Leaf_BST_Helper(self.root)

    def non_Leaf_BST_Helper(self, node):
        if node:
            if node.left or node.right:
                print(node.element, end=" ")  # This is a non-leaf node
            self.non_Leaf_BST_Helper(node.left)
            self.non_Leaf_BST_Helper(node.right)
    

    # Postorder traversal from the root
    def postorder(self):
      self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
      if root != None:
        self.postorderHelper(root.left)
        self.postorderHelper(root.right)
        print(root.element, end = " ")

    # Preorder traversal from the root
    def preorder(self):
      self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
      if root != None:
        print(root.element, end = " ")
        self.preorderHelper(root.left)
        self.preorderHelper(root.right)

    # Return the total number of nodes in the sub-tree rooted at N
    def total_nodesBST(self, node):
        if node is None:
            return 0
        print(node.element, end=" ")  # Print the current node's element (pre-order style)
        left_count = self.total_nodesBST(node.left)   # Count nodes in the left subtree
        right_count = self.total_nodesBST(node.right) # Count nodes in the right subtree
        return 1 + left_count + right_count  # Add 1 for the current node and return total

    # Method to calculate depth of node N
    def depth_nodeBST(self, element):
        depth = 0
        current = self.root  # Start from the root

        while current is not None:
            print(f"Visiting node: {current.element}, Current Depth: {depth}")  # Add this line
            if element < current.element:
                current = current.left
                depth += 1
            elif element > current.element:
                current = current.right
                depth += 1
            else:
                print(f"Node found: {current.element}, Depth: {depth}")  # Add this line
                return depth  # Element found, return depth
        
        print(f"Element {element} not found in the tree")  # Add this line
        return -1  # If element is not found in the tree


    

    # Method to calculate the depth of the subtree rooted at node N
    def depth_subtreeBST(self, node):
        if node is None:
            return -1  # Depth of an empty tree is -1

        # Recursively calculate the depth of the left and right subtrees
        left_depth = self.depth_subtreeBST(node.left)
        right_depth = self.depth_subtreeBST(node.right)

        # The depth of the current subtree is the maximum depth of the left and right subtrees plus 1
        return max(left_depth, right_depth) + 1

    
    # Return true if the tree is empty
    def isEmpty(self):
      return self.size == 0

    # Remove all elements from the tree
    def clear(self):
      self.root == None
      self.size == 0

    # Return the root of the tree
    def getRoot(self):
      return self.root

    #Method to delete a node
    def delete_(self,key):
        self.root=self.delete_helper(self.root,key)

    #Helper method to delete a node
    def delete_helper(self,node,key):
        if node is None:
            return node #If the node is not found, none is returned

        #searching a node to delete
        if key<node.element:
            node.left=self.delete_helper(node.left,key)
        elif key>node.element:
            node.right=self.delete_helper(node.right,key)
        else:
            #handling a leaf node
            if node.left is None and node.right is None:
                node=None

            #handling a node with one child
            elif node.left is None:
                node=node.right
            elif node.right is None:
                node=node.left

            #handling a node with two children
            else:
                in_order_successor=self.minNodeHelper(node.right)
                node.element = in_order_successor.element
                node.right=self.delete_helper(node.right,in_order_successor.element)
        return node

    #helper method to find the minimum value node (in_order_successor)
    def minNodeHelper(self,node):
        current=node
        while current.left is not None:
            current = current.left
        return current


        # Function to insert a node into the BST
    def bst_insert(self,root, value):
        if root is None:
            return TreeNode(value)
        
        if value < root.element:
            root.left = self.bst_insert(root.left, value)
        else:
            root.right = self.bst_insert(root.right, value)
        
        return root

    # Recursive function to generate a re-arranged sequence
    def balanced_BST_seq(self,A, B):
        n = len(A)
        if n == 0:
            return B
        
        if n % 2 == 0:
            middle_index = n // 2
        else:
            middle_index = (n - 1) // 2

        B.append(A[middle_index])

        # Recursive call for the left half
        B = self.balanced_BST_seq(A[:middle_index], B)

        # Recursive call for the right half
        B = self.balanced_BST_seq(A[middle_index+1:], B)

        return B

    # Function to build the balanced BST
    def build_balanced_BST(self,A):
        
        A=A.inorder()  # Sort the input array first
        
        B = []
        B = self.balanced_BST_seq(A, B)  # Generate the re-arranged sequence

        # Build the BST by inserting the elements sequentially
        BST = None
        for value in B:
            BST = self.bst_insert(BST, value)
            
        return B, BST

    # Function to calculate the root index for a complete BST
    def calculate_root_index(self,A):
        n = len(A)
        if n == 1:
            return 0
        
        height = (n + 1).bit_length() - 1  # Calculate the height of the tree
        max_last_level = 2 ** (height - 1)  # Max number of nodes in the last level
        left_nodes = min(max_last_level, n - (2 ** height - 1))  # Nodes in the left subtree

        return left_nodes + (2 ** (height - 1) - 1)

    # Recursive function to generate a sequence for a complete BST
    def complete_BST_seq(self,A, B):
        n = len(A)
        if n == 0:
            return B

        root_index = self.calculate_root_index(A)
        B.append(A[root_index])

        # Recursive call for the left half
        B = self.complete_BST_seq(A[:root_index], B)

        # Recursive call for the right half
        B = self.complete_BST_seq(A[root_index+1:], B)

        return B

    # Function to build the complete BST
    def build_complete_BST(self,A):
        A=A.inorder()  # Sort the input array first
        B = []
        B = self.complete_BST_seq(A, B)  # Generate the re-arranged sequence for a complete BST

        # Build the BST by inserting the elements sequentially
        BST = None
        for value in B:
            BST = self.bst_insert(BST, value)
            
        return B, BST


class TreeNode:
    def __init__(self, e):
      self.element = e
      self.left = None # Point to the left node, default None
      self.right = None # Point to the right node, default None

    ####################### Main test binary tree


def print_level2_menu():
    print("\n\nMENU-Level 2")
    print("\n1. Display the tree shape of current BST, and then display the pre-order, in-order and post-order traversal sequences of the BST")
    print("\n2. Display all leaf nodes of the BST, and all non-leaf nodes (separately)")
    print("\n3. Display a subtree of the BST and count the number of nodes of the subtree")
    print("\n4. Display the depth of a given node in the BST")
    print("\n5. Display the depth of a subtree of the BST")
    print("\n6. Insert a new integer key into the BST")
    print("\n7. Delete an integer key from the BST")
    print("\n8. Convert the current BST to a balanced BST")
    print("\n9. Convert the current BST to a complete BST")
    print("\n10. Return to the level-1 menu")

def task_handler(choice,myTree):
    if choice==1:
        print("\nCurrent BST")
        printTree(myTree.getRoot())
        print("\nPreorder traversal:")
        myTree.preorder()
        print("\n\nInorder traversal:")
        sortedList=myTree.inorder()
        for i in sortedList:
            print(i, end = " ")
        print("\n\nPostorder traversal:")
        myTree.postorder()
        
    elif choice==2:
        print("\nLeaf Nodes")
        myTree.leaf_BST()
        print("\n\nNon-Leaf Nodes")
        myTree.non_leaf_BST()
        
    elif choice==3:
        N=int(input("\nEnter an integer: "))
        found=myTree.search(N)
        if found!=False:
            
            printTree(found)
            num=myTree.total_nodesBST(found)
            print("\nTotal Number of nodes in the sub tree is ",num)
        else:
            print("ERROR: Node ",N," not found!")

    elif choice==4:
        N=int(input("\nEnter an integer: "))
        found=myTree.search(N)
        if found!=False:
            
            num=myTree.depth_nodeBST(N)
            print("\nThe depth of the node ",N, " is ",num)
        else:
            print("ERROR: Node ", N," not found!")

    elif choice==5:
        N=int(input("\nEnter an integer: "))
        found=myTree.search(N)
        if found!=False:
            
            num=myTree.depth_subtreeBST(found)
            print("\nThe depth of the sub tree rooted at ",N, " is ",num)
        else:
            print("ERROR: Subtree rooted at node ", N," not found!")

    if choice==6:
        N=int(input("\nEnter an integer: "))
        found=myTree.search(N)
        if found==False:
            inserted=myTree.insert(N)
            
            if inserted==True:
                print("\nInverse In-Order Traversal")
                myTree.inverse_inorder()
                print("\n\nInteger",N,"successfully inserted")
            else:
                print("\nAn error occured while inserting")
        else:
            print("ERROR: Node Key", N,"already exists in the BST!")
    elif choice==7:
        N=int(input("\nEnter an integer: "))
        found=myTree.search(N)
        if found!=False:
            myTree.delete_(N)
            printTree(myTree.getRoot())
            print("\nNode",N,"is deleted")
            
        else:
            print("ERROR: Node ", N," not found!")
    elif choice==8:
        print("Original Data Sequence (in pre-order):")
        myTree.preorder()
        rearranged_sequence, BST=myTree.build_balanced_BST(myTree)
        print("\nRe-arranged Data Sequence")
        print(rearranged_sequence)
        print()
        printTree(BST)
        
    elif choice==9:
        print("Original Data Sequence(in pre-order):")
        myTree.preorder()
        rearranged_sequence, BST=myTree.build_complete_BST(myTree)
        print("\n\nRe-arranged Data Sequence:")
        print(rearranged_sequence)
        print()
        printTree(BST)
    
    elif choice==10:
        print("\nLevel-2 Menu Exited")
        
    
def main(size = 7):

    choice=0

    while choice != 3:

        myTree = BST()
        
        print("\n\nMENU-Level 1")
        print("\n1. Load a preset sequence of integers to build a BST")
        print("\n2. Manually enter integer keys one by one to build a BST")
        print("\n3. Exit")

        
        choice = input("\nEnter choice: ")
        if not (choice.lstrip('-').isdigit() or choice.isdigit()):
            print("\nOnly Integers are allowed")
            continue
        choice=int(choice)

        if choice==1:
            myPreset=[60, 86, 70, 25, 40, 84, 28, 19, 26, 108, 97, 50, 90, 56, 52, 53, 55, 51, -4, -44]
            for num in myPreset:
                myTree.insert(num)

            while choice!=10:    
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
                isPresent = myTree.search(num)
                if isPresent != False:
                    print(f"\n{num} is already present in the BST.")
                else:
                    myTree.insert(num)
                    


            while choice!=10:    
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
