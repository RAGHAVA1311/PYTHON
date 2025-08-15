class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
# largest element in a linked list
    def slargest(self):
        if not self.head:
            return None
        l = self.head.data
        cn= self.head
        while cn:
            if cn.data > l:
                l = cn.data
            cn = cn.next
        cn = self.head
        sl = self.head.data
        while cn:
            if cn.data > sl and cn.data < l:
                sl = cn.data
            cn = cn.next
        return sl
# mid element in a linked list
    def mid(self):
        slow = self.head
        fast = self.head
        if not self.head:
            return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
u = LinkedList()
u.append(1)
u.append(2)
u.append(3)
u.append(4)
u.append(5)
u.display()
print(u.slargest())

