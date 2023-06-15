# -*- coding: UTF-8 -*-
"""Module for generating and exporting graphs"""
import igraph as ig
from typing import List
from templates import xml_node, xml_graph


class GGenerator:
    """
      Makes an ig-object with different
      graph architecture via types.
    """
    def __init__(self, n, t='full', *links):
        self.__type = t
        self.__nodes = n
        self.__links = links

    def get_ig_graph(self):
        if self.__type == 'paley':
            graph = self.__paley()
            return graph
        elif self.__type == 'circulant':
            graph = self.__circulant()
            return graph
        elif self.__type == 'full':
            graph = self.__full()
            return graph

    def get_nodes(self):
        return self.__nodes

    def __circulant(self):
        return ig.Graph(n=self.__nodes, edges=self.__calc_cir_edges())

    def __full(self):
        return ig.Graph.Full(n=self.__nodes)

    def __paley(self):
        return ig.Graph(n=self.__nodes, edges=self.__calc_paley_edges())

    def __calc_cir_edges(self) -> List:
        e = []
        for i in range(self.__nodes):
            for j in self.__links:
                e.append((i, (i + j) % self.__nodes))
        return e

    def __calc_paley_edges(self) -> List:
        # setting links:
        seq = list(range(self.__nodes))
        mod = [(i ** 2) % self.__nodes for i in seq]
        links = []
        for i, m in enumerate(mod):
            if m <= (self.__nodes - 1) / 2:
                links.append(m)
            else:
                links.append(-m)
        for i, l_ in enumerate(links):
            if l_ < 0:
                links[i] = self.__nodes + l_
        links.remove(0)

        links = list(set(links))

        e = []
        for i in range(self.__nodes):
            for j in links:
                e.append((i, (i + j) % self.__nodes))
        return e


class Extractor:
    """
      All about exporting and making files and captures with graphs
    and plotting
    """
    @classmethod
    def writer(cls, graph: ig.Graph(), name='cir', ex='gml'):
        """Exports files in different formats"""
        if ex == 'gml':
            with open(f'{name}.{ex}', 'w') as file:
                ig.Graph.write_gml(graph, file)
        elif ex == 'adj':
            with open(f'{name}.txt', 'w') as file:
                ig.Graph.write_adjacency(graph, file)
        elif ex == 'xml':
            with open(f'{name}.{ex}', 'w') as file:
                edges = graph.get_edgelist()
                data = xml_graph % ''.join(xml_node % (pair[0], pair[1]) for pair in edges)
                file.write(data)

    @classmethod
    def plotter(cls, graph: ig.Graph(),
                name='graph', ex='png',
                vertex_color="dark green",
                layout='circle',
                vertex_label_color='white'):
        ig.plot(graph, vertex_color=vertex_color,
                layout=layout,
                target=f'./img/{name}.{ex}',
                vertex_label=range(graph.vcount()),
                vertex_label_color=vertex_label_color)
