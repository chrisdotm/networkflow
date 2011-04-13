# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python
from adjacency import Adjacency


class EdgeLabeledGraph:
    """
    Represent an edge labeled graph
    takes a list of adjacencies
    """
    def __init__(self, *args):
        """
        ; listof(adjacecies) -> EdgeLabeledGraph
        """
        self.adjacencies = args[0]
        self.flow = {}

    def __str__(self):
        """
        ; -> String
        """
        adjacency_str = ''
        for adjacency in self.adjacencies:
            adjacency_str += '%s \n' % adjacency
        return adjacency_str

    def __repr__(self):
        """
        ; -> String
        """
        return str(self)

    def __name__(self):
        """
        ; -> String
        """
        return "EdgeLabeledGraph"

