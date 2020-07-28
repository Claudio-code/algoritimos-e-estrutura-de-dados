class Deque:
    def __init__(self):
        self.len = 0
        self.deque = []

    def empty(self):
        if self.len == 0:
            return True
        return False

    def push_front(self, e):
        self.deque.insert(0, e)
        self.len += 1

    def push_back(self, e):
        self.deque.insert(self.len, e);
        self.len += 1

    def pop_front(self):
        if not self.empty():
            self.deque.pop(0)
            self.len -= 1

    def pop_back(self):
        if not self.empty():
            self.deque.pop(self.len - 1)
            self.len -= 1

    def front(self):
        if not self.empty():
            return self.deque[0]

    def back(self):
        if not self.empty():
            return self.deque[-1]


deq = Deque()
deq.push_front(12)
deq.push_front(32)

print(deq.deque)
deq.pop_front()

print(deq.deque)
deq.push_front(322)
deq.push_back(1202)

print(deq.deque)
deq.pop_back()
print(deq.deque)