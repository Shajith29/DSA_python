class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("The List is empty")
        
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break
        


    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            
            curr_node.next = new_node
            new_node.next = self.head
    
    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        
        else:
            new_node.next = self.head
            curr = self.head

            while curr.next != self.head:
                curr = curr.next

            curr.next = new_node
            self.head = new_node
            



clist = CircularLinkedList()
clist.append(1)
clist.append(2)
clist.append(3)
clist.prepend(0)
clist.prepend(19)
clist.print()