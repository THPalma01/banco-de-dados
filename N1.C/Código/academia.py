import os
import sqlite3
os.system('cls')

conector = sqlite3.connect('academia.db')
cursor = conector.cursor()

try:
    cursor.execute("drop table a_receber")
    cursor.execute("drop table planos")
    cursor.execute("drop table aluno")
    cursor.execute("drop table matricula")
    cursor.execute("drop table frequencia_aluno")
    cursor.execute("drop table profissional")
    cursor.execute("drop table atribuicao")
    cursor.execute("drop table turma")
    cursor.execute("drop table telefone_profissional")
    cursor.execute("drop table tipo_atividade")
except sqlite3.OperationalError:
    pass

sql = """  
     CREATE TABLE aluno (
    id_aluno INTEGER PRIMARY KEY NOT NULL,
    codigo_matricula INTEGER,
    data_matricula TEXT,
    nome TEXT,
    endereco TEXT,
    telefone TEXT,
    data_nasc TEXT,
    altura REAL,
    peso REAL
);

CREATE TABLE planos (
    id_plano INTEGER PRIMARY KEY NOT NULL,
    nome_plano TEXT,
    valor REAL,
    duracao_meses INTEGER
);

CREATE TABLE tipo_atividade (
    id_atvd INTEGER PRIMARY KEY NOT NULL,
    nome_atvd TEXT,
    modalidade TEXT,
    descricao TEXT
);

CREATE TABLE profissional (
    id_profissional INTEGER PRIMARY KEY NOT NULL,
    rg_profissional TEXT,
    nome TEXT,
    data_nasc TEXT,
    titulacao TEXT,
    email TEXT
);

CREATE TABLE telefone_profissional (
    id_telefone INTEGER PRIMARY KEY NOT NULL,
    id_profissional INTEGER,
    telefone TEXT,
    FOREIGN KEY (id_profissional) REFERENCES profissional (id_profissional)
);

CREATE TABLE turma (
    id_turma INTEGER PRIMARY KEY NOT NULL,
    id_atvd INTEGER,
    rg_profissional TEXT,
    qtde_alunos INTEGER,
    dia_horario TEXT,
    duracao INTEGER,
    data_inicio TEXT,
    data_fim TEXT,
    FOREIGN KEY (id_atvd) REFERENCES tipo_atividade (id_atvd)
);

CREATE TABLE a_receber (
    id_a_receber INTEGER PRIMARY KEY NOT NULL,
    id_aluno INTEGER,
    id_plano INTEGER,
    valor REAL,
    data_vencimento TEXT,
    status INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES aluno (id_aluno),
    FOREIGN KEY (id_plano) REFERENCES planos (id_plano)
);

CREATE TABLE matricula (
    id_matricula INTEGER PRIMARY KEY NOT NULL,
    id_aluno INTEGER,
    id_turma INTEGER,
    data_matricula TEXT,
    status INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES aluno (id_aluno),
    FOREIGN KEY (id_turma) REFERENCES turma (id_turma)
);

CREATE TABLE frequencia_aluno (
    id_frequencia INTEGER PRIMARY KEY NOT NULL,
    id_matricula INTEGER,
    id_turma INTEGER,
    data TEXT,
    status INTEGER,
    FOREIGN KEY (id_matricula) REFERENCES matricula (id_matricula),
    FOREIGN KEY (id_turma) REFERENCES turma (id_turma)
);

CREATE TABLE atribuicao (
    id_profissional INTEGER NOT NULL,
    id_turma INTEGER NOT NULL,
    funcao TEXT,
    PRIMARY KEY (id_profissional, id_turma),
    FOREIGN KEY (id_profissional) REFERENCES profissional (id_profissional),
    FOREIGN KEY (id_turma) REFERENCES turma (id_turma)
);
"""
cursor.executescript(sql)

conector.commit()
cursor.close()
conector.close()

print("FIM DO PROGRAMA")