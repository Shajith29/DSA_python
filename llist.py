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



        
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(5)
ll.delete_position(3)
ll.print()