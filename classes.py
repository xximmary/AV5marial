from sqlalchemy import create_engine, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

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

    # back_populates vai relacionar "musicas" da classe Banda à "banda" da classe Musica
    musicas: Mapped[list["Musica"]] = relationship(back_populates="banda")
    
    def __str__(self):
        return f'''
{self.nome}
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
    # back_populates vai relacionar "banda" da classe Musica à "musicas" da classe Banda
    banda: Mapped["Banda"] = relationship(back_populates="musicas")

    def __str__(self):
        return f'''   
{self.titulo}
    duração em segundos: {self.duracao}
    BPM: {self.bpm}
    gênero: {self.genero}
    banda: {self.banda.nome}
'''

# base.metadata... faz o sqlalchemy olhar para as classes que defini como Base e cria
# no db as tabelas que ainda nao existem com as colunas que eu definia
Base.metadata.create_all(engine)