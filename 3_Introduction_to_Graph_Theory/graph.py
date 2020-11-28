import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'

G = nx.DiGraph()
G.add_edge("a", "b")
G.add_edge("b", "c")
G.add_edge("c", "d")
G.add_edge("d", "e")
G.add_edge("e", "c")
G.add_edge("a", "d")

# draw(G, layout='circo')
nx.nx_agraph.view_pygraphviz(G, prog='circo')

print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))
