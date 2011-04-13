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
from quality import Quality
from claim import Claim
from edgecapacity import EdgeCapacity


caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()
QUOTE = Suppress("\"")
LPAREN = Suppress("(")
RPAREN = Suppress(")")


def makeNodeObject(n):

    def nodeAction(s, l, t):
        try:
            return n(t[0].asList())
        except:
            return n(t)
    return nodeAction


def nodeandlabel(n):
    n = n[0]
    return NodeAndLabel(n[0], n[1])


def claim(n):
    n = n[0]
    return Claim(n[0], n[1], n[2], n[3])


class Parser:
    def __init__(self):
        """
        why would you even do this?
        """

        self.node = Group(QUOTE + Word(alphanums) + QUOTE).setParseAction(
                lambda t: Node(t[0][0]))
        self.colleague = Group(Optional(Suppress("proposer")) + QUOTE +\
                               Word(caps + alphas + "." + caps + alphas) +\
                               QUOTE).setParseAction(lambda t: Proposer(t[0][0]))
        self.nothing = Suppress(".")

        self.edgecapacity = Group(
                Suppress("c") + Word(nums)
                ).setParseAction(lambda t: EdgeCapacity(t[0][0]))
        self.nodeandlabel = Group(self.node + self.edgecapacity
                ).setParseAction(lambda t: nodeandlabel(t))
        self.adjacency = Group(
                self.node + Suppress("successors") + LPAREN +\
                        ZeroOrMore(self.nodeandlabel) +\
                        RPAREN).setParseAction(lambda t: Adjacency(t[0][0], t[0][1:]))
        self.quality = Group(
                Suppress("quality") + Word(nums) + \
                Optional(".") + Optional(Word(nums))
                ).setParseAction(lambda t: Quality(t[0][0]))

        self.edgelabeledgraph = Group(
                ZeroOrMore(self.adjacency)
                ).setParseAction(lambda t: EdgeLabeledGraph(t[0][0:]))
        self.networkflowinstance = Group(
                Suppress("instance") + \
                self.edgelabeledgraph + \
                Suppress("source") +\
                self.node + Suppress("sink") + self.node
                ).setParseAction(lambda t: NetworkFlowInstance(t[0][0], t[0][1], t[0][2]))

        self.flow = Group(
                Suppress("\"solution\"") + self.edgelabeledgraph
                ).setParseAction(lambda t: Flow(t[0][0]))

        self.edgeflow = Group(
                Suppress("\"f\"") + nums
                ).setParseAction(lambda t: EdgeFlow(t[0][0]))

        self.claim = Group(
                Suppress("FlowClaim") + self.colleague + \
                Suppress("claim") + Suppress("name") + QUOTE + \
                Word(alphanums) + QUOTE + self.networkflowinstance + \
                self.quality).setParseAction(
                        lambda t: claim(t))

    def __str__(self):
        """
        same here
        """
        pass

    def parse(self, expr):
        return self.claim.parseString(expr)


## TESTS:
parser = Parser()
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
nfi_string = 'instance "s" successors ( "t" c 20) "t" successors () source "s" sink "t" quality 1.0'
quality_string = 'quality 1.0'
colleague_string = 'proposer "Karl.Lieberherr"'
adjacency_string = '"99" successors ( )'
#print adjacency.parseString(adjacency_string)
#print colleague.parseString(colleague_string)
#print networkflowinstance.parseString(nfi_string)
#print Node(node.parseString(test_string)[0])
#print NodeAndLabel(nodeandlabel.parseString(test_string)[0])
#print claim.parseString(test_string)

#print str(parser.node.parseString('"999"'))
#print parser.colleague.parseString('proposer "Karl.Lieberherr"')
#print parser.edgecapacity.parseString('c 99')
#print parser.nodeandlabel.parseString('"t" c 20')
#print parser.adjacency.parseString('"s" successors ( "t" c 20 )')
#print parser.quality.parseString(quality_string)
#print parser.edgelabeledgraph.parseString('"s" successors ( "t" c 20) "t" successors ()')
#print parser.networkflowinstance.parseString(nfi_string)

#print parser.claim.parseString(test_string)

##assert Node("s") == parser.node.parseString("s")
