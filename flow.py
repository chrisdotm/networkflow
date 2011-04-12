# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env


class Flow:
    """
    Represent a flow object
    """
    def __init__(self, elg):
        self.elg = elg

    def __str__(self):
        return "\"solution\" \n %s" % self.elg
