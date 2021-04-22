import graphToolbox.core.graphtbox as gtb

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


def tests():
    #gt = nx.Graph([(0, 1), (0, 2), (0, 3), (2, 1), (3, 2)])
    gt = nx.MultiDiGraph([(0, 1, None), (0, 2, None), (0, 3, None), (2, 1, None), (3, 2, None)])
    print(gt.edges())
    print(gtb.GraphRel.relpoly_binary_basic(gt))
    print(gtb.GraphRel.relpoly_binary_improved(gt))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starting...")

    tests()
    exit()

    graph_lst = read_panel(5)
    for n_line, element in enumerate(graph_lst, start=1):
        try:
            print(element.edges())
            print("Basic: ", gtb.Utilities.polynomial2binomial(gtb.GraphRel.relpoly_binary_basic(element)))
            print("Improved: ", gtb.GraphRel.relpoly_binary_improved(element))
            print("")
        except:
            print("Error with graph at line ", n_line)
    print("Done")


