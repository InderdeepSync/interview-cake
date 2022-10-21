class LinkedListNode(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def contains_cycle(first_node):
    seen = set()
    current = first_node
    while current:
        if current in seen:
            return True

        seen.add(current)
        current = current.next

    return False


def contains_cycle_efficient(first_node):
    slow_runner = fast_runner = first_node

    while fast_runner:
        slow_runner = slow_runner.next
        try:
            fast_runner = fast_runner.next.next
        except AttributeError as e:
            return False

        if fast_runner is slow_runner:
            return True





if __name__ == "__main__":
    fifth = LinkedListNode(5)
    fourth = LinkedListNode(4, fifth)
    third = LinkedListNode(3, fourth)
    second = LinkedListNode(2, third)
    first = LinkedListNode(1, second)
    fifth.next = third

    print(contains_cycle_efficient(first))
