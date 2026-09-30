class Banda:
    def __init__(self, nome : str, genero :str, pais : str, ano_lancamento : str):
        self.nome = nome
        self.genero = genero
        self.pais = pais
        self.ano = ano_lancamento
    def __str__(self):
        return f'''
BANDA
    nome: {self.nome}
    gênero: {self.genero}
    país: {self.pais}
    ano lançamento: {self.ano}
'''

class Musica:
    def __init__(self, titulo : str, duracao_segundos : int, bpm : int, genero : str, banda : Banda):
        self.titulo = titulo
        self.duracao = duracao_segundos
        self.bpm = bpm
        self.genero = genero
        self.banda = banda
    def __str__(self):
        return f'''   MUSICA
    titulo: {self.titulo}
    duração em segundos: {self.duracao}
    BPM: {self.bpm}
    gênero: {self.genero}
    banda: {self.banda}
'''
b1 = Banda("deftones", "nu metal, metal alternativo", "Estados Unidos", "1988")
m1 = Musica("root", 220, 91, "nu metal", b1)

print(m1)
