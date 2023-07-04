# Gennerate directed graph with A->B, A->I, A->D,C->B,C->D,D->A,D->E,D->J,E->D,E->F,G->E,F->H,H->F,H->G,J->D,J->G,J->I,I->H 
# Reduce the graph to left only the node that can reach any other node
# Plot the graph with networkx and matplotlib
# diplay the diameter of the graph
# display shortest path between A and F
# display average shortest path form A to all other nodes

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([('A', 'B'), ('A','I'),('A','D'),('C','B'),('C','D'),('D','A'),('D','E'),('D','J'),('E','D'),('E','F'),('G','E'),('F','H'),('H','F'),('H','G'),('J','D'),('J','G'),('J','I'),('I','H')])

#make a list remove1 of all nodes that only point to other nodes
remove1 = []
for node in G.nodes():
    if G.out_degree(node) == 0:
        remove1.append(node)
print(remove1)

#make a list remove2 of all nodes that point by other nodes
remove2 = []
for node in G.nodes():
    if G.in_degree(node) == 0:
        remove2.append(node)
print(remove2)


G.remove_nodes_from(remove1)
G.remove_nodes_from(remove2)

nx.draw(G, with_labels=True)
plt.show()

print("Diameter of the graph is: ",nx.diameter(G))
print("Shortest path between A and F is: ",nx.shortest_path(G,'A','F'))

# funtion to print the shortest path given a node to all other nodes and its length and the average shortest path from A to all other nodes


def printShortestPath(xnode):
    sumAvr = 0
    for node in G.nodes():
        print("Shortest path between ", xnode, " and ", node, " is: ", nx.shortest_path(G, xnode, node), " and its length is: ",nx.shortest_path_length(G,xnode,node))
        sumAvr += nx.shortest_path_length(G,xnode,node)
    print("Average shortest path from ",xnode," to all other nodes is: ",sumAvr/(len(G.nodes())-1))
    print("-------------------------------------------")

#printShortestPath('A')
#printShortestPath('D')
#printShortestPath('E')
#printShortestPath('F')
#printShortestPath('G')
#printShortestPath('H')
#printShortestPath('I')
#printShortestPath('J')

#function to find the list of node name that have the less  average shortest path to all other nodes from graph G
def findMinAvrShortestPath():
    minAvr = 100
    minNode = []
    for node in G.nodes():
        sumAvr = 0
        for node2 in G.nodes():
            sumAvr += nx.shortest_path_length(G,node,node2)
        if sumAvr/(len(G.nodes())-1) < minAvr:
            minAvr = sumAvr/(len(G.nodes())-1)
            minNode = []
            minNode.append(node)
        elif sumAvr/(len(G.nodes())-1) == minAvr:
            minNode.append(node)
    return minNode

print("The list of node name that have the less  average shortest path to all other nodes from graph G is: ",findMinAvrShortestPath())
