"""
graph it's made out of nodes , which are connected by edges , and edges have a number/weight.

the more weight = the more expensive to travel

dijkstra's algorithm: finds the shortest path as long as they are positive
                    (removes the smallest cost entry )

    - min Priority Queue : add nodes with their weight(in this case weight = priority)
        inside min priority queue = starting node = 0
        remove the smallest from PQ, and added to visited nodes
        we dont visit twice nodes that are alredy inside the visited nodes list



"""

graph = {"a":{"b":5,"c":10},"b":{"c":8,"d":4},"c":{"b":2,"d":6,"e":3},"d":{"e":1},"e":{"d":9}}

def dijkstra(graph,start,goal):
    shortes_distance = {}   # empty dictionary, it gets to be constantly updated
    predecessor = {}        # empty dictionary, where the path came from to get shortest distance
    unseenNodes = graph     # run through all nodes
    infinity = 9999999
    path = []               # to be able to show at the end
    for node in unseenNodes:
        shortes_distance[node] = infinity
    shortes_distance[start] = 0   # starting point starts at 0
    # print(shortes_distance)



    while unseenNodes:  # checks if dictionary its empty
        minNode = None  # greedy algorithm choose node that has the lowest value of all
        for node in unseenNodes:    # go through all of the nodes and finds the one with the shortest distance
            if minNode is None:
                minNode = node
            elif shortes_distance[node] < shortes_distance[minNode]:
                minNode = node

        # main part of the dijkstra algorithm / ( what makes it work )
        for childNode, weight in graph[minNode].items():   # we have a node to focused , so the we look to all of its child nodes
            if weight+shortes_distance[minNode] < shortes_distance[childNode]:
                shortes_distance[childNode] = weight+shortes_distance[minNode]
                predecessor[childNode] = minNode           # we want to know how it got to the end
        unseenNodes.pop(minNode)
    print(shortes_distance)
    print(predecessor)

    # writing the path

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]

        except KeyError:
            print("path not reachable")
            break
    # printing it out
    path.insert(0,start)
    if shortes_distance[goal] != infinity:
        print("shortest distance is " + str(shortes_distance[goal]))
        print("and the path is" + str(path))




dijkstra(graph,"a","d")
