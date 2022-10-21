
import math

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




def is_binary_search_tree(root, upper=math.inf, lower=-math.inf):
    left_valid = (lower < root.left.value < min(root.value, upper)) and is_binary_search_tree(root.left,
                                                                                              upper=root.value,
                                                                                              lower=lower) if root.left else True
    right_valid = (upper > root.right.value > max(root.value, lower)) and is_binary_search_tree(root.right,
                                                                                                lower=root.value,
                                                                                                upper=upper) if root.right else True

    return left_valid and right_valid


if __name__ == "__main__":
    tree = BinaryTreeNode(50)
    left = tree.insert_left(30)
    right = tree.insert_right(80)
    left.insert_left(20)
    left.insert_right(60)
    right.insert_left(70)
    right.insert_right(90)
    result = is_binary_search_tree(tree)

    print(result)
