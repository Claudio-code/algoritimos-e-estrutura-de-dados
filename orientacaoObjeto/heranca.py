class Transporte:
    def __init__(self, nome, peso, preco):
        self.nome = nome
        self.peso = peso
        self.preco = preco
    
    def getNome(self):
        return self.nome

    def getPeso(self):
        return self.peso

    def getPreco(self):
        return self.preco


class Carro(Transporte): 

    def __init__(self, nome, peso, preco, preco_seguro):
        Transporte.__init__(self, nome, peso, preco)
        self.preco_seguro = preco_seguro


meuCarro = Carro('corsa', 121, 2122.2, 11221.2)
print(meuCarro.getPeso())