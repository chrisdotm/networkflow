#!/usr/bin/env python
# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
from pyparsing import *
#from proposer import Proposer
#from adjacency import Adjacency
#from edgelabeledgraph import EdgeLabeledGraph
#from networkflowinstance import NetworkFlowInstance
#from flow import Flow
#from node import Node
#from nodeandlabel import NodeAndLabel


caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()

class Parser:

    def __init__(self):
        """
        why would you even do this?
        """
        self.node = Suppress('"') + Word(alphanums) + Suppress('"')
        self.colleague = Optional(Suppress("proposer")) + Suppress("\"") +  Word(caps+alphas+"."+caps+alphas) + Suppress("\"")

        self.edgecapacity = Suppress("c") + Word(nums)
        self.nodeandlabel = self.node + Word(alphanums) + Optional(Word(alphanums))
        self.adjacency = self.node + Suppress("successors") + Suppress("(") + ZeroOrMore(self.nodeandlabel) + Suppress (")")
        self.nothing = Suppress(".")
        self.quality = Suppress("quality") + Word(nums) + Optional(".") + Optional(Word(nums))

        self.edgelabeledgraph = ZeroOrMore(self.adjacency)
        self.networkflowinstance = Suppress("instance") + self.edgelabeledgraph + Suppress("source") +\
                self.node + Suppress("sink") + self.node

        self.flow = Suppress("\"solution\"") + self.edgelabeledgraph
        self.edgeflow = Suppress("\"f\"") + nums

        self.claim = Suppress("FlowClaim") + self.colleague + Suppress("claim") + Suppress("name") + Suppress("\"") + \
                Word(alphanums) + Suppress("\"") + self.networkflowinstance + self.quality

    def __str__(self):
        """
        same here
        """
        pass

    def parse(self, expr):
        return self.claim.parseString(expr)









test_string = """
FlowClaim
proposer "Karl.Lieberherr"
claim name "1"
instance
"s" successors ( "t" c 20)
"t" successors ()
source "s"
sink "t"
quality 1.0
"""
nfi_string = 'instance "s" successors ( "t" c 20) "t" successors () source "s" sink "t"'
quality_string = 'quality 1.0'
colleague_string = 'proposer "Karl.Lieberherr"'
adjacency_string = '"99" successors ( )'
#print adjacency.parseString(adjacency_string)
#print colleague.parseString(colleague_string)
#print quality.parseString(quality_string)
#print networkflowinstance.parseString(nfi_string)
#print Node(node.parseString(test_string)[0])
#print adjacency.parseString('"s" successors ( "t" c 20)')
#print NodeAndLabel(nodeandlabel.parseString(test_string)[0])
#print claim.parseString(test_string)


