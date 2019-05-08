class Vertex:
    def __init__(self,n): # constructor takes a name (n)
        self.name = n  # we assign name(n) to the variable name
        self.neighbors = list ()  # empty list of neighbors

        self.discovery = 0
        self.finish = 0
        self.color = "black"  # all vertices start at color black


    def add_neighbor(self,v):  # we received a vertex letter (v)
        nset = set (self.neighbors)
        if v not in nset :  # check to see if its already in our neighbor list
            self.neighbors.append(v)  # if its not then append it to the list
            self.neighbors.sort()  # and sort it to the list

class Graph :
    vertices = {}
    time = 0

    def add_vertex(self,vertex):  # receives a vertex
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices: # first check if what we passed is indeed a vertex, if not return false
            self.vertices[vertex.name] = vertex  #added to vertex list
            return True
        else :
            return False

    def add_edge(self,u,v):  # takes 2 values , the vertex at either end of the edge.
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items(): # if they are existing vertices in our graph , iterate through the vertices
                if key == u :                        # we find v / u and add a neighbor to it
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_grapgh(self):  # to see what our graph looks like
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors)+ " " +str(self.vertices[key].discovery))


        # 2 different ways to inplement the dfs function ( recursively , or iteraribly )
        # this is recursively

    def _dfs(self,vertex):
        global time
        vertex.color = "red"
        vertex.discovery = time
        time +=1
        for v in vertex.neighbors:
            if self.vertices[v].color == " black":
                self._dfs(self.vertices[v])
        vertex.color = " blue"
        vertex.finish = time
        time += 1
    def dfs(self,vertex):    # you pass the vertex where you are going to start at
        global time
        time = 1
        self._dfs(vertex)

g =Graph()
#print (str(len(g.vertices)))
a = Vertex("A")
g.add_vertex(a)
g.add_vertex(Vertex("B"))
for i in range ( ord ("A"), ord ("K")):
    g.add_vertex(Vertex(chr(i)))

edges = ["AB" , "AE", "BF", "CG", "DE", "DH", "EH", "FG", "FI", "FJ", "GJ", "HI"]
for edge in edges:
    g.add_edge(edge[:1],edge[1:])

g.dfs(a)
g.print_grapgh()