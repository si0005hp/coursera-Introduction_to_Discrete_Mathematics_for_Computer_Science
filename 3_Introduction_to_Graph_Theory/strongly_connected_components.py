import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'

G = nx.DiGraph()
G.add_edges_from([('a', 'b'), ('b', 'c'), ('b', 'd'), ('d', 'c'), ('a', 'd'), ('e', 'd'), ('f', 'a'), ('b', 'f')])
nx.nx_agraph.view_pygraphviz(G, prog='dot')

print("Strongly connected components:")
for scc in nx.strongly_connected_components(G):
    print(scc)
