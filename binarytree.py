# inorder ,postorder, preorder in binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def create_tree(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = create_tree(arr[:mid])
    root.right = create_tree(arr[mid + 1:])
    return root
def print_tree_inorder(root):
    if root is None:
        return
    print_tree_inorder(root.left)
    print(root.data, end=' ')
    print_tree_inorder(root.right)
# expalin inorder
# Inorder traversal of a binary tree visits the left subtree first, then the root node, and finally the right subtree.
# This results in the nodes being visited in non-decreasing order for a binary search tree.

def print_tree_preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    print_tree_preorder(root.left)
    print_tree_preorder(root.right)
# Preorder traversal of a binary tree visits the root node first, then the left subtree, and finally the right subtree.
# This is useful for creating a copy of the tree or for serialization.
def print_tree_postorder(root):
    if root is None:
        return
    print_tree_postorder(root.left)
    print_tree_postorder(root.right)
    print(root.data, end=' ')
# Postorder traversal of a binary tree visits the left subtree first, then the right subtree, and finally the root node.
# This is useful for deleting a tree or evaluating expressions in expression trees.
def sum_of_tree(root):
    if root is None:
        return 0
    return root.data + sum_of_tree(root.left) + sum_of_tree(root.right)
def find_largest_element(root):
    if root is None: 
        return float('-inf')
    left_max = find_largest_element(root.left)
    right_max = find_largest_element(root.right)
    return max(root.data, left_max, right_max)
# leetcode 100 same tree
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.data == q.data and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right))
# leetcode 226 invert binary tree
def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
