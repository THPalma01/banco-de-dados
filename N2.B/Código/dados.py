# TRABALHO N2.B - BANCO DE DADOS ADSVA4
#
# RHIAN OLIVEIRA DANTAS
# GUILHERME ALEXANDRE
# THIAGO FATIGATI

import sqlite3
import csv

Repres = {}
with open('Código/Repres.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    next(leitor_csv)
    for lst in leitor_csv:
        cod_repres = int(lst[0])
        tipo_pess = lst[1] 
        nome_fan = lst[2] 
        comissao_base = float(lst[3])

        Repres[cod_repres] = [tipo_pess, nome_fan, comissao_base]

Produtos = {}
with open('Código/Produtos.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    next(leitor_csv)
    for lst in leitor_csv:
        cod_prod = int(lst[0].replace(',', ''))
        nome_prod = lst[1]
        cod_forne = int(float(lst[2])) if lst[2] else None
        unidade = int(lst[3]) if lst[3] else None
        aliq_icms = float(lst[4]) if lst[4] else 0.0
        val_custo = float(lst[5]) if lst[5] else None 
        val_venda = float(lst[6]) if lst[6] else None 
        qtde_min_str = lst[7].replace(',', '') if lst[7] else None
        qtde_min = int(float(qtde_min_str)) if qtde_min_str else 0 
        qtde_estq_str = lst[8].replace(',', '') if lst[8] else None
        qtde_estq = float(qtde_estq_str) if qtde_estq_str else 0.0 
        grupo = int(lst[9]) if lst[9] else None
        classe_stq = lst[10]
        comissao = float(lst[11]) if lst[11] else 0.0 
        peso_bruto = float(lst[12]) if lst[12] else 0.0 

        Produtos[cod_prod] = [nome_prod, cod_forne, unidade, aliq_icms, val_custo, val_venda, qtde_min, qtde_estq, grupo, classe_stq, comissao, peso_bruto]

FornClien = {}
with open('Código/FornClien.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    next(leitor_csv)
    for lst in leitor_csv:
        cod_clifor = int(lst[0].replace(',', ''))
        tipo_cf = int(lst[1])
        cod_repres = int(float(lst[2])) if lst[2] else 0
        nome_fan = lst[3]
        cidade = lst[4] if lst[4] else None
        uf = lst[5] if lst[5] else None
        cod_municipio = int(float(lst[6])) if lst[6] else None
        tipo_pessoa = int(lst[7])
        cobr_banc = int(lst[8])
        prazo_pgto = int(float(lst[9])) if lst[9] else 0

        FornClien[cod_clifor] = [tipo_cf, cod_repres, nome_fan, cidade, uf,cod_municipio, tipo_pessoa, cobr_banc, prazo_pgto]

Pedidos = {}
with open('Código/Pedidos.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    next(leitor_csv)
    for lst in leitor_csv:
        num_ped = int(lst[0].replace(',', ''))
        partes_data = lst[1].split('.')
        data_ped = f"{partes_data[0]}/{partes_data[1]}/{partes_data[2]}"
        hora_ped = lst[2]
        cod_clien = int(lst[3].replace(',', '')) if lst[3] else None
        es = lst[4]
        finalid_nfe = int(lst[5])
        situacao = int(lst[6])
        peso = float(lst[7].replace(',', '')) if lst[7] else None
        prazo_pgto = int(lst[8])
        valor_prods = float(lst[9].replace(',', '')) if lst[9] else 0.0
        valor_desc = float(lst[10].replace(',', '')) if lst[10] else 0.0
        valor = float(lst[11].replace(',', '')) if lst[11] else 0.0
        val_base_icms = float(lst[12].replace(',', '')) if lst[12] else 0.0
        val_icms = float(lst[13].replace(',', '')) if lst[13] else 0.0
        comissao = float(lst[14].replace(',', '')) if lst[14] else 0.0
        
        Pedidos[num_ped] = [data_ped, hora_ped, cod_clien, es, finalid_nfe, situacao,peso, prazo_pgto, valor_prods, valor_desc, valor,val_base_icms, val_icms, comissao]

PedidosItem = {}
with open('Código/PedidosItem.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    next(leitor_csv)
    for lst in leitor_csv:
        num_ped = int(lst[0].replace(',', ''))
        num_item = int(lst[1])
        cod_prod = int(lst[2].replace(',', ''))
        qtde = float(lst[3])
        val_unit = float(lst[4].replace(',', '')) if lst[4] else 0.0
        unid = lst[5] if lst[5] else None
        aliq_icms = float(lst[6]) if lst[6] else 0.0
        comissao = float(lst[7]) if lst[7] else 0.0
        sticms = int(lst[8]) if lst[8] else 0
        cfop = float(lst[9]) if lst[9] else None
        reduc_base_icms = float(lst[10]) if lst[10] else 0.0
        chave_composta = (num_ped, num_item)

        PedidosItem[num_ped, num_item] = [cod_prod, qtde, val_unit, unid, aliq_icms, comissao, sticms, cfop, reduc_base_icms]

conector = sqlite3.connect('Código/DadosERP.db')
cursor = conector.cursor()

try:
    cursor.execute("drop table Repres")
    cursor.execute("drop table PedidosItem")
    cursor.execute("drop table Pedidos")
    cursor.execute("drop table Produtos")
    cursor.execute("drop table FornClien")
except sqlite3.OperationalError:
    pass

sql = """
   CREATE TABLE Repres (
        cod_repres INTEGER PRIMARY KEY NOT NULL,
        tipo_pess TEXT NOT NULL,
        nome_fan TEXT NOT NULL,
        comissao_base REAL NOT NULL
    );

    CREATE TABLE FornClien (
        cod_clifor INTEGER PRIMARY KEY NOT NULL,
        tipo_cf INTEGER,
        cod_repres INTEGER NOT NULL DEFAULT 0,
        nome_fan TEXT,
        cidade TEXT,
        uf TEXT,
        cod_municipio INTEGER,
        tipo_pessoa TEXT, 
        cobr_banc INTEGER,
        prazo_pgto INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY (cod_repres) REFERENCES Repres (cod_repres)
    );

    CREATE TABLE Produtos (
        cod_prod INTEGER PRIMARY KEY NOT NULL,
        nome_prod TEXT,
        cod_forne INTEGER,
        unidade INTEGER,
        aliq_icms REAL NOT NULL DEFAULT 0,
        val_custo REAL,
        val_venda REAL,
        qtde_min INTEGER NOT NULL DEFAULT 0,
        qtde_estq REAL NOT NULL DEFAULT 0,
        grupo INTEGER,
        classe_stq TEXT,
        comissao REAL NOT NULL DEFAULT 0,
        peso_bruto REAL NOT NULL DEFAULT 0,
        FOREIGN KEY (cod_forne) REFERENCES FornClien (cod_clifor)
        
    );

    CREATE TABLE Pedidos (
        num_ped INTEGER PRIMARY KEY NOT NULL,
        data_ped TEXT,
        hora_ped TEXT,
        cod_clien INTEGER,
        es TEXT,
        finalid_nfe INTEGER,
        situacao INTEGER,
        peso REAL,
        prazo_pgto INTEGER,
        valor_prods REAL NOT NULL DEFAULT 0,
        valor_desc REAL NOT NULL DEFAULT 0,
        valor REAL NOT NULL DEFAULT 0,
        val_base_icms REAL NOT NULL DEFAULT 0,
        val_icms REAL NOT NULL DEFAULT 0,
        comissao REAL NOT NULL DEFAULT 0,
        FOREIGN KEY (cod_clien) REFERENCES FornClien (cod_clifor)
    );

    CREATE TABLE PedidosItem (
        num_ped INTEGER NOT NULL,
        num_item INTEGER NOT NULL,
        cod_prod INTEGER,
        qtde REAL,
        val_unit REAL NOT NULL DEFAULT 0,
        unid TEXT,
        aliq_icms REAL NOT NULL DEFAULT 0,
        comissao REAL NOT NULL DEFAULT 0,
        sticms INTEGER NOT NULL DEFAULT 0,
        cfop REAL,
        reduc_base_icms REAL NOT NULL DEFAULT 0,
        PRIMARY KEY (num_ped, num_item),
        FOREIGN KEY (num_ped) REFERENCES Pedidos (num_ped),
        FOREIGN KEY (cod_prod) REFERENCES Produtos (cod_prod)
    );
"""
cursor.executescript(sql)

#Tabela Repres
sql = """
    insert into Repres (cod_repres, tipo_pess, nome_fan, comissao_base) 
    values (?, ?, ?, ?)
    """
for cod_repres in Repres:
    tipo_pess, nome_fan, comissao_base = Repres[cod_repres]
    cursor.execute(sql, [cod_repres, tipo_pess, nome_fan, comissao_base])

#Tabela Produtos
sql = """
    insert into Produtos (cod_prod, nome_prod, cod_forne, unidade, aliq_icms, val_custo, val_venda, qtde_min, qtde_estq, grupo, classe_stq, comissao, peso_bruto) 
    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

for cod_prod in Produtos:
    nome_prod, cod_forne, unidade, aliq_icms, val_custo, val_venda, qtde_min, qtde_estq, grupo, classe_stq, comissao, peso_bruto = Produtos[cod_prod]

    grupo_tratado = grupo
    if grupo_tratado is not None:
        grupo_tratado = abs(grupo_tratado) 
    
    cursor.execute(sql, [cod_prod, nome_prod, cod_forne, unidade, aliq_icms, val_custo, val_venda, qtde_min, qtde_estq, grupo_tratado, classe_stq, comissao, peso_bruto])

#Tabela FornClien
sql = """
    insert into FornClien (cod_clifor, tipo_cf, cod_repres, nome_fan, cidade, uf, cod_municipio, tipo_pessoa, cobr_banc, prazo_pgto) 
    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

for cod_clifor in FornClien:
    tipo_cf, cod_repres, nome_fan, cidade, uf, cod_municipio, tipo_pessoa, cobr_banc, prazo_pgto = FornClien[cod_clifor]
    
    if tipo_pessoa == 1:
        tipo_pessoa_tratada = 'PF'
    elif tipo_pessoa == 2:
        tipo_pessoa_tratada = 'PJ'
    else:
        tipo_pessoa_tratada = None

    cidade_tratada = cidade
    if cidade_tratada: 
        cidade_tratada = cidade_tratada.upper().replace('SÃO PAULO', 'SAO PAULO').replace('SAO PAULOI', 'SAO PAULO')
    
    uf_tratada = uf
    if uf_tratada: 
        uf_tratada = uf_tratada.upper()
        if uf_tratada in ('RP', 'TS'): 
            uf_tratada = None
    
    if cidade_tratada == 'SAO PAULO':
        uf_tratada = 'SP'
    
    cod_municipio_tratado = cod_municipio
    if cidade_tratada == 'SAO PAULO':
        cod_municipio_tratado = 3550308
     
    cursor.execute(sql, [cod_clifor, tipo_cf, cod_repres, nome_fan, cidade_tratada, uf_tratada, cod_municipio_tratado, tipo_pessoa_tratada, cobr_banc, prazo_pgto])

#Tabela Pedidos
sql = """
    insert into Pedidos (num_ped, data_ped, hora_ped, cod_clien, es, finalid_nfe, situacao, peso, prazo_pgto, valor_prods, valor_desc, valor, val_base_icms, val_icms, comissao) 
    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

for num_ped in Pedidos:
    data_ped, hora_ped, cod_clien, es, finalid_nfe, situacao, peso, prazo_pgto, valor_prods, valor_desc, valor, val_base_icms, val_icms, comissao = Pedidos[num_ped]
    cursor.execute(sql, [num_ped, data_ped, hora_ped, cod_clien, es, finalid_nfe, situacao, peso, prazo_pgto, valor_prods, valor_desc, valor, val_base_icms, val_icms, comissao])

#Tabela PedidosItem
sql = """
    insert into PedidosItem (num_ped, num_item, cod_prod, qtde, val_unit, unid, aliq_icms, comissao, sticms, cfop, reduc_base_icms) 
    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

for chave_composta in PedidosItem:
    num_ped = chave_composta[0]
    num_item = chave_composta[1]
    
    cod_prod, qtde, val_unit, unid, aliq_icms, comissao, sticms, cfop, reduc_base_icms = PedidosItem[chave_composta]
    unid_tratada = unid
    if unid_tratada is not None:
        unid_tratada = unid_tratada.lower().replace('ç', 'c') 
    cursor.execute(sql, [num_ped, num_item, cod_prod, qtde, val_unit, unid_tratada, aliq_icms, comissao, sticms, cfop, reduc_base_icms])

conector.commit()
cursor.close()
conector.close()

print("\nFIM DO PROGRAMA")