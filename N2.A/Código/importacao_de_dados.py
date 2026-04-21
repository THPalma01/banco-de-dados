import os
import sqlite3
import csv
os.system('cls')

Editoras = {}
with open('editoras.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas[1:]:
        lst = linha.rstrip().split(';')
        print(lst)

        id_editora = int(lst[0])
        nome = lst[1]
        cidade_sede = lst[2]
        ano_fundacao = int(lst[3])

        Editoras[id_editora] = [nome, cidade_sede, ano_fundacao]

Generos = {}
with open('generos.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas[1:]:
        lst = linha.rstrip().split(';')
        print(lst)

        id_genero = int(lst[0])
        descricao = lst[1]

        Generos[id_genero] = [descricao]

Livros = {}
with open('livros.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas[1:]:
        lst = linha.rstrip().split(';')
        print(lst)

        id_livro = int(lst[0])
        titulo = lst[1]
        ano_publicacao = int(lst[2])
        id_autor = int(lst[3])
        id_editora = int(lst[4])
        id_genero = int(lst[5])

        Livros[id_livro] = [titulo, ano_publicacao, id_autor, id_editora, id_genero]

Autores = {}
with open('autores.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas[1:]:
        lst = linha.rstrip().split(';')
        print(lst)

        id_autor = int(lst[0])
        nome = lst[1]
        nomeregistro = lst[2]
        ano_nascimento = int(lst[3])
        cidade_nascimento = lst[4]
        estado_nascimento = lst[5]
        ano_falecimento = int(lst[6]) if lst[6] != '' else None
        cidade_falecimento = lst[7] if lst[7] != '' else None
        estado_falecimento = lst[8] if lst[8] != '' else None

        Autores[id_autor] = [nome, nomeregistro, ano_nascimento, cidade_nascimento, estado_nascimento, ano_falecimento, cidade_falecimento, estado_falecimento]

conector = sqlite3.connect('literatura.db')
cursor = conector.cursor()

try:
    cursor.execute("drop table Editoras")
    cursor.execute("drop table Generos")
    cursor.execute("drop table Livros")
    cursor.execute("drop table Autores")
except sqlite3.OperationalError:
    pass

sql = """
    create table Editoras(
        id_editora integer, 
        nome text,
        cidade_sede text,
        ano_fundacao numeric
    );

    create table Generos(
        id_genero integer,
        descricao text
    );

    create table Livros(
        id_livro integer,
        titulo text,
        ano_publicacao integer,
        id_autor integer,
        id_editora integer,
        id_genero integer
    );

    create table Autores(
        id_autor integer,
        nome text,
        nome_registro text,
        ano_nascimento numeric,
        cidade_nascimento text,
        estado_nascimento text,
        ano_falecimento numeric,
        cidade_falecimento text,
        estado_falecimento text
    );
"""
cursor.executescript(sql)


sql = """
    insert into Editoras (id_editora, nome, cidade_sede, ano_fundacao) 
    values (?, ?, ?, ?)
    """
for id_editora in Editoras:
    nome, cidade_sede, ano_fundacao = Editoras[id_editora]
    cursor.execute(sql, [id_editora, nome, cidade_sede, ano_fundacao])


sql = """
    insert into Generos (id_genero, descricao) 
    values (?, ?)
    """
for id_genero in Generos:
    descricao = Generos[id_genero][0]
    cursor.execute(sql, [id_genero, descricao])


sql = """
    insert into Livros (id_livro, titulo, ano_publicacao, id_autor, id_editora, id_genero) 
    values (?, ?, ?, ?, ?, ?)
    """
for id_livro in Livros:
    titulo, ano_publicacao, id_autor, id_editora, id_genero = Livros[id_livro]
    cursor.execute(sql, [id_livro, titulo, ano_publicacao, id_autor, id_editora, id_genero])


sql = """
    insert into Autores (id_autor, nome, nome_registro, ano_nascimento, cidade_nascimento, estado_nascimento, ano_falecimento, cidade_falecimento, estado_falecimento)
    values (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
for id_autor in Autores:
    nome, nome_registro, ano_nascimento, cidade_nascimento, estado_nascimento, ano_falecimento, cidade_falecimento, estado_falecimento = Autores[id_autor]
    cursor.execute(sql, [id_autor, nome, nome_registro, ano_nascimento, cidade_nascimento, estado_nascimento, ano_falecimento, cidade_falecimento, estado_falecimento])

conector.commit()
cursor.close()
conector.close()

print("\nFIM DO PROGRAMA")