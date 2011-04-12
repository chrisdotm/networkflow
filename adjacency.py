# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python


class Adjacency:
    """
    Represent an adjacency object
    """
    def __init__(self, *args):
        self.successors = args

    def __str__(self):
        return "successor ( %s )" % ' '.join(self.successor)
