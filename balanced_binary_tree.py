
class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_balanced(tree_root):
    leaf_node_depths = []

    nodes_to_process = [(tree_root, 0)]
    while nodes_to_process:
        node, depth = nodes_to_process.pop()

        if not node.left and not node.right:
            leaf_node_depths.append(depth)
            continue

        if node.left:
            nodes_to_process.insert(0, (node.left, depth + 1))

        if node.right:
            nodes_to_process.insert(0, (node.right, depth + 1))


    # print(leaf_node_depths, nodes_to_process)


    leaf_node_depths.sort()

    return leaf_node_depths[-1] - leaf_node_depths[0] <= 1




if __name__ == "__main__":
    tree = BinaryTreeNode(6)
    left = tree.insert_left(1)
    right = tree.insert_right(0)
    right_right = right.insert_right(7)
    right_right.insert_right(8)
    result = is_balanced(tree)
    print(result)
