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

    def remove(self, label):
        """
            casos de uso da remoçãop

            1 caso
                o nó a ser removido não tem filhos
                esses caso é simples, basta setar a ligação do pai para none

            2 caso
                o nó a ser removido tem somente 1 filho basta colocar
                o seu filho no lugar dele

            3 caso
                o nó a ser removido possui dois filhos basta pegar o menor
                elemento da subárvore á direita
        """
        parent_node = None
        curr_node = self.root

        while curr_node != None:
            # verifica se encontrou o nó pra remover
            if label == curr_node.getLabel():

                # caso 1 nó sem filho
                if curr_node.getLeft() == None and curr_node.getRight() == None:

                    # verifica se é a raiz
                    if parent_node == None:
                        self.root = None
                    else:

                        # verifica se é filho á esquerda ou a direita
                        if parent_node.getLeft() == curr_node:
                            parent_node.setLeft(None)
                        elif parent_node.getRight() == curr_node:
                            parent_node.setRight(None)

                # caso 2 com um filho
                elif (curr_node.getLeft() == None and curr_node.getRight() != None) or \
                        (curr_node.getLeft() != None and curr_node.getRight() == None):

                    # verifica se ta no nó raiz
                    if parent_node == None:

                        # verifica se o filho de curr_node é filho a esquerda
                        if curr_node.getLeft() != None:
                            self.root = curr_node.getLeft()
                        else:  # senão o filho de curr_node é filho à direita
                            self.root = curr_node.getRight()
                    else:

                        # verifica se o filho de curr_node é filho á esquerda
                        if curr_node.getLeft() != None:

                            # verifica se curr_node é filho a esquerda
                            if parent_node.getLeft() and (parent_node.getLeft().getLabel() == curr_node.getLabel()):
                                parent_node.setLeft(curr_node.getLeft())
                            else:
                                parent_node.setRight(curr_node.getLeft())
                        else:

                            # senão curr_node é filho a direita
                            # verificando se curr_node é filho a esquerda

                            if parent_node.getLeft() and (parent_node.getLeft().getLabel() == curr_node.getLabel()):
                                parent_node.setLeft(curr_node.getRight())
                            else:
                                parent_node.setRight(curr_node.getRight())

                # caso 3: o nó  a ser removido tem dois filhos
                # pega-se o menor elemento da sub-arvore á direita
                elif curr_node.getLeft() != None and curr_node.getRight() != None:
                    dad_smaller_node = curr_node
                    smaller_node = curr_node.getRight()
                    next_smaller = curr_node.getRight().getLeft()

                    while next_smaller != None:
                        dad_smaller_node = smaller_node
                        smaller_node = next_smaller
                        next_smaller = smaller_node.getLeft()

                    # verifica se o nó a ser removido é a raiz
                    if parent_node == None:

                        # caso especial o nó que vai ser a nova raiz é filho da raiz
                        if self.root.getRight().getLabel() == smaller_node.getLabel():
                            smaller_node.setLeft(self.root.getLeft())
                        else:
                            '''
                                verifica se o smaller_node é filho á direita ou á esquerda
                                para setar para none o smaller_node
                            '''
                            if dad_smaller_node.getLeft() and \
                                (dad_smaller_node.getLeft().getLabel() == smaller_node.getLabel()):
                                dad_smaller_node.setLeft(None)
                            else:
                                dad_smaller_node.setRight(None)

                            # seta os filhos á direita e esquerda de smaller_node
                            smaller_node.setLeft(curr_node.getLeft())
                            smaller_node.setRight(curr_node.getRight())

                        # faz com que o smaller_node seja a raiz
                        self.root = smaller_node
                    else:
                        """
                            verificar se curr_node é filho a esquerda
                            ou á direita para setar o smaller_node como filho do pai do
                            curr_node (dad_node)
                        """
                        if parent_node.getLeft() and parent_node.getLeft().getLabel() == curr_node.getLabel():
                            parent_node.setLeft(smaller_node)
                        else:
                            parent_node.setRight(smaller_node)

                        """
                            verifica se o smaller_node é filho á esquerda ou á direita 
                            para setar para none o smaller_node
                        """
                        if dad_smaller_node.getLeft() and \
                            (dad_smaller_node.getLeft().getLabel() == smaller_node.getLabel()):
                            dad_smaller_node.setLeft(None)
                        else:
                            dad_smaller_node.setRight(None)

                        # seta os filhos á direita e esquerda de smaller_node
                        smaller_node.setLeft(curr_node.getLeft())
                        smaller_node.setRight(curr_node.getRight())

                break # sai do loop

            parent_node = curr_node

            # verifica se vai para esquerda
            if label < curr_node.getLabel():
                # vai para a esquerda
                curr_node = curr_node.getLeft()
            else:
                # vai para direita
                curr_node = curr_node.getRight()





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

arvore.remove(8)

arvore.show(arvore.root)