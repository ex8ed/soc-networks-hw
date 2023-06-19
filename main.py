# -*- coding: UTF-8 -*-
from lib import GGenerator, Extractor

# # circulant graph
g_cir = GGenerator(13, 'circulant', 1, 3, 4)
cir = g_cir.get_ig_graph()
Extractor.plotter(cir, 'gg_cir_13', 'png')
Extractor.writer(cir, 'circulant_graph_13', 'xml')

# full graph
g_full = GGenerator(7, 'full')
full = g_full.get_ig_graph()
Extractor.plotter(full, 'gg_full_7', 'png')
Extractor.writer(full, 'full_graph_7', 'adj')

# paley-13 graph
g_paley13 = GGenerator(13, 'paley')
paley13 = g_paley13.get_ig_graph()
# Extractor.plotter(paley13, 'gg_paley13', 'pdf')
Extractor.writer(paley13, 'paley_graph_13', 'gml')

# paley-17 graph
g_paley17 = GGenerator(17, 'paley')
paley17 = g_paley17.get_ig_graph()
Extractor.plotter(paley17, 'gg_paley17', 'png')
Extractor.writer(paley17, 'paley_graph_17', 'xml')

# paley-41 graph
g_paley41 = GGenerator(41, 'paley')
paley41 = g_paley41.get_ig_graph()
Extractor.plotter(paley41, 'gg_paley_41', 'png')
