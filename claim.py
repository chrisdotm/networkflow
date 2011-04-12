# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python
from networkflowinstance import NetworkFlowInstance
from proposer import Proposer
from quality import Quality

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
        return "\"FlowClaim\"\n%s\n\"claim\"\"name\"%s\n%s\n%s" % (
                self.colleague, self.claim_name, self.nfi, self.quality)

    def __repr__(self):
        return str(self)

    def __name__(self):
        return "Claim"
