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
    
    def delete(self,key):
        curr = self.head
        while curr:
            if curr.data == key and curr == self.head:

                #Case 1: 

                if not curr.next:
                    curr = None
                    self.head =  None
                    return
                
                #Case 2:
                
                else:
                    nxt = curr.next
                    curr.next = None
                    nxt.prev  = None
                    curr = None
                    self.head = nxt
                    return 
            
            elif curr.data == key:

                #Case 3: 
                if  curr.next:
                    nxt  = curr.next
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev  = prev
                    curr.next = None
                    curr.prev = None
                    curr = None
                    return
                 
                #Case 4: 
                else:
                    
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    curr = None
                    return
            
            curr = curr.next
    
    def reverse(self):
        temp = None
        curr = self.head

        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev

        if temp:
            self.head = temp.prev
        


dlist = DoublyLinkedList()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.print()
dlist.reverse()
dlist.print()
