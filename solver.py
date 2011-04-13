"""
http://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
this came from here I didnt write it
i made some edits which i feel make it fit the assignment more
"""

class Edge:
    def __init__(self, u, v, w):
        self.source   = u
        self.sink     = v
        self.capacity = w
    def __repr__(self):
        return str(self.source) + "->" + str(self.sink) + " : " + str(self.capacity)

class FlowNetwork(object):
    def __init__(self):
        self.adj, self.flow, = {}, {}

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def get_edges(self, v):
        return self.adj[v]

    def add_edge(self, u, v, w=0):
        if u == v:
            print u
        assert(u != v)
        edge  = Edge(u,v,w)
        redge = Edge(v,u,0)
        edge.redge  = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge]  = 0
        self.flow[redge] = 0

    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge,residual) in path:
                result = self.find_path( edge.sink, sink, path + [(edge,residual)] )
                if result != None:
                    return result

    def max_flow(self, source, sink):
        # used is the list of paths used to compute the final flow
        used = []
        path = self.find_path(source, sink, [])
        while path != None:
            used.append(path)
            flow = min(res for edge,res in path)
            for edge,res in path:
                self.flow[edge]       += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return {"flow":sum(self.flow[edge] for edge in self.get_edges(source)),
                "path": used}
