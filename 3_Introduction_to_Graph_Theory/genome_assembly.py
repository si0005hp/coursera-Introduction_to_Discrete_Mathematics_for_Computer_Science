import random
import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


def random_dna():
    return ''.join((random.choice('agct') for _ in range(3)))


attempt_counts = 10000
for _ in range(attempt_counts):
    dnas = (random_dna() for _ in range(8))
    G = nx.DiGraph(((dna[0:2], dna[1:3]) for dna in dnas))

    if nx.has_eulerian_path(G):
        nx.nx_agraph.view_pygraphviz(G, prog='circo')
        break
