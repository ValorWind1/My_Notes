# priority queue using heapq

import heapq

qu = []    # python list

heapq.heapify(qu)
                                  # (5,d5)
heapq.heappush(qu,(5,"d5"))       # first element of the topple represents the priority and the second the data
heapq.heappush(qu,(1,"d1"))       #
heapq.heappush(qu,(3,"d3"))
heapq.heappush(qu,(2,"d2"))
heapq.heappush(qu,(4,"d4"))



heapq.heappop(qu) # retriving data according to the priority

heapq.heappop(qu)  # return element with second highest priority

print(heapq.heappop(qu))

print(heapq.heappop(qu))