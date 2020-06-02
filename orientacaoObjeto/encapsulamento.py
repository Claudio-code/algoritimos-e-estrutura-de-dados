class Pessoa:
    def __init__(self, nome):
        self.__nome = nome # <<-- declaração de atributos privados

    @property # <<== getter do atributo nome
    def nome(self):
        return self.__nome
    
    @nome.setter # <<== setter do atributo nome
    def nome(self, nome):
        self.__nome = nome

    # def getNome(self): # <<-- gjeito errado de se fazer
    #     return self.__nome

kraudio = Pessoa('kraudio')
kraudio.nome = 'carlos'

print(kraudio.nome)