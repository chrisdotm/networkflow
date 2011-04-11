#!/usr/bin/env python
from pyparsing import Word, alphas, alphanums, Literal, restOfLine, OneOrMore
from pyparsing import empty, Suppress, replaceWith

from proposer import Proposer
from adjacency import Adjacency
from edgelabeledgraph import EdgeLabeledGraph
from networkflowinstance import NetworkFlowInstance
from flow import Flow


def main(expression):
    pass

if __name__ == '__main__':
    # later from stdin now from file
    main(open('/scratch/cmccoy/algo/8/lang.txt'))

