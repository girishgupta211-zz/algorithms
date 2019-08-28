# two stacks with costly enQueue()
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(item)

        while self.s2:
            self.s1.append(self.s2.pop())

    def de_queue(self):
        if len(self.s1) == 0:
            return "Q is empty"
        return self.s1.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.s1)
print(q.de_queue())
print(q.s1)
print(q.de_queue())
print(q.s1)
print(q.de_queue())
print(q.s1)
print(q.de_queue())
print(q.s1)


# two stacks with costly deQueue()
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        self.s1.append(item)

    def de_queue(self):
        if len(self.s1) == 0:
            return "Q is empty"
        while self.s1:
            self.s2.append(self.s1.pop())
        item = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return item


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.s1)
print(q.de_queue())
print(q.s1)
print(q.de_queue())
print(q.s1)
print(q.de_queue())
print(q.s1)
print(q.de_queue())
print(q.s1)
