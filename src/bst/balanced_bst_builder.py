# Node class for BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to insert a node into the BST
def bst_insert(root, value):
    if root is None:
        return Node(value)
    
    if value < root.value:
        root.left = bst_insert(root.left, value)
    else:
        root.right = bst_insert(root.right, value)
    
    return root

# Recursive function to generate a re-arranged sequence
def balanced_BST_seq(A, B):
    n = len(A)
    if n == 0:
        return B
    
    if n % 2 == 0:
        middle_index = n // 2
    else:
        middle_index = (n - 1) // 2

    B.append(A[middle_index])

    # Recursive call for the left half
    B = balanced_BST_seq(A[:middle_index], B)

    # Recursive call for the right half
    B = balanced_BST_seq(A[middle_index+1:], B)

    return B

# Function to build the balanced BST
def build_balanced_BST(A):
    A.sort()  # Sort the input array first
    B = []
    B = balanced_BST_seq(A, B)  # Generate the re-arranged sequence

    # Build the BST by inserting the elements sequentially
    BST = None
    for value in B:
        BST = bst_insert(BST, value)
        
    return B, BST

# Function to print the in-order traversal of the BST
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

# Function to print the shape of the tree (printTree function)
def printTree(root, element="value", left="left", right="right"):
    def display(root, element=element, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, element)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, element)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, element)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

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
    if root is not None:
        lines, *_ = display(root, element, left, right)

    print("\t== Binary Tree: shape ==")
    print()
    if not lines:
        print("\t  No tree found")
    for line in lines:
        print("\t", line)
    print()

# Main function to demonstrate the functionality
def main():
    A = [45, -8, 21, 34, 55, 65, 9, 14, 0, 18, 90, 46, 49, 82, 84, 99, 80, 132, 57, 66]
    mydataSet = [-12,45,-33,27,89,-56,14,-8,73,-19,61,-5,38,-22,7,50,93,-41,0,64]

    # Print the original data sequence
    print("\nDataset 1")
    print("Original Data Sequence:")
    print(A)

    # Build the balanced BST and get the re-arranged sequence
    rearranged_sequence, BST = build_balanced_BST(A)

    # Print the re-arranged data items
    print("\nRe-arranged Data Sequence (from balanced_BST_seq):")
    print(rearranged_sequence)

    # Print the tree shape
    
    printTree(BST)

    print("\n\nDataset 2")
    print("Original Data Sequence:")
    print(mydataSet)
    rearranged_sequence, BST = build_balanced_BST(mydataSet)
    print("\nRe-arranged Data Sequence (from balanced_BST_seq):")
    print(rearranged_sequence)
    printTree(BST)
    

# Call the main function to execute the program
if __name__ == "__main__":
    main()
