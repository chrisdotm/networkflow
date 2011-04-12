# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python
from node import Node

class Adjacency:
    """
    Represent an adjacency object
    """
    def __init__(self, node, *args):
        self.node = node
        self.successors = args

    def __str__(self):
        successors = ''
        for successor in self.successors:
            successors += "%s " % str(successor)
        return "%s successor ( %s )" % (self.node, successors)

    def __repr__(self):
        successors = ''
        for successor in self.successors:
            successors += "%s " % str(successor)
        return "%s successor ( %s )" % (self.node, successors)
