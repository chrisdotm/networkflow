#!/usr/bin/env python
from parser import Parser
from proposer import Proposer
from adjacency import Adjacency
from edgelabeledgraph import EdgeLabeledGraph
from networkflowinstance import NetworkFlowInstance
from flow import Flow
from node import Node
from nodeandlabel import NodeAndLabel

import fulkerson_solver
import sys


## opens the given claims file, parses it, and refutes or supports the claims 
def playSciGame(file_path):
    claims_file = open(file_path)
    lines = ' '.join(claims_file.readlines())
    claims_file.close()

    claim = parseClaim(lines)
    elg = claim.nfi.elg

    flowNetwork = fulkerson_solver.FlowNetwork()
    # create a list of node names
    map(flowNetwork.add_vertex, [adj.node.name for adj in elg.adjacencies])
#    print flowNetwork.adj
    for adj in elg.adjacencies:
        for successor in adj.successors:
            flowNetwork.add_edge(adj.node.name,
                    successor.node.name,
                    successor.edgecap.capacity)
    source = claim.nfi.source.name
    sink   = claim.nfi.sink.name
    maxFlow = flowNetwork.max_flow(source,sink)
    if (maxFlow  == claim.quality):
        print "Claim %s supported!" % claim.claim_name
    else:
        print "Claim refuted! \nCounter Proposal:"
        print  maxFlow



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

