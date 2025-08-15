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
def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.data, end=' ')
    print_tree(root.right)
def sum_of_tree(root):
    if root is None:
        return 0
    return root.data + sum_of_tree(root.left) + sum_of_tree(root.right)
# find the k th element in the tree
def find_kth_element(root, k):
    stack = []
    current = root
    count = 0
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        count += 1
        if count == k:
            return current.data
        current = current.right
    return None

k=create_tree([1, 2, 3, 4, 5, 6, 7])
res = sum_of_tree(k)
print(res) 
i = print_tree(k)
print()
print(find_kth_element(k, 6)) 
