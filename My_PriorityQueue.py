"""
Priority Queue : Abstract data type(ADT), operates similar to a normal queue EXCEPT
                that each element has a certain priority.
        the priority of the elements determine the order in which elements are removed from the Priority Queue.

Poll () = remove the element that has the highest priority in our queue
add()= add element to priority queue

how does a priority queue know which is the next smallest number to remove(in an example smallest to biggest)
smallest had a bigger priority.)?
    - it uses a HEAP
    - a heap it's : a tree based data structure, that follows the heap property :

                                        - Value of the parent node it's always greater than, or equal to the value of the child
                                        nodes through all nodes( Max Heap)
                                        - or the Value of the parent node it's less than or equal to the child nodes of through
                                        all the nodes ( Min Heap)

Priority queue USES : Dijkstra's - shortest path algorithm
    -anytime we need to dynamically fetch the next best or next worst element.
    -huffman coding
    - BFS(best first search) - A*
    -MST ( minimum spanning tree algorithm)



"""

# simply priority queue object orientend way

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

        # for checking if the queue is empty

    def isEmpty(self):
        return len(self.queue) == []

        # for inserting an element in the queue

    def insert(self, data):
        self.queue.append(data)

        # for popping an element based on Priority

    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()



myQueue = PriorityQueue()
myQueue.insert(12)
myQueue.insert(1)
myQueue.insert(14)
myQueue.insert(7)
print(myQueue)
while not myQueue.isEmpty():
    print(myQueue.delete())




# priority queue using heapq

import heapq

qu = []    # python list
                                  # (5,d5)
heapq.heappush(qu,(5,"d5"))       # first element of the topple represents the priority and the second the data
heapq.heappush(qu,(1,"d1"))       #
heapq.heappush(qu,(3,"d3"))
heapq.heappush(qu,(2,"d2"))
heapq.heappush(qu,(4,"d4"))

heapq.heappop(qu) # retriving data according to the priority

print(heapq.heappop(qu))