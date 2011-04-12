#!/usr/bin/env python
# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
from parser import Parser
from proposer import Proposer
from adjacency import Adjacency
from edgelabeledgraph import EdgeLabeledGraph
from networkflowinstance import NetworkFlowInstance
from flow import Flow
from node import Node
from nodeandlabel import NodeAndLabel


def main(expression):
    """
    parses expression and turns it into object which are useable in python
    finds best network flow
    returns representation of best network flow in our language
    """
    print parse(' '.join(expression))

def parse(expr):
    """
    parse expr to objects
    """
    parser = Parser()
    return parser.parse(expr)

def find_flow(nfi):
    """
    find best flow
    """
    pass

if __name__ == '__main__':
    # later from stdin now from file
    input = open('./lang.txt')
    main(input.readlines())

