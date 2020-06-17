''' @author: Sharanjit Singh '''

import networkx as nx
import matplotlib.pyplot as plt

# METHOD 1
# Creating an emplty graph
G = nx.Graph()
# creating nodes in the graph
G.add_node(1)
G.add_node(2)
G.add_node(3) 
'''
(this is another method of creating nodes)
l = [1,2,3]
G.add_nodes_from(l)
'''
# adding edges to the nodes (or connecting nodes together)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,1)
# printing the values of nodes and edges 
print(G.nodes())
print('\n')
print(G.edges())
# printing the graph
nx.draw(G)
plt.show()


# METHOD 2
# networkx comes with some pre-defined graphs
GC = nx.complete_graph(5)  # 5 is no. of nodes
# printing the graph G
nx.draw(GC)
plt.show()


# METHOD 3
# we can plot some random graphs
GR = nx.gnp_random_graph(5,.7)  # 5 is no. of nodes and .7 is the probabilit of edges
# printing the grapg GR
nx.draw(GR)
plt.show()