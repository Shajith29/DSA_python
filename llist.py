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

    def insert_after(self,prev_data,data):
        new_node = Node(data)

        curr_node = self.head
        is_present = False

        while curr_node.next:
            if curr_node.data == prev_data:
                is_present = True
                new_node.next = curr_node.next
                curr_node.next = new_node

            curr_node = curr_node.next

        
        if not  is_present:
            print("The element is not the list")


    def delete_node(self,key):
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return 

        prev_node = None

        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            print("The element is not present in the list")

        prev_node.next = curr_node.next
        curr_node = None
        return 
    

    def delete_position(self,position):
        curr_node = self.head

        if  position == 0:
            self.head = curr_node.next
            curr_node = None
            return
        
    
        index = 1
        prev = None


        while curr_node and index != position:
            prev =  curr_node
            curr_node = curr_node.next
            index += 1

        if curr_node is None:
            print("The Element is not present in the list")
            return 
        
        prev.next = curr_node.next
        curr_node = None

        #function to calculate the length of the list iteratively

    def length_iterative(self):
        count = 0
        if self.head is None:
            count = 0
        
        
        curr_node = self.head
        while curr_node:
            curr_node = curr_node.next
            count += 1
        
        return count
    
    #function to find the length of the list recursively
    
    def length_recursive(self,node):
        if node is None:
            return 0
        
        return 1 + self.length(node.next)


    
    def swap_nodes(self,key_1,key_2):
      if key_1 == key_2:
          return 
      
      prev_1 = None
      curr_1 = self.head

      while curr_1 and curr_1.data != key_1:
          prev_1 = curr_1
          curr_1 = curr_1.next

      prev_2 = None
      curr_2 = self.head

      while curr_2 and curr_2.data != key_2:
          prev_2 = curr_2
          curr_2 = curr_2.next

      if not curr_1 or not curr_2:
          return 
      
      if prev_1:
          prev_1.next = curr_2
      else:
          self.head = curr_2

      if prev_2:
          prev_2.next = curr_1
      else:
          self.head = curr_1

      curr_1.next,curr_2.next = curr_2.next,curr_1.next



    def reverse_iterative(self):
        prev = None
        curr_node = self.head

        while curr_node:
            nxt = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = nxt

        self.head  = prev

    def reverse_recursive(self):
        
        def _reverse_recursive(curr,prev):
            if not curr:
                return prev
            
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

            return _reverse_recursive(curr,prev)

        self.head = _reverse_recursive(curr=self.head,prev=None)

    
   
    def sorted_merge(self,llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next

            new_node = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
            
            if not p:
                s.next = q

            if not q:
                s.next = p
        
        return new_node
    

    def remove_duplicates(self):
        curr_node = self.head
        nodes = dict()
        prev_node = None

        while curr_node:
            if curr_node.data not in nodes:
                nodes[curr_node.data] = 1
                prev_node = curr_node
               
            else:
                prev_node.next = curr_node.next

            curr_node = prev_node.next

    
    def n_to_the_last_node(self,n):

        #Method 1
        # llength = self.length_iterative()

        
        # curr_node = self.head
        # while curr_node:
        #     if llength == n:
        #         return curr_node.data
            
        #     llength -= 1
        #     curr_node = curr_node.next
            
        #     if curr_node is None:
        #         return 


        p = self.head
        q = self.head

        count = 0

        while q and count < n:
            q = q.next
            count += 1

        if not q:
            print(str(n) + " greater than the length of the list")
        
        while p and q:
            p = p.next
            q = q.next
        return p.data
    
    def count_the_occurences_iterative(self,data):
        count = 0
        curr = self.head
        while curr:
            if curr.data == data:
                count += 1

            curr = curr.next
        
        return count
    
    def count_the_occurences_recursive(self,node,data):
        if not node:
            return 0
        
        if node.data == data:
            return 1 + self.count_the_occurences_recursive(node.next,data)
        else:
            return self.count_the_occurences_recursive(node.next,data)
        
    
    def rotate(self,k):
        p = self.head
        q = self.head
        count = 0
        prev = None

        while p and count < k:
            prev = p
            p  = p.next
            q  = q.next
            count += 1
        
        p = prev
        
        while q:
            prev = q
            q = q.next        
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None

            
            

        
# list1 = LinkedList()
# list1.append(1)
# list1.append(5)
# list1.append(7)
# list1.append(9)
# list1.append(10)

# list2 = LinkedList()
# list2.append(2)
# list2.append(3)
# list2.append(4)
# list2.append(6)
# list2.append(8)

# list1.sorted_merge(list2)
# list1.print()
    
# list1 = LinkedList()
# list1.append(1)
# list1.append(2)
# list1.append(3)
# list1.append(4)
# print(list1.n_to_the_last_node(2))
    
# list1 = LinkedList()
# list1.append(1)
# list1.append(2)
# list1.append(2)
# list1.append(1)
# list1.append(3)
# list1.append(4)
# list1.append(1)
# print(list1.count_the_occurences_iterative(1))
# print(list1.count_the_occurences_recursive(list1.head,4))
        
list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
list1.append(6)
list1.print()
print('\n')
list1.rotate(3)
list1.print()





