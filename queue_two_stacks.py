

class QueueTwoStacks(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        # list.append is serving the purpose of stack.push
        self.stack1.append(item)

    def dequeue(self):
        if self.stack2:
            return self.stack2.pop()

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

