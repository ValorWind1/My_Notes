""" data structure stack

push insert item
pop taking out an item


"""

class Stack():
    def __init__(self):   # constructor will modify a python list
        self.items = [] # self.items is = to an empty list

    def push(self, item):
        self.items.append(item) # append its a python function its adding items to the end of the list.

    def pop(self):
        return self.items.pop() # pop python function takes out top element of " stack"/list

    def is_empty(self):         # checks if it's empty
        return self.items ==[]

    def peek(self):             # tells us what is the top most element of the stack
        if not self.is_empty():  # check first if the stack isempty
            return  self.items[-1]



    def get_stack(self):   # tester to be able to print items inside the stack
        return self.items

s = Stack()
s.push("A")  # a bottom visualisation of a stack
s.push("B")  # b is at the top in stack
print(s.get_stack())
s.push("C")
s.push("D")
print(s.get_stack())
s.pop()      # takes out last item
print(s.get_stack())
print(s.is_empty())
print(s.peek())