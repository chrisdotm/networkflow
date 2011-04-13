#!/usr/bin/env
# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
from edgelabeledgraph import EdgeLabeledGraph

class Flow:
    """
    Represent a flow object
    """
    def __init__(self, elg):
        """
        ; EdgeLabeledGraph -> Flow
        """
        self.elg = elg

    def __str__(self):
        """
        ; -> String
        """
        return "\"solution\" \n %s" % self.elg

    def __repr__(self):
        """
        ; -> String
        """
        return str(self)

    def __name__(self):
        """
        ; -> String
        """
        return "Flow"
