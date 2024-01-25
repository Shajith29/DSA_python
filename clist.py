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


            
            


    


# clist = CircularLinkedList()
# clist.append(1)
# clist.append(2)
# clist.append(3)
# clist.remove(3)
    
clist = CircularLinkedList()
clist.append("A")
clist.append("B")
clist.append("C")
clist.append("D")
clist.split_list()