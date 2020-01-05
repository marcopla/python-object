
class Programa:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.ano = ano
        self.__likes = 0
        self.__duracao = duracao

    @property
    def nome(self):
        return self.__nome
        

    @property
    def likes(self):
        return self.__likes
    
    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self, nova_duracao):
        self.__duracao = nova_duracao

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def ano(self):
        return self.ano

    @ano.setter
    def ano(self, novo_ano):
        self.ano = novo_ano

    def dar_likes(self):
        self.__likes += 1

vingadores = Programa('vingadores a era ultron', 10, 180)

print(f'Nome: {vingadores.nome} '
      f'Ano: {vingadores.ano} '  
      f'Duração: {vingadores.duracao}'
      f'Likes: {vingadores.likes}.')