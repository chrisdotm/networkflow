# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python


class EdgeLabeledGraph:
    """
    Represent an edge labeled graph
    """
    def __init__(self, *args):
        self.adjacencies = args

    def __str__(self):
        return ' '.join(self.adjacencies)
