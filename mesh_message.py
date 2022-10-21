

def get_path(graph, start, end):
    return inner(graph, start, end, set())


def inner(graph, start_node, end_node, visited):
    if start_node not in graph or end_node not in graph:
        raise Exception()

    visited.add(start_node)

    if start_node == end_node:
        return [start_node]

    min_path = None
    for neighbor in graph[start_node]:
        if neighbor in visited:
            continue

        new_path = inner(graph, neighbor, end_node, visited)
        if new_path:
            new_path.insert(0, start_node)

            if not min_path or len(new_path) < len(min_path):
                min_path = new_path

    return min_path




if __name__ == "__main__":
    my_graph = {
        'a': ['b', 'c', 'd'],
        'b': ['a', 'd'],
        'c': ['a', 'e'],
        'd': ['a', 'b'],
        'e': ['c'],
        'f': ['g'],
        'g': ['f'],
    }
    print(get_path(my_graph, 'a', 'e'))
