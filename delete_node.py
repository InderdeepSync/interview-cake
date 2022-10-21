"""
Delete a node from a singly-linked list, given only a variable pointing to that node.

"""
def delete_node(node_to_delete):
    if not node_to_delete.next:
        raise Exception()

    node_to_delete.value = node_to_delete.next.value
    node_to_delete.next = node_to_delete.next.next
