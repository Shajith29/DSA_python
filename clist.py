
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        new_node.next = None

    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        new_node.next = self.head
        self.head = new_node
    
    def print(self):
        if self.head is None:
            print("The list is empty")
        
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

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

    
    def remove(self,key):

        # if the key value equals to the head of the list
        if self.head.data == key:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next

            curr.next = self.head.next
            self.head = self.head.next
        
        #if the key value is not equals to the head of the list
            
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next

                if cur.data  == key:
                    prev.next = cur.next
                    cur = cur.next

    def __len__(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        
        return count
    
    def split_list(self):
        size = len(self)
        mid = size // 2
        count = 0

        if size == 0:
            return None

        if size == 1:
            return self.head
        
        prev = None
        curr = self.head

        while curr and count < mid:
            count += 1
            prev = curr
            curr = curr.next

        prev.next = self.head

        split_list = CircularLinkedList()

        while curr.next != self.head:
            split_list.append(curr.data)
            curr = curr.next

        split_list.append(curr.data)
        self.print()
        print("\n")
        split_list.print() 

    def remove_node(self,node):

        if self.head == node:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next

            curr.next = self.head.next
            self.head = self.head.next
        
            
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next

                if cur  == node:
                    prev.next = cur.next
                    cur = cur.next


    
    def jospheus_circle(self,step):
        curr = self.head

        while len(self) > 1:
            count = 1

            while count != step:
                curr = curr.next
                count += 1

            self.remove_node(curr) 
            curr = curr.next   

    def is_circular_linked_list(self,list):
        curr = list.head

        while curr:

            if curr.next == list.head: 
                return True

            curr = curr.next
            
        return False

                  
        




            
            


    


# clist = CircularLinkedList()
# clist.append(1)
# clist.append(2)
# clist.append(3)
# clist.remove(3)
    
# clist = CircularLinkedList()
# clist.append("A")
# clist.append("B")
# clist.append("C")
# clist.append("D")
# clist.split_list()
    
# jlist = CircularLinkedList()
# jlist.append(1)
# jlist.append(2)
# jlist.append(3)
# jlist.append(4)
# jlist.jospheus_circle(2)

slist = LinkedList()
slist.append(1)
slist.append(2)
clist = CircularLinkedList()
clist.append(1)
clist.append(2)
clist.append(3)
clist.append(4)
print(clist.is_circular_linked_list(clist))
print(clist.is_circular_linked_list(slist))