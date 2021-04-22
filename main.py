import os
import numpy as np
import networkx as nx

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def read_panel(p):
    """
    Creates all possible multidigraphs with the given number of panels.
    :param p: number of panels
    :return: list with all multidigraphs
    """
    path = os.getcwd() + "/data/Xdigraph/"
    f = open(path + str(p) + 'digraph.txt', 'r')

    digraphs = list()
    for line in f:
        exec('digraphs+=[' + line + ']')

    graph_lst = list()
    [graph_lst.append(nx.MultiDiGraph(digraph)) for digraph in digraphs]
    f.close()

    return (graph_lst)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starting...")
    result = read_panel(3)

    print("Done")


