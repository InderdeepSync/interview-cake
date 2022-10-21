
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


def find_largest(root_node):
    cur = root_node

    while cur.right:
        cur = cur.right

    return cur.value


def find_second_largest(root_node):
    prev = None
    cur = root_node

    while cur.right:
        prev = cur
        cur = cur.right

    if not prev and not cur.left:
        raise Exception("Binary Search Tree has only one element")

    return find_largest(cur.left) if cur.left else prev.value




if __name__ == "__main__":
    tree = BinaryTreeNode(50)
    left = tree.insert_left(40)
    left_left = left.insert_left(30)
    left_left_left = left_left.insert_left(20)
    left_left_left.insert_left(10)
    print(find_second_largest(tree))