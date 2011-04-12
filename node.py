#!/usr/bin/env python
# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab

class Node:
    """
    Represents a node
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "\"%s\"" % str(self.name)

    def __repr__(self):
        return "\"%s\"" % str(self.name)
