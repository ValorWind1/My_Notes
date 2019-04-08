"""
Queues: is basically a limited list. only allows data to be inserted from one end, and retrieved from the other.
A special implementation of a list.

This is a FIFO DTS(data structure), first value in first value out.

data pushed INTO the queue = enqueue
data is RETRIEVED from the queue = dequeue


Import things to remember : No ability to insert or retrieve from any other location from the list except from
the data enqueue at front end, or data dequeue at back end ..

"""

# # queue it's basically just a list
# queue = ["Wake up","Have a coffee", "Have a shower", "Get dressed", "have breakfast","Go to work"] # end of queue where push will insert item to
#
# # view the list
# def view():
#     for x in range(len(queue)):
#         print(queue[x])
#
# def push():
#     item = input("Please enter the item you wish to add to the queue: ")
#     queue.append(item)
#
# def pop():
#     item=queue.pop(0) # pops out the first item in the queue
#     print("You just popped out: ", item)
#
#
# # test case
#
# while True :
#     print("")
#     print("Python Implementation of a Queue")
#     print("----")
#     print("1. view queue")
#     print("2.push onto Queue")
#     print("3. pop out of queue")
#     print("----")
#     print("")
#     menu_choice = int(input("Enter your menu choice : "))
#     print("")
#     print("")
#
#     if menu_choice == 1:
#         view()
#     elif menu_choice == 2:
#         push()
#     elif menu_choice == 3:
#         pop()


 # making the same program in an object oriented program ------------------------------------------------------------

class queue_class():
     def __init__(self):
         self.a_queue= ["Wake up","Have a coffee", "Have a shower", "Get dressed", "have breakfast","Go to work"] # end of queue where push will insert item to

     def view (self):
         for x in range(len(self.a_queue)):
             print(self.a_queue[x])

     def push(self):
         item = input("Enter the item of your choice to the queue:")
         self.a_queue.append(item)

     def pop(self):
         item =self.a_queue.pop(0)
         print("You just popped out: ", item)


# test case
queue = queue_class() # create the object from the class
while True:

    print("")
    print("Python Implementation of a Queue")
    print("----")
    print("1. view queue")
    print("2.push onto Queue")
    print("3. pop out of queue")
    print("----")
    print("")
    menu_choice = int(input("Enter your menu choice : "))
    print("")
    print("")

    if menu_choice == 1:
        queue.view()
    elif menu_choice == 2:
        queue.push()
    elif menu_choice == 3:
        queue.pop()

