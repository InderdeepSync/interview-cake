import math


class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


def color_graph(graph, colors):
    max_degree = -math.inf
    for node in graph:
        if node in node.neighbors:
            raise Exception("Loop Detected!")

        max_degree = max(max_degree, len(node.neighbors))

    allowed_colors = {}
    for node in graph:
        allowed_colors[node.label] = colors[:max_degree + 1][:]

    for index, node in enumerate(graph):
        node.color = allowed_colors[node.label].pop()

        for neighbor in node.neighbors:
            try:
                allowed_colors[neighbor.label].remove(node.color)
            except:
                pass
