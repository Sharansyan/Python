"""@author: Sharanjit Singh"""

import networkx as nx
import matplotlib.pyplot as plt

# we can plot some random graphs
GR = nx.gnp_random_graph(50,.3)  # 5 is no. of nodes and .7 is the probabilit of edges
# printing the grapg GR
nx.draw(GR)
plt.show()