def compute_num_triangles(G):  # This is Prob. 3-e.
    '''
    Parameters
    ----------
    G: "networkx.classes.graph.Graph"
        the Graph object
    
    Returns
    -------
    result: "int"
        can form how many triangular
    '''
    def choose_2(data,i):
        result=[]
        data1=list(data[i])
        while data1:
            a = data1.pop(-1)
            for m in data1:
                result.append((a,m))
        return result

    G2=G.copy()
    graph_changed=True
    while graph_changed:
        graph_changed=False
        for nodes , degree in list(G.degree):
            if degree<2:
                G.remove_node(nodes)
                graph_changed=True

    triangle=0
    for i in list(G2):
        for j,k in choose_2(G2,i):
            if j in G2[k]:
                triangle+=1
        G2.remove_node(i)
    return triangle

import networkx as nx
import pandas as pd
import numpy as np
class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self,data):  # This is Prob. 3-d.
        '''
        Parameters
        -----------
        data: "networkx.classes.graph.Graph"
             the Graph object
        
        Returns
        -------
        result: "list"
             each nodes of the degree
        
        '''
        self.data = data
        return list(nx.degree(self.data))

