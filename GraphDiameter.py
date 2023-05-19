#Gennerate directed graph with A->B, A->I, A->D,C->B,C->D,D->A,D->E,D->J,E->D,E->F,G->E,F->H,H->F,H->G,J->D,J->G,J->I,I->H 
#Plot the graph with networkx and matplotlib
#diplay the diameter of the graph
#display shortest path between A and F
#display average shortest path form A to all other nodes



import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([('A','B'),('A','I'),('A','D'),('C','B'),('C','D'),('D','A'),('D','E'),('D','J'),('E','D'),('E','F'),('G','E'),('F','H'),('H','F'),('H','G'),('J','D'),('J','G'),('J','I'),('I','H')])
nx.draw(G, with_labels=True)
plt.show()

#print("Diameter of the graph is: ",nx.diameter(G))
print("Shortest path between A and F is: ",nx.shortest_path(G,'A','F'))
#print("Average shortest path from A to all other nodes is: ",nx.average_shortest_path_length(G,'A'))




