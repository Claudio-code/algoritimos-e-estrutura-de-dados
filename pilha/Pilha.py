class Pilha: # stack
    def __init__(self):
        self.pilha = []

    def push(self, item):
        self.pilha.append(item)

    def pop(self):
        if not self.empty():
            self.pilha.pop(len(self.pilha) - 1)
        return None

    def top(self):
        if not self.empty():
            return self.pilha[-1]
        return None

    def empty(self):
        if (len(self.pilha) == 0):
            return True
        return False

    def length(self):
        return len(self.pilha)

pilha = Pilha()

pilha.push(1)
pilha.push(2)
pilha.push(3)

pilha.pop()

print(pilha.empty())
print(pilha.top())

pilha.pop()
pilha.pop()

print(pilha.empty())