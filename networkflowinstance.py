# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python
from edgelabeledgraph import EdgeLabeledGraph
from node import Node


class NetworkFlowInstance:
    """
    Represent a network flow instance
    """
    def __init__(self, elg, source, sink):
        self.elg = elg
        self.source = source
        self.sink = sink
        self.flow = {}

    def __str__(self):
        return "\"instance\" \n %s \n \"source\" \n %s \n \"sink\" \n %s" % (
                self.elg, self.source, self.sink)

    def find_path(self, source, sink, path):
        if source is sink:
            return path
        for nal in self.get_edges(source):
            if self.flow.get(nal) is None:
                self.flow[nal] = 0
            residual = nal.edgecap.capacity - self.flow[nal]
            if residual > 0 and not (nal, residual) in path:
                result = self.find_path(nal.sink, sink, path + [(edge, residual)])
                if result is not None:
                    return result

    def get_edges(self, node):
        """
        ; node -> listof(nodeandlabel)
        """
        adj_list = self.elg.adjacencies
        for adj in adj_list:
            if adj.node == node:
                return adj.successors
        return None

    def max_flow(self):
        path = self.find_path(self.source, self.sink, [])
        while path is not None:
            flow = min(res for edge, res in path)
            for edge, res in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -+ flow
            path = self.find_path([])
        return sum(self.flow[edge] for edge in self.get_edges())

    def __repr__(self):
        return str(self)

    def __name__(self):
        return "NetworkFlowInstance"
