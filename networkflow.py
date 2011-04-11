#!/usr/bin/env python
from pyparsing import Word, alphas, alphanums, Literal, restOfLine, OneOrMore
from pyparsing import empty, Suppress, replaceWith


class Proposer(Object):
    """
    Represent a proposer
    """
    def __init__(self):
        pass

    def __str__(self):
        pass

class EdgeLabeledGraph(Object):
    """
    Represent an edge labeled graph
    """
    def __init__(self):
        pass

    def __str__(self):
        pass

class Adjacency(Object):
    """
    Represent an adjanceny object
    """
    def __init__(self):
        pass

    def __str__(self):
        pass

class NetworkFlowInstance(Object):
    """
    Represent a network flow instance
    """
    def __init__(self):
        pass

    def __str__(self):
        pass

class Flow(Object):
    """
    Represent a flow object
    """
    def __init__(self):
        pass

    def __str__(self):
        pass


def main(expression):


if __name__ == '__main__':
    # later from stdin now from file
    main(open('/scratch/cmccoy/algo/8/lang.txt'))

