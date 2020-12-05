import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'

G = nx.Graph()
G.add_edges_from([('a', 'b'), ('t', 'c'), ('b', 'x'), ('c', 'q'), ('q', 't')])
nx.nx_agraph.view_pygraphviz(G, prog='circo')

print("G has {} connected components".format(nx.number_connected_components(G)))
for cc in nx.connected_components(G):
    print(cc)
