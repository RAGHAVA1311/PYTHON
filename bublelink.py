class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubble_sort_linked_list(head):
    if head is None:
        return None

    swapped = True
    while swapped:
        swapped = False
        current = head

        while current.next:
            if current.data > current.next.data:
                # Swap data
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next
    return head


# Helper function to create linked list from list
def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

# Dynamic input
arr = list(map(int, input().split()))
head = create_linked_list(arr)
head = bubble_sort_linked_list(head)
print_linked_list(head)

res =13

# stack problem
def stack_problem():
    stack = []
    for i in range(1, 11):
        stack.append(i)
    while stack:
        print(stack.pop(), end=" ")
    print()
# Call the stack problem functionHṄK';
stack_problem()
# Output the result
print(res)