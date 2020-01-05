class Programa:

	def __init__(self, nome, ano):
		self._nome = nome.title()
		self.ano = ano
		self._likes = 0 
	
	def __str__(self):
	    return f'{self._nome} - {self.ano} - {self.likes} Likes' 

	@property
	def nome(self):
	    return self._nome

	@nome.setter
	def nome(self, novo_nome):
		self._nome = novo_nome

	@property
	def likes(self):
		return self._likes

	def dar_like(self):
		self._likes += 1
    
	
class Filme(Programa): 

	def __init__(self, nome, ano, duracao):
		super().__init__(nome, ano)
		self.duracao = duracao

	def __str__(self):
	    return f'{self._nome} - {self.ano} - {self.likes} Likes - {self.duracao} min.'

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas  

    def __str__(self):
	    return f'{self._nome} - {self.ano} - {self.likes} Likes - {self.temporadas} Temporadas' 
       

class Playlist(list):
	def __init__(self, nome, programas):
		self.nome = nome
		super().__init__(programas)
	
	

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tmep = Filme('todo mundo em panico', 2016, 100)
demolidor = Serie('Demolidor', 2016, 2)
atlanta = Serie('atlanta', 2018, 2)

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

atlanta.dar_like()
vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana :
	print(programa)

print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana }')







