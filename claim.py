# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python

class Claim:
    """
    Represents a claim
    """
    def __init__(self, colleague, claim, nfi, quality):
        self.colleague = colleague
        self.claim_name = claim
        self.nfi = nfi
        self.quality = quality


    def __str__(self):
        return """
        \"FlowClaim\"
        %s
        \"claim\" \"name\" %s
        %s
        %s
        """ % (self.colleague, self.claim_name, self.nfi, self.quality)

    def __repr__(self):
        return """
        \"FlowClaim\"
        %s
        \"claim\" \"name\" %s
        %s
        %s
        """ % (self.colleague, self.claim_name, self.nfi, self.quality)
