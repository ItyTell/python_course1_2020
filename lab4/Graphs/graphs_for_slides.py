import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import pathlib
import math
from collections import namedtuple

__all__ = ['ROOT', "ARROWS", 'LABELS', 'NODES', 'EDGES', 'COLORS', 'BLACK', 'IZO', 'BB',
           'circle_n', 'line_n']

ROOT = pathlib.Path(r'D:\Courses\Programming\Prog2020\Pictures\graphs')
ARROWS = {'arrowsize': 20, 'arrowstyle': ptch.ArrowStyle.CurveB(head_length=0.6, head_width=0.3)}
LABELS = {'font_color': 'black', 'font_size': 22}
NODES = {'edgecolors': 'black', 'node_color': 'white', 'node_size': 800}
EDGES = {'edge_color': 'black', 'width': 2.5}
COLORS = NODES | EDGES | {'with_labels': True} | LABELS | ARROWS
BLACK = {'node_color': 'black', 'node_size': 250, 'width': 2.5, 'with_labels': False} | ARROWS
BB = {'font_size': 18, 'node_size': 700}


def circle_n(n):
    fi = math.pi / n * 2
    return {i: np.array((math.cos(i * fi + math.pi * 0.5), math.sin(i * fi + math.pi * 0.5))) for i in range(n)}


def line_n(n):
    return {i: np.array((i, 0)) for i in range(n)}


def lay_petersen():
    lay = circle_n(5)
    return lay | {i + 5: lay[i] * 0.5 for i in range(5)}


def k_3_3_layout():
    g = nx.complete_bipartite_graph(3, 3)
    return nx.bipartite_layout(g, (v for v, prop in g.nodes('bipartite') if prop == 0),
                               align='horizontal')


def draw(graphs, root, param):
    for g in graphs:
        nx.draw(g.g, pos=g.layout, **param)
        plt.savefig(root.joinpath(g.fname))
        plt.clf()


def draw_equal(graphs, root, param):
    for g in graphs:
        ax = plt.axes()
        ax.set_xmargin(0.1)
        ax.set_ymargin(0.1)
        ax.set_aspect('equal', adjustable='datalim')
        nx.draw(g.g, pos=g.layout, **param)
        plt.savefig(root.joinpath(g.fname))
        plt.clf()


IZO = namedtuple('IZO', ('g', 'fname', 'layout'))

SPECIAL = [IZO(nx.empty_graph(5), 'empty_5.png', line_n(5)),
           IZO(nx.path_graph(5), 'P_5.png', line_n(5)),
           IZO(nx.cycle_graph(5), 'C_5.png', circle_n(5)),
           IZO(nx.complete_graph(5), 'K_5.png', circle_n(5)),
           IZO((g := nx.complete_bipartite_graph(3, 3)), 'K_3_3.png', k_3_3_layout()),
           IZO((g := nx.complete_bipartite_graph(3, 5)), 'K_3_5.png',
               nx.bipartite_layout(g, (v for v, prop in g.nodes('bipartite') if prop == 0),
                                   align='horizontal')),
           IZO(nx.petersen_graph(), 'petersen.png', lay_petersen()),

           ]


def k_3_3_edge():
    g = nx.complete_bipartite_graph(3, 3)
    g.remove_edge(1, 4)
    return g


def k_3_3_node():
    g = nx.complete_bipartite_graph(3, 3)
    g.remove_node(4)
    return g


OPERATIONS = [
    IZO((g := nx.cycle_graph(4)), 'C_4_.png', c4_lay := nx.shell_layout(g)),
    IZO((g := nx.complete_graph(3)), 'K_3_.png', k3_lay := nx.shell_layout(g)),
    IZO((g := nx.compose(nx.complete_graph(3), nx.cycle_graph(4))), 'K3_C4_.png', nx.shell_layout(g)),
    IZO((g := nx.disjoint_union(nx.complete_graph(3), nx.cycle_graph(4))), 'K3_u_C4_.png',
        k3_lay | {i + 3: c4_lay[i] + (2.0, 0.0) for i in c4_lay}),
    IZO((g := nx.complement(nx.cycle_graph(4))), 'C_C_4_.png', nx.shell_layout(g)),
    IZO(k_3_3_edge(), 'K_3_3_edge_.png', k_3_3_layout()),
    IZO(k_3_3_node(), 'K_3_3_node_.png', k_3_3_layout()),
]


def K_2_xn_layout(n):
    pos = {2 * i: np.array((i, 0)) for i in range(n)}
    pos |= {2 * i + 1: pos[2 * i] + (0.0, 1.0) for i in range(n)}
    return pos


def nodes_edges(root, param):
    g = nx.complete_bipartite_graph(3, 5)
    lay = nx.bipartite_layout(g, (v for v, prop in g.nodes('bipartite') if prop == 0),
                              align='horizontal')
    nx.draw(g, pos=lay, **param)
    plt.savefig(root.joinpath('K_3_5_.png'))
    plt.clf()

    g = nx.Graph()
    n = iter(range(10))
    g.add_edges_from(zip(n, n))
    pos = K_2_xn_layout(5)
    ax = plt.axes()
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_ymargin(0.2)
    nx.draw(g, pos=pos, **param)
    tmp1 = ax.get_xlim()
    tmp2 = ax.get_ylim()
    plt.savefig(root.joinpath('g1.png'))
    plt.clf()

    ax = plt.axes()
    ax.set_aspect('equal', )
    ax.set_xlim(tmp1)
    ax.set_ylim(tmp2)
    ax.set_ymargin(0.1)
    nx.draw(g.subgraph({8, 9}), pos=pos, **param)
    plt.savefig(root.joinpath('g2.png'))
    plt.clf()

    g = nx.Graph()
    nx.add_star(g, range(4))
    nx.add_cycle(g, range(4, 10))
    nx.add_path(g, range(10, 13))
    p1 = circle_n(6)
    p2 = line_n(4)
    pos = {0: (0, 1)} | {i: (i - 2, -1) for i in range(1, 4)} \
          | {i + 4: p1[i] * 1.5 + (3.5, 0) for i in p1} \
          | {i + 10: p2[i] * 1.5 + (6, 0) for i in p2}
    plt.axes().set_aspect('equal', adjustable='datalim')
    nx.draw(g, pos=pos, **param)
    plt.savefig(root.joinpath('g3.png'))
    plt.clf()


def graph_types(root, param):
    g = nx.DiGraph()
    g.add_edges_from([(1, 2), (2, 1), (2, 3), (4, 3)])
    nx.draw(g, pos=line_n(5), **param)
    plt.savefig(root.joinpath('g4.png'))
    plt.clf()

    g = nx.Graph()
    g.add_edge(1, 2, weight=3, color='red')
    g.add_edge(3, 2, weight=1, color='blue')
    g.add_edge(3, 1, color='green')
    g[1][2]['weight'] = 5
    colors = [color for a, b, color in g.edges.data(data='color', default='black')]
    nx.draw_shell(g, with_labels=True, font_color='white', font_weight='bold',
                  node_color=['red', 'green', 'blue'],
                  edge_color=colors,
                  node_size=param.get('node_size', 50),
                  font_size=param.get('font_size', 20))
    plt.savefig(root.joinpath('g5.png'))
    plt.clf()


def digraphs(root):
    g = nx.DiGraph()
    set1 = [(2, 3), (4, 3)]
    set2 = [(1, 2), (2, 1)]
    g.add_edges_from(set1)
    g.add_edges_from(set2)

    plt.axis('off')
    nx.draw_networkx_nodes(g, pos=line_n(5), **NODES)
    nx.draw_networkx_labels(g, pos=line_n(5), **LABELS)
    nx.draw_networkx_edges(g, pos=line_n(5), edgelist=set1, **(EDGES | ARROWS))
    nx.draw_networkx_edges(g, pos=line_n(5), edgelist=set2, connectionstyle="arc3,rad=0.25", **(EDGES | ARROWS));
    plt.savefig(root.joinpath('g6.png'))
    plt.clf()

    g = nx.DiGraph()
    g.add_edges_from([(0, 1), (1, 0), (1, 2), (3, 0), (3, 2)])
    lay = circle_n(4)

    plt.axis('off')
    nx.draw_networkx_nodes(g, pos=lay, **NODES)
    nx.draw_networkx_labels(g, pos=lay, **LABELS)
    nx.draw_networkx_edges(g, pos=lay, edgelist=[(a, b) for a, b in g.edges if a + b > 1], **(EDGES | ARROWS))
    nx.draw_networkx_edges(g, pos=lay, edgelist=[(a, b) for a, b in g.edges if a + b <= 1],
                           connectionstyle="arc3,rad=0.25", **(EDGES | ARROWS))
    plt.savefig(root.joinpath('g7.png'))
    plt.clf()


def _save_draw_i(root, i):
    plt.savefig(root.joinpath(f'draw{i}.png'))
    plt.clf()
    return i + 1


def draw_simple(root):
    i = 0
    g = nx.complete_bipartite_graph(3, 3)
    nx.draw_shell(g)
    i = _save_draw_i(root, i)

    nx.draw_shell(g, with_labels=True, font_weight='bold', font_color='white')
    i = _save_draw_i(root, i)

    nx.draw_shell(g, node_color='black', node_size=50, width=1.5)
    i = _save_draw_i(root, i)

    nx.draw(g, pos=nx.bipartite_layout(g, (v for v, prop in g.nodes('bipartite') if prop == 0)),
            node_color='black', node_size=50, width=1.5)
    i = _save_draw_i(root, i)

    nx.draw(g, pos=nx.bipartite_layout(g, (v for v, prop in g.nodes('bipartite') if prop == 0), align='horizontal'),
            node_color='black', node_size=50, width=1.5)
    i = _save_draw_i(root, i)

    g = nx.complete_graph(4)
    nx.draw(g, node_color='black', node_size=50, width=1.5)
    i = _save_draw_i(root, i)

    nx.draw_shell(g, node_color='black', node_size=50, width=1.5)
    i = _save_draw_i(root, i)

    nx.draw_planar(g, node_color='black', node_size=50, width=1.5)
    i = _save_draw_i(root, i)

    g = nx.cycle_graph(5)
    nx.draw_shell(g, with_labels=True, font_weight='bold', font_color='white')
    i = _save_draw_i(root, i)

    plt.axes().set_aspect('equal', adjustable='datalim')
    nx.draw_shell(g, with_labels=True, font_weight='bold', font_color='white')
    i = _save_draw_i(root, i)

    g = nx.cycle_graph(5)
    plt.axes().set_aspect('equal', adjustable='datalim')
    nx.draw(g, pos=nx.shell_layout(g, rotate=math.pi / 2), with_labels=True, font_weight='bold', font_color='white')
    i = _save_draw_i(root, i)

    g = nx.petersen_graph()
    lay = nx.shell_layout(g, nlist=[range(5, 10), range(0, 5)])
    plt.axes().set_aspect('equal', adjustable='datalim')
    nx.draw(g, pos=lay, with_labels=True, font_weight='bold', font_color='white')
    i = _save_draw_i(root, i)

    lay = nx.shell_layout(g, nlist=[range(5, 10), range(0, 5)], rotate=0)
    plt.axes().set_aspect('equal', adjustable='datalim')
    nx.draw(g, pos=lay, with_labels=True, font_weight='bold', font_color='white')
    i = _save_draw_i(root, i)

    g = nx.cycle_graph(5)
    plt.axes().set_aspect('equal', adjustable='datalim')
    nx.draw(g, pos=circle_n(5), with_labels=True, font_weight='bold', font_color='white')
    i = _save_draw_i(root, i)

    g = nx.petersen_graph()
    plt.axes().set_aspect('equal', adjustable='datalim')
    nx.draw(g, pos=lay_petersen(), with_labels=True, font_weight='bold', font_color='white')
    i = _save_draw_i(root, i)


if __name__ == '__main__':
    pass
    # draw(SPECIAL, ROOT, BLACK)
    # nodes_edges(ROOT, COLORS)
    # draw_simple(ROOT)
    # draw_equal(OPERATIONS, ROOT, COLORS)
    # graph_types(ROOT, COLORS)
    # digraphs(ROOT)
