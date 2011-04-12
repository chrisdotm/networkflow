# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python
from node import Node

class NodeAndLabel:
    """
    Represents a node and label
    """
    def __init__(self, node, label1, label2):
        self.node = node
        self.label1 = label1
        self.label2 = label2

    def __str__(self):
        return "%s %s %s" % (self.node, self.label1, self.label2)


    def __repr__(self):
        return "%s %s %s" % (self.node, self.label1, self.label2)
