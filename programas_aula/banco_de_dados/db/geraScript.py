
Script = ['INSERT INTO `g5_genero` (`id_genero`, `descricao`) VALUES']
arq = open('generos.csv', 'r', encoding='utf-8')
s = arq.readline()
s= arq.readline().rstrip()
while s != '':
    s = s.split(';')
    Script.append(f"('{s[0]}', '{s[1]}'), ")
    s = arq.readline().rstrip()

arq.close()

Script[-1] = Script[-1].replace('),', ');')

for linha in Script:
    print(linha)

arqScript = open('script.txt', 'w', encoding='utf-8')
for linha in Script:
    arqScript.write(f"{linha}\n")



Script = ['INSERT INTO `g5_autor` (`id_autor`, `nome`, `nomeregistro`, `ano_nascimento`, `cidade_nascimento`, `estado_nascimento`, `ano_falecimento`, `cidade_falecimento`, `estado_falecimento`) VALUES']
arq = open('autores.csv', 'r', encoding='utf-8')
s = arq.readline()
s= arq.readline().rstrip()
while s != '':
    s = s.split(';')
    Script.append(f"('{s[0]}', '{s[1]}', '{s[2]}', '{s[3]}', '{s[4]}', '{s[5]}', '{s[6]}', '{s[7]}', '{s[8]}'), ")
    s = arq.readline().rstrip()

arq.close()

Script[-1] = Script[-1].replace('),', ');')

for linha in Script:
    print(linha)

for linha in Script:
    arqScript.write(f"{linha}\n")



Script = ['INSERT INTO `g5_editora` (`id_editora`, `nome`, `cidade_sede`, `ano_fundacao`) VALUES']
arq = open('editoras.csv', 'r', encoding='utf-8')
s = arq.readline()
s= arq.readline().rstrip()
while s != '':
    s = s.split(';')
    Script.append(f"('{s[0]}', '{s[1]}', '{s[2]}', '{s[3]}'), ")
    s = arq.readline().rstrip()

arq.close()

Script[-1] = Script[-1].replace('),', ');')

for linha in Script:
    print(linha)

for linha in Script:
    arqScript.write(f"{linha}\n")



Script = ['INSERT INTO `g5_livro` (`id_livro`, `titulo`, `ano_publicacao`, `id_autor`, `id_editora`, `id_genero`) VALUES']
arq = open('livros.csv', 'r', encoding='utf-8')
s = arq.readline()
s= arq.readline().rstrip()
while s != '':
    s = s.split(';')
    Script.append(f"('{s[0]}', '{s[1]}', '{s[2]}', '{s[3]}', '{s[4]}', '{s[5]}'), ")
    s = arq.readline().rstrip()

arq.close()

Script[-1] = Script[-1].replace('),', ');')

for linha in Script:
    print(linha)

for linha in Script:
    arqScript.write(f"{linha}\n")
arqScript.close()