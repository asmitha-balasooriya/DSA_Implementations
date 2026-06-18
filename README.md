# Data Structures & Algorithms Implementations

**Author**: Asmitha Darani Balasooriya
**Course**: Data Structures and Algorithms

A comprehensive collection of **Data Structures** and **Sorting Algorithms** implemented in Python, including advanced tree structures, application systems with menus, and detailed performance analysis.

---

## 📁 Projects Included

### 1. Balanced & Complete Binary Search Trees 
- Implemented algorithms to construct **Balanced BST** and **Complete BST** from an unsorted array.
- Recursive sequence generation + BST insertion.
- Time & Space complexity analysis (O(n) time for both).

### 2. Enhanced Binary Search Tree Operations
- Leaf & Non-leaf node identification
- Count nodes in subtree
- Depth of a node and subtree
- Node deletion with proper handling (0, 1, or 2 children)

### 3. BST & AVL Tree Application Systems 
- Interactive menu-driven applications for BST and AVL trees.
- Supports: Insert, Delete, Traversals (Pre/In/Post), Visualization, Balance/Complete conversion, Search, etc.
- AVL Tree with self-balancing on deletion.

### 4. Sorting Algorithms Analysis 
- Bubble Sort + Multiple Optimizations (Early termination, Reduced range, Combined improvements)
- Sink-Down Sort
- Bi-directional Bubble Sort (Cocktail Sort)
- Experimental performance study (comparisons & runtime) on arrays up to 2000 elements.

---

## 🛠 Tech Stack
- **Python 3**
- Object-Oriented Programming (Classes for Node, BST, AVL)
- Recursion & Iterative approaches
- matplotlib (for tree visualization)


FULL IMPLEMENTATION, ANALYSIS AND OUTPUT REPORTS ARE INCLUDED


---


## 📂 Repository Structure

```bash
.
├── outputs
│   ├── Experimental_Study_Output.txt
│   └── shell_output.txt
├── README.md
├── reports
│   ├── BST_AVL_Documentation.pdf
│   └── Sorting_Report.pdf
├── requirements.txt
└── src
    ├── avl
    │   └── AVL_tree.py
    ├── bst
    │   ├── balanced_bst_builder.py
    │   ├── bst_management_system.py
    │   └── complete_bst_builder.py
    └── sorting
        ├── Bidirectional_BubbleSort.py
        ├── BubbleSort.py
        ├── Experimental_Study_Code.py
        ├── main.py
        ├── Obs1_BubbleSort.py
        ├── Obs2_BubbleSort.py
        ├── Obs3_BubbleSort.py
        ├── SinkDownSort_Improved.py
        └── SinkDownSort.py
---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd DSA-Implementations

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run BST Application
python src/bst/bst_management_system.py

# 4. Run AVL Application
python src/avl/AVL_tree.py

# 5. Run Sorting Analysis
python src/sorting/main.py


