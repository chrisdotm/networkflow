# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python
from edgelabeledgraph import EdgeLabeledGraph

class NetworkFlowInstance:
    """
    Represent a network flow instance
    """
    def __init__(self, elg, source, sink):
        self.elg = elg
        self.source = source
        self.sink = sink

    def __str__(self):
        return "\"instance\" \n %s \n \"source\" \n %s \n \"sink\" \n %s" % (
                self.elg, self.source, self.sink)

    def __repr__(self):
        return "\"instance\" \n %s \n \"source\" \n %s \n \"sink\" \n %s" % (
                self.elg, self.source, self.sink)
