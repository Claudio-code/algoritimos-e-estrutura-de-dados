class Fila:
    def __init__(self):
        self.fila = []
        self.len_fila = 0

    def push(self, value):
        self.fila.append(value)
        self.len_fila += 1

    def empty(self):
        if self.len_fila == 0:
            return True
        return False

    def pop(self):
        if not self.empty():
            self.fila.pop(0)

    def length(self):
        return self.len_fila

    def front(self):
        if not self.empty():
            return self.fila[0]
        return None


fila1 = Fila()

fila1.push(12)
fila1.push(122)
fila1.push("casa")

print(fila1.front())

fila1.pop()

print(fila1.fila)