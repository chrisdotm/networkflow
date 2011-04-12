# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python
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
colleague = Suppress('"') +  Word(caps, alphas, "." , caps, alphas) + Suppress('"')


edgecapacity = Word("c") + nums  
nodeandlabel = node + Word(alphanums) + Word(alphanums)  
adjacency = node + Suppress("successors") + Suppress("(") + ZeroOrMore(nodeandlabel) + Suppress (")")   

test_string = """
FlowClaim
"Karl.Lieberherr"
instance
"s" successors ( "t" c 20)
"t" successors ()
source "s"
sink "t"
quality 1.0
"""
##print Node(node.parseString('"v"')[0])


