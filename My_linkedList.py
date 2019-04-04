# Every node has 2 parts : a data , and a pointer to the next node
# link list its a collection of nodes.
# the next pointers always pointing to the next node

# the first node its called root, and the last node its called None/Null

# Popular Operations : include get_size() , finda(data), add(data), remove(data).

class Node(object): # our node class

    def __init__(self,d,n = None): # our constructor takes 2 arguments d for data, and n for next node n.(which defaults to None
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self,n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self,d):
          self.data = d

class LinkedList(object): # Linked List class , which needs 2 instace variables a root(the pointe to find the root node), and the size

    def __init__(self,r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self,d): # add function takes a piece of data d
        new_node = Node( d,self.root) # creates a new node using that piece of data, and will use as a pointer the next node the root node.
        self.root = new_node # will change the root node pointer to the new node
        self.size+= 1 # then, will increment size by 1

    def remove(self,d): # for the remove function we need first to do a find
        this_node = self.root # therefore, we track the current node that we are looking at which starts at the root
        prev_node = None #and also track the previous node, because we will have to change the pointer of the previous node

        while this_node: # while loop to iterate through the list
            if this_node.get_data() == d: # if we find the root node
                if prev_node:
                    prev_node.set_next(this_node.get_next()) # if we are not in the root node, we set previous node next pointer to "this" node next node pointer
                else:
                    self.root = this_node.get_next()
                self.size -= 1 # decrease size by 1
                return True # data removed, returning true
            else: # if we didn't find the data in the node returning false
                prev_node = this_node
                this_node = this_node.get_next()
        return False # data not found

    def find ( self, d):
        this_node = self.root # find function will start at the root node
        while this_node: # while there's still another node
            if this_node.get_data() == d: # it will look at each node to compare the data, with the data that we are looking for
                return d # if it finds it it will return the data
            else:
                this_node = this_node.get_next() # if it doesn't find it. it will move to the next node
        return None

    def printLinkedList(self): # printing the elements of the linked list
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


