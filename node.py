#!/usr/bin/env python
# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab


class Node:
    """
    Represents a node
    """
    def __init__(self, name):
        """
        ; String -> node
        """
        self.name = name

    def __str__(self):
        """
        ; -> String
        """
        return "\"%s\"" % str(self.name)

    def __repr__(self):
        """
        ; -> String
        """
        return str(self)

    def __name__(self):
        """
        ; -> String
        """
        return "Node"
