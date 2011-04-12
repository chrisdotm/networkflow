# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env


class EdgeFlow:
    """
    Represents an edgeflow
    """
    def __init__(self, flow_int):
        self.flow_int = flow_int

    def __str__(self):
        return "\"f\" %d" self.flow_int
