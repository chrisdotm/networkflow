# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env


class EdgeFlow:
    """
    Represents an edgeflow
    """
    def __init__(self, flow_int):
        """
        ; int -> EdgeFlow
        """
        self.flow_int = flow_int

    def __str__(self):
        """
        ; -> String
        """
        return "\"f\" %d" % self.flow_int

    def __repr__(self):
        """
        ; -> String
        """
        return str(self)

    def __name__(self):
        """
        ; -> String
        """
        return "EdgeFlow"
