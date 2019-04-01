# Implementing adjacency lists using dictionaries to represent sparse graphs - graphs with less number of edges

class Vertex:

    def __init__(self, key ):
        self.id = key
        self.connectedTo = {}

    # Add an edge along with weight
    def addneighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    # Return all vertices connected to this vertex
    def getconnections(self):
        return self.connectedTo.keys()

    # Return weight of the edge connected to a particular vertex
    def getweights(self, endpoint):
        return self.connectedTo[endpoint]

    def getid(self):
        return self.id

    # returns a string version of the object
    def __str__(self):
        return str(self.id) + ' connected to ' + str([x.id for x in self.connectedTo])

class Graph:

    def __init__(self):
        self.verticesList = {}
        self.numVertices = 0

    def addvertex(self,key):
        self.numVertices += 1
        new_vertex = Vertex(key)
        self.verticesList[key] = new_vertex


    def getvertex(self,n):
        if n in self.verticesList:
            return self.verticesList[n]
        else:
            return None


    def addedge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.verticesList:
            self.addvertex(start_vertex)
        if end_vertex not in self.verticesList:
            self.addvertex(end_vertex)
        self.verticesList[start_vertex].addneighbor(self.verticesList[end_vertex], weight)

    def getvertices(self):
        return self.verticesList.keys()

    # create an iterator for the graph object that iterates through the edges
    def __iter__(self):
        return iter(self.verticesList.values())

    # implement contains for the graph object that checks if the vertex exists in the graph
    def __contains__(self, item):
        return item in self.verticesList

    def __len__(self):
        return len(self.verticesList)

def breadthfirstSearch(graph, start):
    # start vertex - start

    # use this to keep track if a node was visited
    visited = [False] * (len(graph) + 1)

    queue = []
    start_vertex = graph.getvertex(start)
    visited[start_vertex.id] = True
    queue.append(start_vertex)
    print start_vertex.id,

    while queue:
        s = queue.pop(0)
        for item in s.getconnections():
            if visited[item.id] == False:
                queue.append(item)
                visited[item.id] = True
                print item.id,


# Recursive depth first traversal
def dfsutil(graph, start_vertex, visited):
    print start_vertex.id,
    visited[start_vertex.id] = True
    for item in start_vertex.getconnections():
        if visited[item.id] != True:
            dfsutil(graph, item, visited)



def depthfirst(graph, start):
    visited = [False] * (len(graph) + 1)

    start_vertex = graph.getvertex(start)
    dfsutil(graph, start_vertex, visited)

# Find a cycle in a graph
def hasCycle(graph):

    visited = [False] * (len(graph) + 1)
    # Start from first vertex in the list
    start_vertex = graph.getvertex(1)
    visited[start_vertex.id] = True
    queue = []
    queue.append(start_vertex)

    while queue:
        s = queue.pop(0)
        for item in s.getconnections():
            if visited[item.id] == True:  #Cycle detected
                return True
            else:
                visited[item.id] = True
                queue.append(item)
    return False



"""
Word Ladder problem : Build a graph from a file containing words
create buckets - with just one character differing and add the words in corresponding buckets. all words in a bucket 
must be connected
"""

def buildgraph(wordfile):
    d = {}
    G = Graph()
    wfile = open(wordfile, "r")

    for line in wfile:
        print line
        word = line[:-1]
        print word
        # Create buckets and add words to respective buckets
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

        # add vertices and edges for words in each bucket
        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        G.addedge(word1, word2)
        return G



G = Graph()
for i in range(1, 7):
    G.addvertex(i)

G.addedge(1, 5)
G.addedge(1, 4)
G.addedge(2, 3)
G.addedge(2, 4)
G.addedge(1, 6)
G.addedge(3, 5)
G.addedge(4, 2)
G.addedge(5, 3)
G.addedge(6, 2)

for item in G:
    print item
print(hasCycle(G))






