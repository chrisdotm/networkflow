# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python

class Proposer:
    """
    Represent a proposer
    """
    def __init__(self, name):
        """
        ; String -> Proposer
        """
        self.name = name

    def __str__(self):
        """
        ; -> String
        """
        return "\"proposer\" %s" % self.name

    def __repr__(self):
        """
        ; -> String
        """
        return str(self)

    def __name__(self):
        """
        ; -> String
        """
        return "Proposer"
