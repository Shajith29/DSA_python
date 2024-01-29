class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("The list is Empty")
        
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next

    def append(self,data):

        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next

            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
    
    def prepend(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node

        else:
            new_node = Node(data)
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
    

    def insert_after(self,key,data):
        curr = self.head
        
        while curr:
            if curr.next is None and curr.data == key:

                new_node = Node(data)
                curr.next = new_node
                new_node.prev = curr
                new_node.next = None
                return

            elif curr.data == key:

                nxt = curr.next
                new_node = Node(data)
                curr.next = new_node
                new_node.next = nxt
                new_node.prev = curr
                nxt.prev = new_node
            
            curr = curr.next

    def insert_before(self,key,data):
        curr = self.head
        while curr:
            if curr.prev is None and curr.data == key:
               new_node = Node(data)
               self.prepend(data)
               return 
            
            elif curr.data == key:
                new_node = Node(data)
                prev = curr.prev
                prev.next = new_node
                curr.prev = new_node
                new_node.next = curr
                new_node.prev = prev

            curr = curr.next

                
    
# dlist = DoublyLinkedList()
# dlist.append(1)
# dlist.append(2)
# dlist.append(3)
# dlist.append(4)
# dlist.prepend(0)
# dlist.print()

dlist = DoublyLinkedList()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.insert_before(4,12)
dlist.print()
