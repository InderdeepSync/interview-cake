class LinkedListNode(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_values(self):
        node = self
        values = []
        while node is not None:
            values.append(node.value)
            node = node.next
        return values


def kth_to_last_node(k, head):
    if k <= 0:
        raise Exception("k must be a non-negative integer")

    p1 = p2 = head

    for _ in range(k - 1):
        if not p2.next:
            raise Exception()

        p2 = p2.next

    while p2.next:
        p1 = p1.next
        p2 = p2.next

    return p1


if __name__ == "__main__":
    fourth = LinkedListNode(4)
    third = LinkedListNode(3, fourth)
    second = LinkedListNode(2, third)
    first = LinkedListNode(1, second)
    print(kth_to_last_node(0, first).value)
