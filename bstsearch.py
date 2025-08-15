# binary tree search
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
def search_in_bst(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search_in_bst(root.left, key)
    else:
        return search_in_bst(root.right, key)
def insert_into_bst(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert_into_bst(root.left, key)
    else:
        root.right = insert_into_bst(root.right, key)
    return root
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.data] + inorder_traversal(root.right)
k = create_tree([1, 2, 3, 4, 5, 6, 7])
print("Inorder Traversal of BST:", inorder_traversal(k))
print("Search for 5 in BST:", search_in_bst(k, 5))
print("Search for 10 in BST:", search_in_bst(k, 10))
print("Insert 8 into BST")
k = insert_into_bst(k, 8)
print("Inorder Traversal after inserting 8:", inorder_traversal(k))


