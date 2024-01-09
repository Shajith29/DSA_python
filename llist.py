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

        

        
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.reverse_iterative()
ll.print()
