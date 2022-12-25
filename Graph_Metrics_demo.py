# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 15:00:07 2022

@author: Mriank Ghosh
"""

#Centrality is a term to describe importance of individual nodes in a graph. 
#There has been a lot of research carried out in this topic for network analysis
# to answer the question, 
#“Which are the most important nodes (vertices) in a graph?”
#list of different metrics included in our analysis:
    #Degree Centrality
    #Eigenvector Centrality
    #Katz Centrality
    #PageRank
    #HITS Hubs and Authorities
    #Closeness Centrality
    #Betweenness Centrality
==============================================================================
Imports
-----------
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
-------------------------------------------------------------
#method to draw the graph and the centrality metrics of nodes
-------------------------------------------------------------
def draw(G, pos, measures, measure_name):
    
    nodes = nx.draw_networkx_nodes(G, pos, node_size=250, cmap=plt.cm.plasma, 
                                   node_color=list(measures.values()),
                                   nodelist=measures.keys())
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1, base=10))
    # labels = nx.draw_networkx_labels(G, pos)
    edges = nx.draw_networkx_edges(G, pos)

    plt.title(measure_name)
    plt.colorbar(nodes)
    plt.axis('off')
    plt.show()
-------------------------
#Example Undirected Graph
-------------------------
G = nx.karate_club_graph()
pos = nx.spring_layout(G, seed=675)
-----------------------
#Example Directed Graph
-----------------------
DiG = nx.DiGraph()
DiG.add_edges_from([(2, 3), (3, 2), (4, 1), (4, 2), (5, 2), (5, 4),
                    (5, 6), (6, 2), (6, 5), (7, 2), (7, 5), (8, 2),
                    (8, 5), (9, 2), (9, 5), (10, 5), (11, 5)])
dpos = {1: [0.1, 0.9], 2: [0.4, 0.8], 3: [0.8, 0.9], 4: [0.15, 0.55],
        5: [0.5,  0.5], 6: [0.8,  0.5], 7: [0.22, 0.3], 8: [0.30, 0.27],
        9: [0.38, 0.24], 10: [0.7,  0.3], 11: [0.75, 0.35]}
--------------------
#Degree Distribution
--------------------
degrees = [G.degree(n) for n in G.nodes()]
plt.hist(degrees)
-------------------
#Degree Centrality
-------------------
#Degree of a node is basically number of edges that it has. The basic intuition
# is that, nodes with more connections are more influential and important in a
# network.
draw(G, pos, nx.degree_centrality(G), 'Degree Centrality')
deg_centrality = nx.degree_centrality(G)
print(deg_centrality)
for node in sorted(deg_centrality, key=deg_centrality.get, reverse=True):
  print(node, deg_centrality[node])
#For directed graphs, in-degree, number of incoming points, is considered as 
#importance factor for nodes.
--------------
#in-degree
--------------
draw(DiG, dpos, nx.in_degree_centrality(DiG), 'DiGraph Degree Centrality')
in_deg_centrality = nx.in_degree_centrality(DiG)
print(in_deg_centrality)
for node in sorted(in_deg_centrality, key=in_deg_centrality.get, reverse=True):
  print(node, in_deg_centrality[node])
------------
#out-degree
------------
draw(DiG, dpos, nx.out_degree_centrality(DiG), 'DiGraph Degree Centrality')
out_deg_centrality = nx.out_degree_centrality(DiG)
print(out_deg_centrality)
for node in sorted(out_deg_centrality, key=out_deg_centrality.get, reverse=True):
  print(node, out_deg_centrality[node])
-----------------------
#Eigenvector Centrality
-----------------------
#Eigenvector centrality is a basic extension of degree centrality, which 
#defines centrality of a node as proportional to its neighbors’ importance. 
draw(G, pos, nx.eigenvector_centrality(G), 'Eigenvector Centrality')
eig_centrality = nx.eigenvector_centrality(G)
print(eig_centrality)
for node in sorted(eig_centrality, key=eig_centrality.get, reverse=True):
  print(node, eig_centrality[node])
-------------------
#Katz Centrality
-------------------
#Katz centrality introduces two positive constants 
#α and β
#to tackle the problem of eigenvector centrality with zero in-degree nodes:
draw(DiG, dpos, nx.katz_centrality(DiG, alpha=0.1, beta=1.0), 'DiGraph Katz Centrality')
katz_centrality = nx.katz_centrality(DiG, alpha=0.1, beta=1.0)
print(katz_centrality)
for node in sorted(katz_centrality, key=katz_centrality.get, reverse=True):
  print(node, katz_centrality[node])
#Although this method is introduced as a solution for directed graphs, 
#it can be useful for some applications of undirected graphs as well.
draw(G, pos, nx.katz_centrality(G, alpha=0.1, beta=1.0), 'Katz Centrality')
---------
#PageRank
--------
#PageRank was introduced by the founders of Google to rank websites in search 
#results. It can be considered as an extension of Katz centrality.
draw(DiG, dpos, nx.pagerank(DiG, alpha=0.85), 'DiGraph PageRank')
page_rank = nx.pagerank(DiG, alpha=0.85)
print(page_rank)
for node in sorted(page_rank, key=page_rank.get, reverse=True):
  print(node, page_rank[node])
--------------------------
#HITS Hubs and Authorities
--------------------------
#Up until this point, we have discussed the measures that captures high node 
#centrality, however, there can be nodes in the network which are important 
#for the network, but they are not central.
h,a = nx.hits(DiG)
draw(DiG, dpos, h, 'DiGraph HITS Hubs')
draw(DiG, dpos, a, 'DiGraph HITS Authorities')
---------------------
#Closeness Centrality
---------------------
#Closeness Centrality is a self-explanatory measure where each node’s 
#importance is determined by closeness to all other nodes.
draw(G, pos, nx.closeness_centrality(G), 'Closeness Centrality')
closeness_centrality = nx.closeness_centrality(G)
print(closeness_centrality)
for node in sorted(closeness_centrality, key=closeness_centrality.get, reverse=True):
  print(node, closeness_centrality[node])
-----------------------
#Betweenness Centrality
-----------------------
#Betweenness Centrality is another centrality that is based on shortest 
#path between nodes. It is determined as number of the shortest paths passing
# by the given node. 
draw(G, pos, nx.betweenness_centrality(G), 'Betweenness Centrality')
betweenness_centrality = nx.betweenness_centrality(G)
print(betweenness_centrality)
for node in sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True):
  print(node, betweenness_centrality[node])
--------------------------------------------