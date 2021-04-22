import os
import numpy as np
import networkx as nx

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def read_panel(p):
    """
    Creates all possible digraphs with the given number of panels.
    :param p: number of panels
    :return: list with all digraphs
    """
    path = os.getcwd() + "/data/graph6/"
    f = open(path + '/Xdigraph/' + str(p) + 'digraph.txt', 'r')

    digraphs = []

    for line in f:
        exec('digraphs+=[' + line + ']')

    graph = []

    for digraph in digraphs:
        a = nx.MultiDiGraph()
        a.add_edges_from(digraph)
        graph += [a]

    f.close()

    return (graph)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello world")


