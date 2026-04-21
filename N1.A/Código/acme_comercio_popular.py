import os
import sqlite3
os.system('cls')

conector = sqlite3.connect('acme.db')
cursor = conector.cursor()

try:
    cursor.execute("drop table loja")
    cursor.execute("drop table fornecedores")
    cursor.execute("drop table produto")
    cursor.execute("drop table cliente")
    cursor.execute("drop table vendedor")
    cursor.execute("drop table estoque")
    cursor.execute("drop table entrada_produto")
    cursor.execute("drop table vendas")
    cursor.execute("drop table item_venda")
    cursor.execute("drop table pagamento")
    cursor.execute("drop table pagamento_fornecedor")
    cursor.execute("drop table comissao")
except sqlite3.OperationalError:
    pass

sql = """
   CREATE TABLE loja (
    id_loja INTEGER PRIMARY KEY NOT NULL,
    nome TEXT,
    endereco TEXT,
    telefone TEXT
);

CREATE TABLE fornecedores (
    id_fornecedor INTEGER PRIMARY KEY NOT NULL,
    nome TEXT,
    cnpj TEXT,
    email TEXT,
    telefone TEXT
);

CREATE TABLE produto (
    id_produto INTEGER PRIMARY KEY NOT NULL,
    nome TEXT,
    preco REAL,
    estoque_minimo INTEGER
);

CREATE TABLE cliente (
    id_cliente INTEGER PRIMARY KEY NOT NULL,
    nome TEXT,
    email TEXT,
    telefone TEXT,
    data_cadastro TEXT
);

CREATE TABLE vendedor (
    id_vendedor INTEGER PRIMARY KEY NOT NULL,
    nome TEXT,
    cpf TEXT,
    salario_fixo REAL,
    comissao REAL
);

CREATE TABLE estoque (
    id_estoque INTEGER PRIMARY KEY NOT NULL,
    id_loja INTEGER,
    id_produto INTEGER,
    qtde INTEGER,
    FOREIGN KEY (id_loja) REFERENCES loja (id_loja),
    FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);

CREATE TABLE entrada_produto (
    id_entrada INTEGER PRIMARY KEY NOT NULL,
    id_produto INTEGER,
    id_fornecedor INTEGER,
    id_loja INTEGER,
    qtde INTEGER,
    data_entrada TEXT,
    preco_unitario REAL,
    FOREIGN KEY (id_produto) REFERENCES produto (id_produto),
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedores (id_fornecedor),
    FOREIGN KEY (id_loja) REFERENCES loja (id_loja)
);

CREATE TABLE vendas (
    id_vendas INTEGER PRIMARY KEY NOT NULL,
    id_loja INTEGER,
    id_cliente INTEGER,
    id_vendedor INTEGER,
    data_venda TEXT,
    valor_total REAL,
    FOREIGN KEY (id_loja) REFERENCES loja (id_loja),
    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente),
    FOREIGN KEY (id_vendedor) REFERENCES vendedor (id_vendedor)
);

CREATE TABLE item_venda (
    id_item_venda INTEGER PRIMARY KEY NOT NULL,
    id_vendas INTEGER,
    id_produto INTEGER,
    qtde INTEGER,
    preco_unitario REAL,
    FOREIGN KEY (id_vendas) REFERENCES vendas (id_vendas),
    FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);

CREATE TABLE pagamento (
    id_pagamento INTEGER PRIMARY KEY NOT NULL,
    id_vendas INTEGER,
    metodo_pgto TEXT,
    valor REAL,
    FOREIGN KEY (id_vendas) REFERENCES vendas (id_vendas)
);

CREATE TABLE pagamento_fornecedor (
    id_pagamento INTEGER PRIMARY KEY NOT NULL,
    id_fornecedor INTEGER,
    valor REAL,
    data_pagamento TEXT,
    status TEXT,
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedores (id_fornecedor)
);

CREATE TABLE comissao (
    id_comissao INTEGER PRIMARY KEY NOT NULL,
    id_vendedor INTEGER,
    id_vendas INTEGER,
    valor_comissao REAL,
    FOREIGN KEY (id_vendedor) REFERENCES vendedor (id_vendedor),
    FOREIGN KEY (id_vendas) REFERENCES vendas (id_vendas)
);
"""
cursor.executescript(sql)

conector.commit()
cursor.close()
conector.close()

print("FIM DO PROGRAMA")