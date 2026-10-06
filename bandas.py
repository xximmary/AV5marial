
#create_engine é uma "ponte" entre o programa e o db
#string é só o tipo de dado usado para teto no db
#integer é o tipo de dado usado para números inteiros no db
#declarativebase é uma base para as classes que serão transformadas em tabelas no db
#mapped é pra dizer que um atributo da classe será associado a u campo do db

from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase):
    pass

class Banda:
    def __init__(self, nome : str, genero :str, pais : str, ano_lancamento : str, ):
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

print("Olá, seja bem-vindo(a). por favor, escolha uma das opções a seguir:")
print("1. Inserir")
print("2. Listar")
print("3. Excluir")
opc = input()

#se o usuário quer inserir...
if opc == "1":
        print("Inserindo dados para a banda...")
        nome = input("Nome da banda: ")
        genero = input("Gênero: ")
        pais = input("País: ")
        ano = input("Ano de lançamento: ")

        #banda é do tipo da classe Banda e recebe os atributos que o 
        #usuário disse
        banda = Banda(nome, genero, pais, ano)

        #mandou as info para o db
        session.add(banda)
        session.commit()

        print("Banda inserida com sucesso!")

        #fazendo o mesmo processo para música...
        print("\nInserindo dados para a música...")
        titulo = input("Título da música: ")
        duracao = int(input("Duração em segundos: "))
        bpm = int(input("BPM: "))
        genero = input("Gênero: ")

        musica = Musica(titulo, duracao, bpm, genero, banda)

        session.add(musica)
        session.commit()

        print("Música cadastrada com sucesso!")
#inserção 100% completa