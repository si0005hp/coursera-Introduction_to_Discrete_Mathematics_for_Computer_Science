import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


G = nx.Graph()
G.add_edges_from([(1, 'b'), (1, 'c'), (1, 'd'), (2, 'a'), (2, 'c'), (2, 'e'), (3, 'b'),
                  (3, 'c'), (3, 'd'), (4, 'a'), (4, 'e'), (5, 'a'), (5, 'e')])

if nx.bipartite.is_bipartite(G):
    left, right = nx.bipartite.sets(G)
    for v in left:
        G.nodes[v]['color'] = 'blue'
    for v in right:
        G.nodes[v]['color'] = 'green'
else:
    print("This graph is not bipartite")

nx.nx_agraph.view_pygraphviz(G, prog='circo')

M = nx.max_weight_matching(G)
print(M)
for v1, v2 in M:
    G[v1][v2]['color'] = 'red'
nx.nx_agraph.view_pygraphviz(G, prog='circo')
