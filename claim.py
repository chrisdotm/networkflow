# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python

class Claim:
    """
    Represents a claim
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
