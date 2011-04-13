# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python
from node import Node


class NodeAndLabel:
    """
    Represents a node and label
    """
    def __init__(self, node, edgecap):
        """
        ; Node,String,String -> NodeAndLabel
        """
        self.node = node
        self.edgecap = edgecap

    def __str__(self):
        """
        ; -> String
        """
        return "%s %s " % (self.node, self.edgecap)

    def __repr__(self):
        """
        ; -> String
        """
        return str(self)

    def __name__(self):
        """
        ; -> String
        """
        return "NodeAndLabel"
