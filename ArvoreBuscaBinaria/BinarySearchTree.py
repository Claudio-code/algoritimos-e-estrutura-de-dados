from ArvoreBuscaBinaria.Node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def empty(self):
        if self.root == None:
            return True
        return False

    #mostra em pre-ordem (raiz-esq-dir)
    def show(self, curr_node):
        if curr_node != None:
            print('%d' % curr_node.getLabel(), end=' ')
            self.show(curr_node.getLeft())
            self.show(curr_node.getRight())

    def getRoot(self):
        return self.root

    def insert(self, label):
        node = Node(label)

        # verifica se arvore ta vazia
        if self.empty():
            self.root = node

        else:
            # se n tiver vazia
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node != None:
                    dad_node = curr_node

                    # ver se vai para esquerda ou direita
                    if node.getLabel() < curr_node.getLabel():
                        #vai para esquerda
                        curr_node = curr_node.getLeft()
                    else:
                        # vai para direita
                        curr_node = curr_node.getRight()
                else:
                    # se curr_node é none, então encontrou onde inserir
                    if node.getLabel() < dad_node.getLabel():
                        dad_node.setLeft(node)
                    else:
                        dad_node.setRight(node)

                    break # sai do loop


arvore = BinarySearchTree()

arvore.insert(8)
arvore.insert(3)
arvore.insert(1)
arvore.insert(6)
arvore.insert(4)
arvore.insert(7)
arvore.insert(10)
arvore.insert(14)
arvore.insert(13)

arvore.show(arvore.root)