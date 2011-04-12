# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python
from pyparsing import Word, alphas, alphanums, Literal, restOfLine, OneOrMore
from pyparsing import empty, Suppress, replaceWith

from proposer import Proposer
from adjacency import Adjacency
from edgelabeledgraph import EdgeLabeledGraph
from networkflowinstance import NetworkFlowInstance
from flow import Flow


def main(expression):
    """
    parses expression and turns it into object which are useable in python
    finds best network flow
    returns representation of best network flow in our language
    """
    pass

def parse(expr):
    """
    parse expr to objects
    """
    pass

def find_flow(nfi):
    """
    find best flow
    """
    pass

if __name__ == '__main__':
    # later from stdin now from file
    main(open('/scratch/cmccoy/algo/8/lang.txt'))

