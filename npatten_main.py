#!/usr/bin/env python
from parser import Parser
from proposer import Proposer
from adjacency import Adjacency
from edgelabeledgraph import EdgeLabeledGraph
from networkflowinstance import NetworkFlowInstance
from flow import Flow
from node import Node
from nodeandlabel import NodeAndLabel

import solver
import sys

## opens the given claims file, parses it, and refutes or supports the claims 
def playSciGame(file_path):
    claims_file = open(file_path)
    lines = ' '.join(lang_file.readlines())
    claims_file.close()

    network = parse(lines)
    elg = network.nfi.elg

    solver = solver.FlowNetwork()
    # create a list of node names
    map(s.add_vertex, [adj.node.name for adj in elg.adjacencies])

    for adj in elg.adjacencies:
        for successor in adj.successors:
            s.add_edge(adj.node.name,
                    successor.node.name,
                    successor.edgecap.capacity)

    print s.max_flow(network.nfi.source, network.nfi.sink)

## parseClaim : Strings 
## create a parser and returns the parsed lines
def parseClaim(lines):
    try:
        parser = Parser()
        return parser.parse(lines)[0]
    except Exception, e:        
        print("file did not accurately follow the grammar %s" % e)

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        playSciGame(sys.argv[1])
    else:
        playSciGame('./simpleClaim.txt')

