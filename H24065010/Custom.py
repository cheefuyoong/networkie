import networkx as nx
import pandas as pd
import numpy as np

class LoadFromFile(object):
    def __init__(self):
        """
        Initiate variables for the class.
        """
        self.g = nx.Graph()

        pass

    def from_edgelist(self, path):
        '''
        Read graph in edgelist txt format from `path`.

        Parameters
        ----------
        path: `str`
            The path to the edgelist text file. Note that the node index must start from 0.

        Returns
        -------
        G: `NetworkX graph`
            The parsed graph.

        '''

        edgelist = []
        with open(path, 'r') as f:
            for line in f:
                node_pair = line.replace('\n', '').split(' ')
                edgelist += [node_pair]
        self.g.add_edges_from(edgelist)
        print(nx.info(self.g))
        print('Edgelist txt data successfully loaded into a networkx Graph!')
        return self.g

    def from_in_class_network(self):  # This is Prob. 3-a.
        '''
        Parses the file to a Graph object
        --------
        Returns
        -------
        result: networkx.classes.graph.Graph
             Graph object
        '''
        df=pd.read_csv("In-class_network.txt",sep="\t")
        relation=list(df["IDs-of-acquaintances"])
        new_relation=[]
        ida=list(df["ID"])
        for i in relation:
            if len(i)>=3:
                new_relation.append(i.split(","))
            else:
                new_relation.append([i])
        self.g.add_nodes_from(ida)
        listedge=[]
        for i in range(len(ida)):
            para=[]
            for j in new_relation[i]:
                para.append((ida[i],j))
            listedge.extend(para)
        delete=[]
        for j in range(len(listedge)):
            if " " in listedge[j]:
                delete.append(listedge[j])
            
        for i in range(len(delete)):
            listedge.remove(delete[i])
            
        for i in range(len(listedge)):
            listedge[i]=(listedge[i][0],int(listedge[i][1]))
        self.g.add_edges_from(listedge)
        return self.g
