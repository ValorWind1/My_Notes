"""
Tree def: Root node( top most node), with child nodes, and leaf nodes(nodes with no children).

Binary Tree : each node has no more than 2 child nodes ( left , right child nodes) # child nodes they can be null

Binary search tree : fulfills specific order property : On any subtree the left nodes , are less than the root node
                    which is less than all of the right nodes. # very easy to find a node.

Insert : we have a value and we compare if its bigger/smaller than the root node. ( proceed accordingly, following the
        specific order property.

insert O(log n),find O(log n) Balanced vs Unbalanced trees: insert O(n),find:O(n)

Traversing tree : 3 ways Inorder traversal , Preorder Traversal , Postorder Traversal

-Preorder : Visit root first , then visit left ,and then right

-Inorder : Left node first , then root , then right  # Typically the best for binary search trees

-postorder : Left first , then right , then root

"""

# omitting deletion much harder with many implications
from random import randint

class node:
    def __init__(self , value=None):
        self.value= value
        self.left_child = None
        self.right_child = None  # start from no nodes in either left or right

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self,value):  # first function adding elements to search tree
        if self.root == None:  # checking if we can insert it at the root
            self.root = node(value)
        else :
            self._insert(value,self.root)  #_insert() function is recursive

    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None: # if left node is empty add it there
                cur_node.left_child==node(value)
            else:
                self. _insert(value,cur_node.left_child) # if there's a left child then, call again the recursive function
                                                         # put the node back into the function from the left side since is less than.
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child==node(value)        # the same as above but checking if right side is empty
            else:
                self._insert(value,cur_node.right_child)
        else:
            print ("Value already in Tree!")

    def print_tree(self):           # Print tree function to be able to see what's happening.
        if self.root != None:       # checking to see if there's a node on the root
            self. _print_tree(self.root)

    def _print_tree(self,cur_node): # just like our insert function, we will be using recursion
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print (str(cur_node.value))# inorder traversal
            self._print_tree(cur_node.right_child)


    def height(self):              # getting the height of the tree
        if self.root != None:
            return self. _height(self.root,0)
        else:
            return 0

    def _height(self,cur_node,cur_height):
        if cur_node == None:
            return cur_height
        left_height = self. _height(cur_node.left_child,cur_height+1)   # incrementing the height to allow the value to be measure correctly on the next recursive call
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height,right_height)  # whichever one is larger it will return that one , doing the comparison at every level of the tree

    def search(self,value):
        if self.root!= None:
            return self. _search(value,self.root)
        else:
            return False

    def _search(self,value,cur_node):
        if value == cur_node.value:
            return True
        elif value <cur_node.value and cur_node.left_child != None:
            return self.search(value,cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self.search(value,cur_node.right_child)
        return False         # If we dont get into any of the other 2 cases then return False, meaning we couldnt find the value



tree = binary_search_tree()

def fill_tree(tree ,num_elems=100,max_int=1000):

     for _ in range(num_elems):
         cur_elem = randint(0,max_int)
         tree.insert(cur_elem)
     return tree
#tree = fill_tree(tree)



tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(10)
tree.insert(0)
tree.insert(20)

tree.print_tree()

print ("tree height: "+ (str(tree.height())))

print (tree.search(10))
print (tree.search(30))

