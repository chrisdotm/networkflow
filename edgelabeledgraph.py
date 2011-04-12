# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python
from adjacency import Adjacency

class EdgeLabeledGraph:
    """
    Represent an edge labeled graph
    """
    def __init__(self, *args):
        self.adjacencies = args

    def __str__(self):
        adjacency_str = ''
        for adjacency in self.adjacencies:
            adjacency_str += '%s ' % adjacency
        return adjacency_str

    def __repr__(self):
        adjacency_str = ''
        for adjacency in self.adjacencies:
            adjacency_str += '%s ' % adjacency
        return adjacency_str
