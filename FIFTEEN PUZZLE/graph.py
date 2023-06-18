
#author: Anshul Jagtap



from collections import deque

class Vertex:

    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

# To assign the weight to neigbour 
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

#adding the vertex 
    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

#to get the vertex
    def getVertex(self,n):
        for vertex in self.vertList.values():
            if vertex.getId() == n:
                return vertex
        return None

    def __contains__(self, vertex):
        return vertex in self.vertList.values()

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

# Implementing BFS 
    def breadth_first_search(self, s):
        start = self.getVertex(s)
        start.color = 'gray'
        queue = deque([start])
        path = []
        while queue:
            current = queue.popleft()
            path.append(current.id)
            for neighbor in current.getConnections():
                if neighbor.color == 'white':
                    neighbor.color = 'gray'
                    queue.append(neighbor)
            current.color = 'black'
        return path

# Implementing DFS
    def depth_first_search(self):
        path = []
        for vertex in self:
            vertex.color = 'white'
        for vertex in self:
            if vertex.color == 'white':
                self.DFS(vertex, path)
        return path


    def DFS(self, vid, path):
        vid.color = 'gray'
        path.append(vid.id)
        for neighbor in vid.getConnections():
            if neighbor.color == 'white':
                self.DFS(neighbor, path)
        vid.color = 'black'



#Given driver code to check if the code works 

if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)

    g.addEdge(0,1)
    g.addEdge(0,5)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(4,0)
    g.addEdge(5,4)
    g.addEdge(5,2)
  

    for v in g:
        print(v)

    assert (g.getVertex(0) in g) == True
    assert (g.getVertex(6) in g) == False

    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'

    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'

    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]

    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]                