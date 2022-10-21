class LinkedListNode(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(head):
    prev = None
    current = head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev

