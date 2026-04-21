#============================== AUTORES ==============================
create_table_autores = ['create table g6_autores(\n'
'id_autor int primary key,\n'
'nome varchar(30),\n '
'nomeregistro varchar(30),\n '
'ano_nascimento int,\n '
'cidade_nascimento varchar(30),\n'
'estados_nascimento char(2),\n '
'ano_falecimento int,\n '
'cidade_falecimento char(2)\n'
');\n'
'drop table if exists g6_autores;\n']


Script_autores = ['INSERT INTO `g6_autores` (`id_autor`, `nome`, `nomeregistro`, `ano_nascimento`, `cidade_nascimento`, `estados_nascimento`, `ano_falecimento`, `cidade_falecimento`) VALUES']

arq = open('autores.csv', 'r', encoding='utf-8')
s= arq.readline()
s = arq.readline().rstrip()

while s != '':
    s = s.split(';')
    Script_autores.append(f"('{s[0]}','{s[1]}','{s[2]}','{s[3]}','{s[4]}', '{s[5]}', '{s[6]}', '{s[7]}'),")
    s = arq.readline().rstrip()
arq.close()

Script_autores[-1] = Script_autores[-1].replace('),',');')


arqScript = open('script.txt', 'w', encoding = 'utf-8')

for autores_table in create_table_autores:
     arqScript.write(f"{autores_table}\n\n")
for autores_campos in Script_autores:
    arqScript.write(f"{autores_campos}\n")

#============================== EDITORAS ==============================
create_table_editoras = ['\n\ncreate table g6_editoras(\n'
'id_editoras int primary key,\n'
'nome varchar(30),\n '
'cidade_sede varchar(30),\n '
'ano_fundacao int,\n '
');\n'
'drop table if exists g6_editoras;\n']

Script_editoras = ['INSERT INTO `g6_editores` (`id_editora`, `nome`, `cidade_sede`, `ano_fundacao`) VALUES']

arq = open('editoras.csv', 'r', encoding='utf-8')
s= arq.readline()
s = arq.readline().rstrip()

while s!='':
     s = s.split(';')
     Script_editoras.append(f"('{s[0]}','{s[1]}','{s[2]}','{s[3]}'),")
     s = arq.readline().rstrip()
arq.close()

Script_editoras[-1] = Script_editoras[-1].replace('),',');')


for editoras_table in create_table_editoras:
    arqScript.write(f"{editoras_table}\n\n")

for editora_campos in Script_editoras:
    arqScript.write(f"{editora_campos}\n")




#============================== generos ==============================

create_table_generos = ['\n\ncreate table g6_generos(\n'
'id_genero int primary key,\n'
'descricao varchar(10),\n '
');\n'
'drop table if exists g6_generos;\n']

Script_generos = ['INSERT INTO `g6_editores` (`id_editora`, `descricao`) VALUES']

arq = open('generos.csv', 'r', encoding='utf-8')
s= arq.readline()
s = arq.readline().rstrip()

while s!='':
     s = s.split(';')
     Script_generos.append(f"('{s[0]}','{s[1]}'),")
     s = arq.readline().rstrip()
arq.close()

Script_generos[-1] = Script_generos[-1].replace('),',');')


for genero_tables in create_table_generos:
    arqScript.write(f"{genero_tables}\n\n")

for genero_campos in Script_generos:
    arqScript.write(f"{genero_campos}\n")


#============================== livros ==============================

create_table_livros = ['\n\ncreate table g6_livros(\n'
'id_livro int primary key,\n'
'titulo varchar(50),\n '
'ano_publicao int, \n'
'id_autor int, \n'
'id_genero, \n'
');\n'
'drop table if exists g6_livros;\n']

Script_livros = ['INSERT INTO `g6_livros` (`id_livro`, `titulo`, `ano_publicao`, `id_autor`, `id_genero`) VALUES']

arq = open('livros.csv', 'r', encoding='utf-8')
s= arq.readline()
s = arq.readline().rstrip()

while s!='':
     s = s.split(';')
     Script_livros.append(f"('{s[0]}','{s[1]}','{s[2]}','{s[3]}','{s[4]}'),")
     s = arq.readline().rstrip()
arq.close()

Script_livros[-1] = Script_livros[-1].replace('),',');')


for livros_tables in create_table_livros:
    arqScript.write(f"{livros_tables}\n\n")

for livros_campos in Script_livros:
    arqScript.write(f"{livros_campos}\n")

arqScript.close()