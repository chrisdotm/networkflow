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
import solver


def main():
    """
    parses expression and turns it into object which are useable in python
    finds best network flow
    returns representation of best network flow in our language
    """
    solve()

def parse(expr):
    """
    parse expr to objects
    """
    parser = Parser()
    return parser.parse(expr)[0]

def solve():
    lang_file = open('./lang.txt')
    lang = ' '.join(lang_file.readlines())
    lang_file.close()

    network = parse(lang)
    elg = network.nfi.elg

    s = solver.FlowNetwork()
    # you have to loop twice here no way around it :(
    map(s.add_vertex, [adj.node.name for adj in elg.adjacencies])


    for adj in elg.adjacencies:
        for successor in adj.successors:
            s.add_edge(adj.node.name,
                    successor.node.name,
                    successor.edgecap.capacity)

    print s.max_flow(network.nfi.source.name,
            network.nfi.sink.name)


def test():
    return main(open('./lang.txt').readlines())


if __name__ == '__main__':
    # later from stdin now from file
    main()

