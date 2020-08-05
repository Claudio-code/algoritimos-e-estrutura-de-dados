from listaEncadeada.Node import Node

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.lengthList = 0

    def length(self):
        return self.lengthList

    def show(self):
        currentNode = self.first
        while currentNode != None:
            print(currentNode.getLabel(), end=' ')
            currentNode = currentNode.getNext()
        print('')

    def empty(self):
        if self.first is None:
            return True
        return False

    def pop(self, index):
        if not self.empty() and index >= 0 and index < self.lengthList:
            flagRemove = False
            if self.first.getNext() == None:
                # tem apenas um elemento
                self.first = None
                self.last = None
                flagRemove = True

            elif index == 0:
                # remove do inicio mais com mais de um elemento
                nextNode = self.first.getNext()
                self.first = nextNode
                flagRemove = True

            else:
                # remove do meio da lista
                preventNode = self.first
                currentNode = self.first.getNext()
                currentIndex = 1

                while currentNode != None:
                    if currentIndex == index:
                        # o proximo do anterior aponta para o proximo do nó corrente
                        preventNode.setNext(currentNode.getNext())
                        currentNode.setNext(None)
                        flagRemove = True
                        break

                    preventNode = currentNode
                    currentNode = preventNode.getNext()
                    currentIndex += 1

        if flagRemove:
            self.lengthList -= 1

        return flagRemove

    def push(self, label, index):
        if index >= 0:
            node = Node(label)

            if self.empty():
                self.first = node
                self.last = node
            else:
                #inserindo no inicio
                if index == 0:
                    node.setNext(self.first)
                    self.first = node
                #inserindo no fim
                elif index >= self.lengthList:
                    self.last.setNext(node)
                    self.last = node
                else:
                    #inserindo no meio pegando o anterior eo proximo nó
                    preventNode = self.first
                    currentNode = self.first.getNext()
                    currentIndex = 1

                    while currentNode != None:
                        if currentIndex == index:
                            # seta o currentNode como o proximo do nó
                            node.setNext(currentNode)

                            # seta o node como o proximo do preventNode do no anterior
                            preventNode.setNext(node)
                            break

                        preventNode = currentNode
                        currentNode = currentNode.getNext()
                        currentIndex += 1

            # atualizo o tamanho da lista
            self.lengthList += 1


lista = LinkedList()
lista.push('carlos', 0)
lista.show()
lista.push('maria', 1)
lista.show()
lista.push('antonio', 0)
lista.show()
lista.push('keven', lista.length())
lista.show()
lista.push('vitoria', lista.length() - 2)
lista.show()

lista.pop(0)
lista.show()
lista.pop(lista.length() - 1)
lista.show()
lista.pop(1)
lista.show()