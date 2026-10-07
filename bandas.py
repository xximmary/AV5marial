
#create_engine é uma "ponte" entre o programa e o db
#string é só o tipo de dado usado para teto no db
#integer é o tipo de dado usado para números inteiros no db
#declarativebase é uma base para as classes que serão transformadas em tabelas no db
#mapped é pra dizer que um atributo da classe será associado a u campo do db

from sqlalchemy import create_engine, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///bandas.db")

class Banda(Base):
    __tablename__ = "bandas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String)
    genero: Mapped[str] = mapped_column(String)
    pais: Mapped[str] = mapped_column(String)
    ano: Mapped[str] = mapped_column(String)

    musicas: Mapped[list["Musica"]] = relationship()
    
    def __str__(self):
        return f'''
BANDA
    nome: {self.nome}
    gênero: {self.genero}
    país: {self.pais}
    ano lançamento: {self.ano}
'''

class Musica(Base):
    __tablename__ = "musicas"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String)
    duracao: Mapped[int] = mapped_column(Integer)
    bpm: Mapped[int] = mapped_column(Integer)
    genero: Mapped[str] = mapped_column(String)

    banda_id: Mapped[int] = mapped_column(ForeignKey("bandas.id"))
    banda: Mapped["Banda"] = relationship()

    def __str__(self):
        return f'''   MUSICA
    titulo: {self.titulo}
    duração em segundos: {self.duracao}
    BPM: {self.bpm}
    gênero: {self.genero}
    banda: {self.banda}
'''

lista_musicas = []

# base.metadata... faz o sqlalchemy olhar para as classes que defini como Base e cria
# no db as tabelas que ainda nao existem com as colunas que eu definia
Base.metadata.create_all(engine)
with Session(engine) as session:
    # programa fica aqui dentro

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
            banda = Banda(
                 nome = nome,
                 genero = genero,
                 pais = pais,
                 ano = ano
            )

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

            musica = Musica(
                titulo = titulo,
                duracao = duracao,
                bpm = bpm,
                genero = genero,
                banda = banda)

            session.add(musica)
            session.commit()

            lista_musicas.append(musica)
            print("Música cadastrada com sucesso!")
        #inserção 100% completa

    if opc == "2":
         print("Listando...")
         for i in range(lista_musicas):
              print("música nro", i)
              print(lista_musicas[i])

    if opc == "3":
         # percorre as musicas ja criadas na lista que armazena elas
         for i in range(lista_musicas):
              print(i+1, musica.nome)
              print("da banda", musica.banda.nome)
              print('')

         nroex = int(input("Qual o nro da música que você deseja excluir?"))
         # percorre a lista de musicas de novo e...
         for i in range (lista_musicas):
              # ... verifica se o numero q o usuario pediu é o mesmo da
              # posicao na lista
              if i == nroex - 1:
                   # deleta a info da posição certa
                   del lista_musicas[i]