
# create_engine é uma "ponte" entre o programa e o db
# string é só o tipo de dado usado para teto no db
# integer é o tipo de dado usado para números inteiros no db
# declarativebase é uma base para as classes que serão transformadas em tabelas no db
# mapped é pra dizer que um atributo da classe será associado a u campo do db
# select serve para montar uma consulta que busca informações no db

from sqlalchemy import select
from sqlalchemy.orm import Session
from classes import engine, Banda, Musica

from db import conectar_sqlite, conectar_mysql
print("Escolha o banco de dados:")
print("1. SQLite")
print("2. MySQL")
escolha = input("")

if escolha == "1":
    engine = conectar_sqlite()
elif escolha == "2":
    engine = conectar_mysql()
else:
    print("Opção inválida!")
    exit()

# programa real fica aqui dentro
with Session(engine) as session:
    
    opc = ""
    while opc != "6":
        print("\nPor favor, escolha uma das opções a seguir:")
        print("1. Inserir BANDA")
        print("2. Inserir MUSICA")
        print("3. Listar")
        print("4. Excluir")
        print("5. Mudar BANCO DE DADOS")
        print("6. Sair")
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

        elif opc == "2":
                #fazendo o mesmo processo de banda para música...
                print("\nInserindo dados para a música...")

                # o significado das coisas abaixo está no prox. elif =)
                consulta = select(Banda)
                bandas = session.scalars(consulta)

                for banda in bandas:
                    print(banda.nome)
                    print("ID:", banda.id)
                
                id_banda = int(input("Digite o ID da banda da música:"))
                consulta = select(Banda).where(Banda.id == id_banda)
                banda = session.scalar(consulta)

                if banda:
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

                    print("Música cadastrada com sucesso!")
                   #inserção 100% completa
                else:
                    print("Banda não encontrada!")

        elif opc == "3":
            print("\n Listando as bandas...")

            # consulta vai representar objetos da classe Banda
            consulta = select(Banda)
            # executa a consulta e retorna os objetos encontrados sendo como consulta/sendo do tipo Banda
            bandas = session.scalars(consulta)

            # percorre todas as bandas encontradas e da print nelas
            for banda in bandas:
                print(banda)

            # começa a fazer o mesmo passo a passo para musicas...
            print("\n Listando as musicas...")
            consulta = select(Musica)
            musicas = session.scalars(consulta)
            for musica in musicas:
                print(musica)

        elif opc == "4":
            print("O que você deseja excluir?")
            print("1. Banda")
            print("2. Musica")
            escolha = input()

            # os dois if fazem a mesma coisa, so que um pra banda e outro pra musica
            if escolha == "1":
                # mesmo passo a passo de antes (na opc 2)
                consulta = select(Banda)
                bandas = session.scalars(consulta)

                for banda in bandas:
                    print("ID:", banda.id)
                    print(banda)

                id_banda = int(input("Digite o ID da banda que deseja apagar:"))
                #consulta vai ser um objeto do tipo Banda que tiver o mesmo id que o usuário escolheu (guardado na variavel id_banda)
                consulta = select(Banda).where(Banda.id == id_banda)
                # retorna o objeto
                banda = session.scalar(consulta)

                # verifica antes se banda existe para evitar erros
                if banda:
                    # se essa badna ainda tem músicas, para evitar erro, vamos pedir pro usuário
                    # apaga-las primeiro
                    if banda.musicas:
                        print("Não é possível excluir essa banda! Exclua as músicas dela primeiro")
                    else:
                # apaga banda com delete e envia isso ao db usando commit
                        session.delete(banda)
                        session.commit()
                        print("Banda excluída com sucesso!")
                else:
                    print("Banda não encontrada!")
            elif escolha == "2":
                consulta = select(Musica)
                musicas = session.scalars(consulta)
                for musica in musicas:
                    print("ID:", musica.id)
                    print(musica)

                id_musica = int(input("Digite o ID da música que deseja apagar:"))
                consulta = select(Musica).where(Musica.id == id_musica)
                musica = session.scalar(consulta)

                if musica:
                    session.delete(musica)
                    session.commit()
                    print("Música excluída com sucesso!")
                else:
                    print("Musica não encontrada!")
        elif opc == "5":
            print("Para qual banco de dados você deseja migrar?")
            print("1. SQLite")
            print("2. MySQL")
            escolha = input("")
            if escolha == "1":
                conectar_sqlite()
                print("Banco de dados alterao com sucesso!")
            elif escolha == "2":
                conectar_mysql()
                print("Banco de dados alterao com sucesso!")

