import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'

G = nx.DiGraph()
G.add_edges_from([('a', 'b'), ('b', 'c'), ('b', 'd'), ('d', 'c'), ('a', 'd')])
nx.nx_agraph.view_pygraphviz(G, prog='circo')

if nx.is_directed_acyclic_graph(G):
    print("Topological ordering of the nodes:", list(nx.topological_sort(G)))
else:
    print("G contains a cycle, hence it cannot be topologically sorted.")

nx.nx_agraph.view_pygraphviz(G, prog='dot')
