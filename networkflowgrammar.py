#!/usr/bin/env python
# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
from pyparsing import *

from proposer import Proposer
from adjacency import Adjacency
from edgelabeledgraph import EdgeLabeledGraph
from networkflowinstance import NetworkFlowInstance
from flow import Flow
from node import Node
from nodeandlabel import NodeAndLabel

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()

## items in strings:
node = Suppress('"') + Word(alphas) + Suppress('"')
colleague = Optional(Suppress("proposer")) + Suppress("\"") +  Word(caps+alphas+"."+caps+alphas) + Suppress("\"")


edgecapacity = Suppress("c") + Word(nums)
nodeandlabel = node + Word(alphanums) + Word(alphanums)
adjacency = node + Suppress("successors") + Suppress("(") + ZeroOrMore(nodeandlabel) + Suppress (")")
nothing = Suppress(".")
quality = Suppress("quality") + Word(nums) + Optional(".") + Optional(Word(nums))

edgelabeledgraph = ZeroOrMore(adjacency)

networkflowinstance = Suppress("instance") + edgelabeledgraph + Suppress("source") + node + Suppress("sink") + node

flow = Suppress("\"solution\"") + edgelabeledgraph
edgeflow = Suppress("\"f\"") + nums

claim = Suppress("FlowClaim") + colleague + Suppress("claim") + Suppress("name") + Suppress("\"") + \
        Word(alphanums) + Suppress("\"") + networkflowinstance + quality

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
#print colleague.parseString(colleague_string)
#print quality.parseString(quality_string)
#print networkflowinstance.parseString(nfi_string)
#print Node(node.parseString(test_string)[0])
#print adjacency.parseString('"s" successors ( "t" c 20)')
#print NodeAndLabel(nodeandlabel.parseString(test_string)[0])
print claim.parseString(test_string)


