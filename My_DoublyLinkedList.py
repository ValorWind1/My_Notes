""" doubly linked lists (bidirectional)
 every node has 3 parts, it has a pointer to the previous node the data ,a piece of data
  and a pointer to the next node. so it can go forward or backwards through the linked list
  but it uses more memory"""

class Node(object): # our node class

    def __init__(self,d,n = None, p = None): # we need a previous node in constructor
        self.data = d
        self.next_node = n
        self.prev_node = p  # set it to = p

    def get_next(self):
        return self.next_node

    def set_next(self,n):
        self.next_node = n

    def get_prev(self):    # get previous node value
        return self.prev_node

    def set_prev(self, p): # set previous node value
        self.prev_node = p

    def get_data(self):
        return self.data

    def set_data(self, d):
          self.data = d

class LinkedList(object):

    def __init__(self,r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self,d):
        new_node = Node( d,self.root)
        if self.root:         # check if there's at least 1 node in the linked list already
            self.root.set_prev(new_node) # if there's a root node we set the prev pointer to the new node
        self.root = new_node
        self.size+= 1

    def remove(self,d):
        this_node = self.root

        while this_node:
            if this_node.get_data() == d: # if we find the root node
                next = this_node.get_next() # we set our next and previous pointers
                prev = this_node.get_prev()

                if next:
                    next.set_prev(prev) # then , we set prev , and next to the other prev and next
                if prev :
                    prev.set_next(next)

                else:
                    self.root = this_node
                self.size -= 1
                return True

            else:

                this_node = this_node.get_next()
        return False # data not found

    def find ( self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

    def printLinkedList(self):
        node = self.root
        while node != None:
            print(node.get_data())
            node = node.get_next()


myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.remove(8)
myList.printLinkedList() # calling printing method of printing elements of a linked list

print(myList.remove(12))
print(myList.find(5))
