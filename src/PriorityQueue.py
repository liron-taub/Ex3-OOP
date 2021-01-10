class PriorityQueue:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        self.list.sort()
        return self.list.pop(0)

    def empty(self):
        return len(self.list) == 0
