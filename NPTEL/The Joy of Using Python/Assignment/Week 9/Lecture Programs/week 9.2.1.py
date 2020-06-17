import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
l = [1,2,3,4,5,6,7,8,9,10]
G.add_nodes_from(l)

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(2,4)
G.add_edge(2,5)
G.add_edge(2,1)
G.add_edge(3,7)
G.add_edge(3,6)
G.add_edge(3,1)
G.add_edge(4,2)
G.add_edge(4,8)
G.add_edge(4,9)
G.add_edge(5,2)
G.add_edge(5,10)
G.add_edge(6,3)
G.add_edge(7,3)

nx.draw(G)
plt.show()